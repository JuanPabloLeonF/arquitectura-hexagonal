from app.infraestructure.outputs.sqllite.configurations.database_config import db
import uuid

class ProductEntity(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(80), unique=False, nullable=False)
    code = db.Column(db.String(120), unique=True, nullable=False)
    price = db.Column(db.Float, unique=False, nullable=False)
    
    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getCode(self):
        return self.code
    
    def getPrice(self):
        return self.price

    def __repr__(self):
        return f'id: {self.id}, name: {self.name}, code: {self.code}, price: {self.price}'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'price': self.price
        }