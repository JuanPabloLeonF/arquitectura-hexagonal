class ProductModel():
    def __init__(self, id=None, name=None, code=None, price=None):
        self.__id = id
        self.__name = name
        self.__code = code
        self.__price = price

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getCode(self):
        return self.__code

    def setCode(self, code):
        self.__code = code

    def getPrice(self):
        return self.__price

    def setPrice(self, price):
        self.__price = price

    def __repr__(self):
        return f'id: {self.__id}, name: {self.__name}, code: {self.__code}, price: {self.__price}'
    
    def to_dict(self):
        return {
            "id": self.__id,
            "name": self.__name,
            "code": self.__code,
            "price": self.__price
        }