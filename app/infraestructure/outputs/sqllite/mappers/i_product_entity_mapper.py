from app.domain.models.product_model import ProductModel
from app.infraestructure.outputs.sqllite.entities.product_entity import ProductEntity

class IProductEntityMapper():

    @staticmethod
    def mapProductModelToProductEntity(productModel: ProductModel):
        if not isinstance(productModel, ProductModel):
            raise TypeError("El argumento debe ser una instancia de ProductModel")

        return ProductEntity(
            name=productModel.getName(),
            code=productModel.getCode(),
            price=productModel.getPrice()
        )

    @staticmethod
    def mapProductEntityToProductModel(productEntity: ProductEntity):
        if not isinstance(productEntity, ProductEntity):
            raise TypeError("El argumento debe ser una instancia de ProductEntity")

        return ProductModel(
            id=productEntity.getId(),
            name=productEntity.getName(),
            code=productEntity.getCode(),
            price=productEntity.getPrice()
        )
