import pytest
import app
from controllers import cars

@pytest.fixture
def api(monkeypatch):
    test_cars = [
        {'id': 1, 'manufacturer': 'Lamborghini', 'model': "Aventador"},
        {'id': 2, 'manufacturer': 'Audi', 'model': "RS6"},
        {'id': 3, 'manufacturer': 'Ferrari', 'model': "Enzo"},
        {'id': 4, 'manufacturer': 'Porsche', 'model': "911 Turbo"},
        {'id': 5, 'manufacturer': 'Vauxhall', 'model': "Corsa"},
        {'id': 6, 'manufacturer': 'BMW', 'model': "M3"}
    ]
    monkeypatch.setattr(cars, "cars", test_cars)
    api = app.app.test_client()
    return api
