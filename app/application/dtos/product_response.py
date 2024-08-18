class ProductResponse():
    def __init__(self, name=None, code=None, price=None):
        self.__name = name
        self.__code = code
        self.__price = price

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
        return f"name: {self.__name}, code: {self.__code}, price: {self.__price}"
    
    def to_dict(self):
        return {
            "name": self.__name,
            "code": self.__code,
            "price": self.__price
        }