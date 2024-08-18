from flask import Blueprint, request, jsonify
import json

from app.application.handlers.product_handler_implementation import ProductHandlerImplementation
from app.application.mappers.i_product_request_mapper import ProductRequestMapper
from app.application.mappers.i_product_response_mapper import ProductResponseMapper
from app.domain.useCases.product_use_case import ProductUseCase
from app.infraestructure.outputs.sqllite.adapters.product_adapter import ProductAdapter
from app.infraestructure.outputs.sqllite.mappers.i_product_entity_mapper import IProductEntityMapper
from app.infraestructure.outputs.sqllite.repositories.i_product_repository import IProductRepository

productRoute = Blueprint('product', __name__, url_prefix='/product')

productRepository = IProductRepository(IProductEntityMapper)
productPersistencePortImplementation = ProductAdapter(productRepository)
productServicePortImplementation = ProductUseCase(productPersistencePortImplementation)

iProductHandler = ProductHandlerImplementation(
    iProductServicePort=productServicePortImplementation,
    productRequestMapper=ProductRequestMapper,
    productResponseMapper=ProductResponseMapper
)

@productRoute.route("/getAll", methods=["GET"])
def getAll():
    return jsonify(iProductHandler.getAll()), 200

@productRoute.route("/create", methods=["GET", "POST"])
def create():
    productData = json.loads(request.data)
    return jsonify(iProductHandler.create(productData=productData)), 201

@productRoute.route("/getById/<string:id>", methods=["GET"])
def getById(id):
    return jsonify(iProductHandler.getById(id=id)), 200

@productRoute.route("/updateById/<string:id>", methods=["PUT", "GET"])
def updateById(id):
    productData = json.loads(request.data)
    return jsonify(iProductHandler.updateById(id=id, productData=productData)), 200

@productRoute.route("/deleteById/<string:id>", methods=["DELETE", "GET"])
def deleteById(id):
    return jsonify(iProductHandler.deleteById(id=id)), 200