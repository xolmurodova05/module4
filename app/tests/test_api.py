import requests

def test_predict_all():
    r = requests.get("http://localhost:5000/predict?country=ALL")
    assert r.status_code == 200

def test_predict_country():
    r = requests.get("http://localhost:5000/predict?country=USA")
    assert r.status_code == 200