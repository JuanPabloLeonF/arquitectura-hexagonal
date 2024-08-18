from app.application.dtos.product_response import ProductResponse
from app.domain.models.product_model import ProductModel


class ProductResponseMapper():

    @staticmethod
    def mapProductModelToProductResponse(productModel: ProductModel):
        if not isinstance(productModel, ProductModel):
            raise TypeError("El argumento debe ser una instancia de ProductModel")

        return ProductResponse(
            name=productModel.getName(),
            code=productModel.getCode(),
            price=productModel.getPrice()
        )

    @staticmethod
    def mapProductResponseToProductModel(productResponse: ProductResponse):
        if not isinstance(productResponse, ProductResponse):
            raise TypeError("El argumento debe ser una instancia de ProductResponse")

        return ProductModel(
            name=productResponse.getName(),
            code=productResponse.getCode(),
            price=productResponse.getPrice()
        )
