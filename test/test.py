import requests 

# https://keras-flask.herokuapp.com/predict
resp = requests.post("https://keras-flask.herokuapp.com/predict", files={'file': open('eight.png', 'rb')})

print(resp.text)
