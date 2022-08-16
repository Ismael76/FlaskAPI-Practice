from flask import Flask, request, jsonify
from flask_cors import CORS
from controllers import cars


app = Flask(__name__)
CORS(app)

@app.route('/')
def welcome():
    return "Welcome to Cars API!"

@app.route('/cars', methods=['GET', 'POST'])
def car_list():
    fns = {
        'GET': cars.index,
        'POST': cars.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

@app.route('/cars/<int:car_id>', methods=['GET', 'DELETE', 'PUT'])
def cat_handler(car_id):
    fns = {
        'GET': cars.show,
        'DELETE': cars.destroy,
        'PUT': cars.update
    }
    resp, code = fns[request.method](request, car_id)
    return jsonify(resp), code


if __name__ == '__main__':
    app.run(debug=True)
