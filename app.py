from flask import Flask, request, jsonify
from flask_cors import CORS
from controllers import cars
from waitress import serve
from werkzeug import exceptions
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import sqlite3
from models import vehicles

app = Flask(__name__)
CORS(app)

# app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///cars.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# db = SQLAlchemy(app)

# Function That Creates A Connection To Our DB


def get_db_connection():
    conn = sqlite3.connect('cars.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def welcome():
    try:
        # db.session.query(text('1')).from_statement(text('SELECT 1')).all()
        return "Welcome to Cars API!"
    except Exception as e:
        error_text = "<p>The Error:<br>" + str(e) + "</p>"
        hed = '<h1>Database Is Not Working!</h1>'
        return hed + error_text


@app.route('/cars', methods=['GET', 'POST'])
def car_list():
    # fns = {
    #     'GET': Vehicles.query.all,
    #     'POST': cars.create
    # }

    if request.method == 'GET':
        # Connecting To DB By Calling The Function That Creates A Connection To DB
        conn = get_db_connection()
        # Retrieving All Data Using SQL Query, fetchall() Returns All Rows
        allCars = conn.execute('SELECT * FROM vehicles').fetchall()
        # We Need To Convert Each Row Into A Tuple So It Can Be Iterated Over, We Store This Inside A List
        results = [tuple(row) for row in allCars]
        conn.close()
        # We Return The Results List In JSON Format
        return jsonify(results)

    if request.method == 'POST':
        # We Use request.get_json() To Get JSON Response In The POST REQUEST
        car_to_add = request.get_json()
        # car_to_add['manufacturer'] This Will Return The Value In The JSON Body That Has The Key 'manufacturer' etc.
        # We Call Our Model & Access It's Create Method That Creates A New Entry To Our Vehicles Table In DB.
        new_car = vehicles.Vehicles.create(
            car_to_add['manufacturer'], car_to_add['model'])
        return "Added Car!"

    # resp, code = fns[request.method](request)
    # return jsonify(resp), code


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
    app.run(debug=True)
    # serve(app, host='0.0.0.0', port=8080, url_scheme='https')
    # Waitress to deploy on heroku!
