from abc import ABC, abstractmethod

class IProductServicePort(ABC):

    @abstractmethod
    def getAll(self):
        pass

    @abstractmethod
    def create(self, productRequest):
        pass
    
    @abstractmethod
    def getById(self, id):
        pass
    
    @abstractmethod
    def updateById(self, id, productRequest):
        pass

    @abstractmethod
    def deleteById(self, id):
        pass