import requests


def test_status_endpoint():
    res = requests.get("http://localhost:5000/api/status")
    assert res.status_code == 200
    assert res.json()["status"] == "OK"
