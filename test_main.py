
import requests

BASE_URL = "http://127.0.0.1:8000"

r = requests.post(f"{BASE_URL}/items/", json={"item_name": "Test Item", "description": "A test item"})
print(r.json())
