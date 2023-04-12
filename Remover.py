import requests
import json

webhook_url = input("Enter the webhook URL to delete: ")
field_name = input("Enter the field name: ")
field_value = input("Enter the field value: ")
message_title = input("Enter the message title: ")
message_desc = input("Enter the message description: ")

message_embed = {
    "title": message_title,
    "description": message_desc,
    "color": 16711680, 
    "fields": [
        {
            "name": field_name,
            "value": field_value
        }
    ]
}

data = {
    "embeds": [message_embed]
}
response = requests.post(webhook_url, json=data)

if response.ok:
    print(f"Message sent to webhook {webhook_url} before deleting!")
else:
    print(f"Error sending message to webhook {webhook_url}: {response.status_code} {response.text}")

response = requests.delete(webhook_url)

if response.ok:
    print(f"Webhook {webhook_url} deleted successfully!")
else:
    print(f"Error deleting webhook {webhook_url}: {response.status_code} {response.text}")
