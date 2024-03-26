import requests

def get_subscriber_by_phone(phone_number, api_key):
    url = f"https://backend.botconversa.com.br/api/v1/webhook/subscriber/get_by_phone/{phone_number}/"
    headers = {
        "accept": "application/json",
        "API-KEY": api_key
    }
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else None

def create_subscriber(phone_number, first_name, last_name, api_key):
    url = "https://backend.botconversa.com.br/api/v1/webhook/subscriber/"
    headers = {
        "accept": "application/json",
        "API-KEY": api_key,
        "Content-Type": "application/json"
    }
    data = {
        "phone": phone_number,
        "first_name": first_name,
        "last_name": last_name
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json() if response.status_code == 200 else None

def send_message_to_subscriber(subscriber_id, message_type, message_value, api_key):
    url = f"https://backend.botconversa.com.br/api/v1/webhook/subscriber/{subscriber_id}/send_message/"
    headers = {
        "accept": "application/json",
        "API-KEY": api_key,
        "Content-Type": "application/json"
    }
    data = {
        "type": message_type,
        "value": message_value
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json() if response.status_code == 200 else None
