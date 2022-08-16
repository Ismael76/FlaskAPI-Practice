from flask import Flask, request, jsonify
from flask_cors import CORS
from controllers import cars
from waitress import serve
from werkzeug import exceptions


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
def car_handler(car_id):
    fns = {
        'GET': cars.show,
        'DELETE': cars.destroy,
        'PUT': cars.update
    }
    resp, code = fns[request.method](request, car_id)
    return jsonify(resp), code


@app.errorhandler(exceptions.NotFound)
def error_404(err):
    return {'message': f'Page Not Found {err}'}, 404


if __name__ == '__main__':
    # app.run(debug=True)
    serve(app, host='0.0.0.0', port=8080, url_scheme='https')

    # Waitress to deploy on heroku!
