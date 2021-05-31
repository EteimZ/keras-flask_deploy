# keras-flask_deploy

REST API to recognise hand written digits built with keras & flask hosted on heroku.

## Usage

Make a post request to **https://keras-flask.herokuapp.com/predict** sending an image of the number you wish to predict. 

### Example using python.

```python
import requests 

resp = requests.post("https://keras-flask.herokuapp.com/predict", files={'file': open('eight.png', 'rb')})

print(resp.text)
```

## Resource

[Tutorial by Python Engineer](https://youtu.be/bA7-DEtYCNM)
