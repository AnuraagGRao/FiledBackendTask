# app/__init__.py

from flask_api import FlaskAPI
from flask import request, jsonify

from app.logic import *
from instance.config import app_config

def create_app(config_name):
    """Creates the app instance in a particular config."""
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')


    @app.route('/ProcessPayment', methods=['POST'])
    def ProcessPayment():
        data = request.get_json()
        if not check_if_request_is_valid(data):
            return jsonify({"status":"The request is invalid!"}), 400
        
        if not check_if_args_are_vaild(data):
            return jsonify({"status":"The request is invalid!"}), 400
        
        if data["Amount"] < 20.99:
            res = useCheapPaymentGateway(data)
        elif data["Amount"] > 21.00 and data["Amount"] < 500.00:
            res = useExpensivePaymentGateway(data)
            if not res:
                res = useCheapPaymentGateway(data)
        else:
            res = usePremiumPaymentGateway(data)
            count = 0
            while not res and count < 3:
                count += 1
                res = usePremiumPaymentGateway(data)
        if not res:
            return jsonify({"status":"Payment could not be processed!"}), 500
        
        return jsonify({"status":"Payment has been processed!"}), 200

    return app

