import requests
import json

BASE_URL = "http://localhost:8000"

def pretty(data):
    print(json.dumps(data, indent=4))


def test_hello():
    print("\n🔹 Testing /api/hello")
    res = requests.get(f"{BASE_URL}/api/hello")
    pretty(res.json())


def test_chat():
    print("\n🔹 Testing /api/chat (Gemini)")
    payload = {
        "message": "What is the meaning of risk-free rate?",
        "provider": "gemini"
    }
    res = requests.post(f"{BASE_URL}/api/chat", json=payload)
    pretty(res.json())


def test_stock():
    print("\n🔹 Testing /api/stock/AAPL")
    res = requests.get(f"{BASE_URL}/api/stock/AAPL")
    pretty(res.json())


def test_interest_rate():
    print("\n🔹 Testing /api/interestRates")
    res = requests.get(f"{BASE_URL}/api/interestRates")
    pretty(res.json())


def test_predict():
    print("\n🔹 Testing /api/predict/AAPL")
    res = requests.get(f"{BASE_URL}/api/predict/AAPL")
    pretty(res.json())


def test_options():
    print("\n🔹 Testing /api/options/AAPL/2025-01-17")
    res = requests.get(f"{BASE_URL}/api/options/AAPL/2025-11-21")
    pretty(res.json())


def test_option_delta():
    print("\n🔹 Testing /api/options/getDelta")
    params = {
        "S": 100,
        "K": 110,
        "T": 0.25,
        "r": 0.05,
        "sigma": 0.33
    }
    res = requests.get(f"{BASE_URL}/api/options/getDelta/", params=params)
    pretty(res.json())


if __name__ == "__main__":
    print("\n🚀 Starting API Test Suite\n")

    test_hello()
    test_chat()
    test_stock()
    test_interest_rate()
    test_predict()
    # test_options()
    # test_option_delta()

    print("\n✨ All tests completed.\n")
