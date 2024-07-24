import requests

# Train endpoint
train_response = requests.post('http://127.0.0.1:5000/train')
print(train_response.json())
# New 