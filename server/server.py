from concurrent import futures
from math import prod
import time
import logging
import productGRPC
import grpc
import product
from sqlalchemy import insert, text, values, select, update, delete, desc

from database.config import engine
from models.product import Product


class ProductsServicer(productGRPC.ProductsServicer):
    def GetProduct(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                res = conn.execute(
                    select(Product).where(Product.id == request.id)
                ).first()

                conn.commit()

            return product.ProductResponse(
                product=product.Product(
                    id=res[0],
                    name=res[1],
                    price=res[2],
                    description=res[3],
                    stock=res[4],
                    image_url=res[5],
                ),
                message="Product retrieved",
            )
        except Exception as e:
            print(f"Error fd {e}")
            return product.ProductResponse(message="Error")

    def GetProducts(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                res = conn.execute(
                    select(Product).order_by(desc(Product.id))).all()

                products = []

                for row in res:
                    products.append(
                        product.Product(
                            id=row[0],
                            name=row[1],
                            price=row[2],
                            description=row[3],
                            stock=row[4],
                            image_url=row[5],
                        )
                    )

                conn.commit()

            return product.ProductListResponse(
                products=products,
                message="Products retrieved",
            )
        except Exception as e:
            print(f"Error df {e}")
            return product.ProductListResponse(message="Error")

    def CreateProduct(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                res = conn.execute(
                    insert(Product).values(
                        name=request.name,
                        description=request.description,
                        price=request.price,
                        stock=request.stock,
                        image_url=request.image_url,
                    )
                )

                conn.commit()

            print(f"Product {request.name} created")

            return product.ProductResponse(
                product=product.Product(
                    name=request.name,
                    description=request.description,
                    price=request.price,
                    image_url=request.image_url,
                    stock=request.stock,
                ),
                message="Product created",
            )

        except Exception as e:
            print(f"Error sd {e}")
            return product.ProductResponse(message="Error")

    def UpdateProduct(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                res = conn.execute(
                    update(Product)
                    .where(Product.id == request.id)
                    .values(
                        name=request.name,
                        description=request.description,
                        price=request.price,
                        stock=request.stock,
                        image_url=request.image_url,
                    )
                )

                conn.commit()

            print(f"Product {request.name} updated")

            return product.ProductResponse(
                product=product.Product(
                    id=request.id,
                    name=request.name,
                    description=request.description,
                    price=request.price,
                    image_url=request.image_url,
                    stock=request.stock,
                ),
                message="Product updated",
            )

        except Exception as e:
            print(f"Error as {e}")
            return product.ProductResponse(message="Error")

    def DeleteProduct(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                conn.execute(delete(Product).where(Product.id == request.id))

                conn.commit()

            return product.ProductDeleteResponse(message="Product deleted")

        except Exception as e:
            print(f"Error as {e.with_traceback()}")
            return product.ProductDeleteResponse(message="Error")

    def SumPriceProducts(self, request, context):
        try:
            price = 0

            ids = request.id

            for id in ids:
                with engine.connect() as conn:
                    conn.begin()

                    res = conn.execute(select(Product).where(
                        Product.id == id)).first()

                    if res is not None:
                        conn.execute(
                            update(Product)
                            .where(Product.id == id)
                            .values(stock=res[4] - 1)
                        )

                        price += res[2]

                    conn.commit()

            return product.ProductSumPriceResponse(
                price=price,
            )

        except Exception as e:
            print(f"Error df {e}")
            return product.ProductSumPriceResponse()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    productGRPC.add_ProductsServicer_to_server(
        ProductsServicer(), server)
    server.add_insecure_port("localhost:6000")
    server.start()
    print("Server started at localhost:6000")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
