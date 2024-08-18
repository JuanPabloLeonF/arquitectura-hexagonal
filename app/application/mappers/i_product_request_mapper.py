from app.application.dtos.product_request import ProductRequest
from app.domain.models.product_model import ProductModel
from app.infraestructure.outputs.sqllite.entities.product_entity import ProductEntity


class ProductRequestMapper():

    @staticmethod
    def mapProductDataToProductRequest(name, code, price):
        if (name is None or code is None or price is None) and (not isinstance(name, str) or not isinstance(code, str) or not isinstance(price, int)):
            raise TypeError("El argumento debe ser una instancia de str o int y no debe ser None")

        return ProductRequest(
            name=name,
            code=code,
            price=price
        )


    @staticmethod
    def mapProductModelToProductRequest(productModel: ProductModel):
        if not isinstance(productModel, ProductModel):
            raise TypeError("El argumento debe ser una instancia de ProductModel")

        return ProductRequest(
            name=productModel.getName(),
            code=productModel.getCode(),
            price=productModel.getPrice()
        )

    @staticmethod
    def mapProductRequestToProductModel(productRequest: ProductRequest):
        if not isinstance(productRequest, ProductRequest):
            raise TypeError("El argumento debe ser una instancia de ProductRequest")

        return ProductModel(
            name=productRequest.getName(),
            code=productRequest.getCode(),
            price=productRequest.getPrice()
        )
        
    @staticmethod
    def mapProductRequestToProductEntity(productRequest: ProductRequest):
        if not isinstance(productRequest, ProductRequest):
            raise TypeError("El argumento debe ser una instancia de ProductRequest")

        return ProductEntity(
            name=productRequest.getName(),
            code=productRequest.getCode(),
            price=productRequest.getPrice()
        )
