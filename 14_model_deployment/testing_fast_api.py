import requests

#url="http://127.0.0.1:8000/predict"
url = "http://127.0.0.1:4444/predict"
# data={"features":[5.1,3.5,1.4,0.2]}
data={"features":[6.1,6.5,3.4,5.2]}

response=requests.post(url,json=data)
print(response.json())
