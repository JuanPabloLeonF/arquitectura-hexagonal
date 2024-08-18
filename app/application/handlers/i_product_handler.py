from abc import ABC, abstractmethod

class IProductHandler(ABC):

    @abstractmethod
    def getAll(self):
        pass

    @abstractmethod
    def create(self, productData):
        pass
    
    @abstractmethod
    def getById(self, id):
        pass
    
    @abstractmethod
    def updateById(self, id, productData):
        pass

    @abstractmethod
    def deleteById(self, id):
        pass