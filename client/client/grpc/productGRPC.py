# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import client.grpc.product as product_


class ProductsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetProduct = channel.unary_unary(
            "/products.Products/GetProduct",
            request_serializer=product_.ProductRequest.SerializeToString,
            response_deserializer=product_.ProductResponse.FromString,
        )
        self.GetProducts = channel.unary_unary(
            "/products.Products/GetProducts",
            request_serializer=product_.ProductListRequest.SerializeToString,
            response_deserializer=product_.ProductListResponse.FromString,
        )
        self.CreateProduct = channel.unary_unary(
            "/products.Products/CreateProduct",
            request_serializer=product_.ProductCreateRequest.SerializeToString,
            response_deserializer=product_.ProductResponse.FromString,
        )
        self.UpdateProduct = channel.unary_unary(
            "/products.Products/UpdateProduct",
            request_serializer=product_.ProductUpdateRequest.SerializeToString,
            response_deserializer=product_.ProductResponse.FromString,
        )
        self.DeleteProduct = channel.unary_unary(
            "/products.Products/DeleteProduct",
            request_serializer=product_.ProductDeleteRequest.SerializeToString,
            response_deserializer=product_.ProductDeleteResponse.FromString,
        )
        self.SumPriceProducts = channel.unary_unary(
            "/products.Products/SumPriceProducts",
            request_serializer=product_.ProductSumPriceRequest.SerializeToString,
            response_deserializer=product_.ProductSumPriceResponse.FromString,
        )


class ProductsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetProducts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SumPriceProducts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ProductsServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetProduct": grpc.unary_unary_rpc_method_handler(
            servicer.GetProduct,
            request_deserializer=product_.ProductRequest.FromString,
            response_serializer=product_.ProductResponse.SerializeToString,
        ),
        "GetProducts": grpc.unary_unary_rpc_method_handler(
            servicer.GetProducts,
            request_deserializer=product_.ProductListRequest.FromString,
            response_serializer=product_.ProductListResponse.SerializeToString,
        ),
        "CreateProduct": grpc.unary_unary_rpc_method_handler(
            servicer.CreateProduct,
            request_deserializer=product_.ProductCreateRequest.FromString,
            response_serializer=product_.ProductResponse.SerializeToString,
        ),
        "UpdateProduct": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateProduct,
            request_deserializer=product_.ProductUpdateRequest.FromString,
            response_serializer=product_.ProductResponse.SerializeToString,
        ),
        "DeleteProduct": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteProduct,
            request_deserializer=product_.ProductDeleteRequest.FromString,
            response_serializer=product_.ProductDeleteResponse.SerializeToString,
        ),
        "SumPriceProducts": grpc.unary_unary_rpc_method_handler(
            servicer.SumPriceProducts,
            request_deserializer=product_.ProductSumPriceRequest.FromString,
            response_serializer=product_.ProductSumPriceResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "products.Products", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Products(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetProduct(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/products.Products/GetProduct",
            product_.ProductRequest.SerializeToString,
            product_.ProductResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetProducts(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/products.Products/GetProducts",
            product_.ProductListRequest.SerializeToString,
            product_.ProductListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def CreateProduct(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/products.Products/CreateProduct",
            product_.ProductCreateRequest.SerializeToString,
            product_.ProductResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def UpdateProduct(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/products.Products/UpdateProduct",
            product_.ProductUpdateRequest.SerializeToString,
            product_.ProductResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def DeleteProduct(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/products.Products/DeleteProduct",
            product_.ProductDeleteRequest.SerializeToString,
            product_.ProductDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def SumPriceProducts(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/products.Products/SumPriceProducts",
            product_.ProductSumPriceRequest.SerializeToString,
            product_.ProductSumPriceResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
