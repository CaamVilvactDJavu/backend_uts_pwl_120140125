def includeme(config):
    config.add_route("home", "/")
    config.add_route("product", "/api/v1/product/")
    config.add_route("sum_product_price", "/api/v1/product/sum-price")
