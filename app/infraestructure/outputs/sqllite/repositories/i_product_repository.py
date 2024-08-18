from app.infraestructure.outputs.sqllite.entities.product_entity import ProductEntity
from app.infraestructure.outputs.sqllite.mappers.i_product_entity_mapper import IProductEntityMapper
from app.infraestructure.outputs.sqllite.configurations.database_config import db
from sqlalchemy.exc import IntegrityError

class IProductRepository():

    def __init__(self, iProductEntityMapper: IProductEntityMapper):
        self.iProductEntityMapper = iProductEntityMapper

    def getAll(self):
        products = ProductEntity.query.all()
        productList = []
        for product in products:
            productModel = self.iProductEntityMapper.mapProductEntityToProductModel(product)
            productList.append(productModel)
        return productList

    def create(self, productRequest):
        try:
            productEntity = ProductEntity(name=productRequest.getName(),code=productRequest.getCode(),price=productRequest.getPrice())
            db.session.add(productEntity)
            db.session.commit()
            productModel = self.iProductEntityMapper.mapProductEntityToProductModel(productEntity)
            return productModel.to_dict()
        except IntegrityError as e:
            db.session.rollback()
            return {
                    "status": "BAD_REQUEST",
                    "statusCode": 400,
                    "message": "Product already exists"
                }
        except Exception as e:
            db.session.rollback()
            raise e
        
    def getById(self, id):
        try:
            product = ProductEntity.query.get(id)
            if product is None:
                raise ValueError(f"Producto no encontrado con el id: {id}")
            return self.iProductEntityMapper.mapProductEntityToProductModel(product)
        except ValueError as e:
            return {
                "status": "NOT_FOUND",
                "statusCode": 404,
                "message": str(e)
            }
        except Exception as e:
            raise e
        
    def updateById(self, id, productRequest):
        try:
            product = ProductEntity.query.get(id)
            if product is None:
                raise ValueError(f"Producto no encontrado con el id: {id}")
            product.name = productRequest.getName()
            product.price = productRequest.getPrice()
            product.code = productRequest.getCode()
            db.session.commit()
            return self.iProductEntityMapper.mapProductEntityToProductModel(product)
        except ValueError as e:
            return {
                "status": "NOT_FOUND",
                "statusCode": 404,
                "message": str(e)
            }
        except Exception as e:
            db.session.rollback()
            return {
                "status": "ERROR",
                "statusCode": 500,
                "message": "Ocurrió un error al actualizar el producto"
            }

    def deleteById(self, id):
        try:
            product = ProductEntity.query.get(id)
            if product is None:
                raise ValueError(f"Producto no encontrado con el id: {id}")
            db.session.delete(product)
            db.session.commit()
            return {
                "status": "SUCCESS",
                "statusCode": 200,
                "message": f"Producto con id {id} eliminado exitosamente"
            }
        except ValueError as e:
            return {
                "status": "NOT_FOUND",
                "statusCode": 404,
                "message": str(e)
            }
        except Exception as e:
            db.session.rollback()
            return {
                "status": "ERROR",
                "statusCode": 500,
                "message": "Ocurrió un error al eliminar el producto"
            }
