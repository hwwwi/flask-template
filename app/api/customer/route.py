""" API for customer """

from flask import Blueprint, jsonify, current_app
# from app.model import Customer

customer = Blueprint('customer', __name__)


@customer.route('/', methods=['GET'])
def get_customer_list():
    """[summary]

    Returns:
        [type] -- [description]
    """
    current_app.logger.info("Get customer info called!!!")

    return jsonify("Hello customers!!"), 200
