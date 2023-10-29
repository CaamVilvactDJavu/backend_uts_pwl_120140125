import logging

import grpc
import client.grpc.productGRPC as productGRPC
import client.grpc.product as product


class ProductClient:
    def __init__(self):
        self.host = "localhost"
        self.server_port = 6000

        self.channel = grpc.insecure_channel(f"{self.host}:{self.server_port}")
        self.stub = productGRPC.ProductsStub(self.channel)

    def create_product(self, name, price, description, image_url, stock):
        response = self.stub.CreateProduct(
            product.ProductCreateRequest(
                name=name,
                price=price,
                description=description,
                image_url=image_url,
                stock=stock,
            )
        )
        return dict(
            id=response.product.id,
            name=response.product.name,
            price=response.product.price,
            description=response.product.description,
            image_url=response.product.image_url,
            stock=response.product.stock,
        )

    def get_product(self, id):
        response = self.stub.GetProduct(product.ProductRequest(id=id))

        if response.product.id == 0:
            return None

        return dict(
            id=response.product.id,
            name=response.product.name,
            price=response.product.price,
            description=response.product.description,
            image_url=response.product.image_url,
            stock=response.product.stock,
        )

    def get_products(self):
        response = self.stub.GetProducts(product.ProductListRequest())

        if len(response.products) == 0:
            return None

        return [
            dict(
                id=product.id,
                name=product.name,
                price=product.price,
                description=product.description,
                image_url=product.image_url,
                stock=product.stock,
            )
            for product in response.products
        ]

    def update_product(self, id, name, price, description, image_url, stock):
        response = self.stub.UpdateProduct(
            product.ProductUpdateRequest(
                id=id,
                name=name,
                price=price,
                description=description,
                image_url=image_url,
                stock=stock,
            )
        )

        if response.product.id == 0:
            return None

        return dict(
            id=response.product.id,
            name=response.product.name,
            price=response.product.price,
            description=response.product.description,
            image_url=response.product.image_url,
            stock=response.product.stock,
        )

    def delete_product(self, id):
        response = self.stub.DeleteProduct(
            product.ProductDeleteRequest(id=id))

        if response.message is None:
            return None

        return dict(message=response.message)

    def sum_price_product(self, id):
        response = self.stub.SumPriceProducts(
            product.ProductSumPriceRequest(id=id)
        )

        if response.price is None:
            return None

        return dict(pro=response.price)
