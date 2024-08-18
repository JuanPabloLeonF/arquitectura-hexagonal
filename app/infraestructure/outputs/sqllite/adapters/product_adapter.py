from app.domain.spi.i_product_persistence_port import IProductPersistencePort
from app.infraestructure.outputs.sqllite.repositories.i_product_repository import IProductRepository

class ProductAdapter(IProductPersistencePort):

    def __init__(self, iProductRepository: IProductRepository):
        self.iProductRepository = iProductRepository

    #OVERRIDE
    def getAll(self):
        return self.iProductRepository.getAll()

    #OVERRIDE
    def create(self, productRequest):
        return self.iProductRepository.create(productRequest=productRequest)
    
    #OVERRIDE
    def getById(self, id):
        return self.iProductRepository.getById(id=id)
    
    #0VERRIDE
    def updateById(self, id, productRequest):
        return self.iProductRepository.updateById(id=id, productRequest=productRequest)

    #OVERRIDE
    def deleteById(self, id):
        return self.iProductRepository.deleteById(id=id)