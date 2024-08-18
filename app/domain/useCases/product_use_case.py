from app.domain.apis.i_services_product_port import IProductServicePort
from app.domain.spi.i_product_persistence_port import IProductPersistencePort


class ProductUseCase(IProductServicePort):

    def __init__(self, iProductPersistencePort: IProductPersistencePort):
        self.iProductPersistencePort = iProductPersistencePort
    
    #OVERRIDE
    def getAll(self):
        return self.iProductPersistencePort.getAll()

    #OVERRIDE
    def create(self, productRequest):
        return self.iProductPersistencePort.create(productRequest=productRequest)
    
    #OVERRIDE
    def getById(self, id):
        return self.iProductPersistencePort.getById(id=id)
    
    #OVERRIDE
    def updateById(self, id, productRequest):
        return self.iProductPersistencePort.updateById(id=id, productRequest=productRequest)

    #OVERRIDE
    def deleteById(self, id):
        return self.iProductPersistencePort.deleteById(id=id)