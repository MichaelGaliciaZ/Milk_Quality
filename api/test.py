import requests

new_data={
    'pH':5,
    'Temp':35,
    'Taste':41,
    'Odor':14,
    'Fat':1,
    'Turbidity':1.5,
    'Colour':200
}

response=requests.post('http://127.0.0.1:8000/predict',json=new_data)
print(response.content)

