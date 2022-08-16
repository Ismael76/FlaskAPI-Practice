from http.client import BAD_REQUEST

cars = [
    {'id': 1, 'manufacturer': 'Lamborghini', 'model': "Aventador"},
    {'id': 2, 'manufacturer': 'Audi', 'model': "RS6"},
    {'id': 3, 'manufacturer': 'Ferrari', 'model': "Enzo"},
    {'id': 4, 'manufacturer': 'Porsche', 'model': "911 Turbo"},
    {'id': 5, 'manufacturer': 'Vauxhall', 'model': "Corsa"},
    {'id': 6, 'manufacturer': 'BMW', 'model': "M3"}
]

def index(req):
    return [car for car in cars], 200

def create(req):
    new_car = req.get_json()
    new_car['id'] = sorted([c['id'] for c in cars])[-1] + 1
    cars.append(new_car)
    return new_car, 201

def show(req, uid):
    return find_by_uid(uid), 200

def destroy(req, uid):
    car = find_by_uid(uid)
    cars.remove(car)
    return car, 204

def update(req, uid):
    car = find_by_uid(uid)
    data = req.get_json()
    print(data)
    for key, value in data.items():
        car[key] = value
    return car, 200

def find_by_uid(uid):
    try:
        return next(c for c in cars if c['id'] == uid)
    except:
        raise BAD_REQUEST(f"We don't have a car with {uid}!")
