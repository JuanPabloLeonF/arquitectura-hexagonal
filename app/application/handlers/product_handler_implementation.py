from app.application.handlers.i_product_handler import IProductHandler
from app.application.mappers.i_product_request_mapper import ProductRequestMapper
from app.application.mappers.i_product_response_mapper import ProductResponseMapper
from app.domain.apis.i_services_product_port import IProductServicePort


class ProductHandlerImplementation(IProductHandler):

    def __init__(self, iProductServicePort: IProductServicePort, productRequestMapper: ProductRequestMapper, productResponseMapper: ProductResponseMapper):
        self.iProductServicePort = iProductServicePort
        self.productRequestMapper = productRequestMapper
        self.productResponseMapper = productResponseMapper

    #OVERRRIDE
    def getAll(self):
        listProductDataBase = self.iProductServicePort.getAll()
        listProducts = []
        for productModel in listProductDataBase:
            productResponse = self.productResponseMapper.mapProductModelToProductResponse(productModel=productModel)
            listProducts.append(productResponse.to_dict())
        return listProducts

    #OVERRRIDE
    def create(self, productData):
        productRequest = self.productRequestMapper.mapProductDataToProductRequest(name=productData.get('name'), code=productData.get('code'), price=productData.get('price'))
        return self.iProductServicePort.create(productRequest=productRequest)
    
    #OVERRRIDE
    def getById(self, id):
        productModel = self.iProductServicePort.getById(id=id)
        productResponse = self.productResponseMapper.mapProductModelToProductResponse(productModel=productModel)
        return productResponse.to_dict()
    
    #OVERRIDE
    def updateById(self, id, productData):
        productRequest = self.productRequestMapper.mapProductDataToProductRequest(name=productData.get('name'), code=productData.get('code'), price=productData.get('price'))
        productModel = self.iProductServicePort.updateById(id=id, productRequest=productRequest)
        productResponse = self.productResponseMapper.mapProductModelToProductResponse(productModel=productModel)
        return productResponse.to_dict()

    #OVERRIDE
    def deleteById(self, id):
        return self.iProductServicePort.deleteById(id=id)