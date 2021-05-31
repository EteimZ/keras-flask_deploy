#Test Script to make post request to the server
import requests 

resp = requests.post("https://keras-flask.herokuapp.com/predict", files={'file': open('eight.png', 'rb')})

print(resp.text)
