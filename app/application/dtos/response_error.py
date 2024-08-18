class ResponseError():
    def __init__(self, status=None, statusCode=None, message=None):
        self.__status = status
        self.__statusCode = statusCode
        self.__message = message
        
    def to_dict(self):
        return {
            "status": self.__status,
            "statusCode": self.__statusCode,
            "message": self.__message
        }