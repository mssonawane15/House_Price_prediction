from flask import Flask,json,render_template,request,jsonify
from Project_Data.utils import HousePricePredictor

app = Flask(__name__)

@app.route("/")
def func():
    print("hello World")
    return "hello world"


@app.route("/predict")
def get_price():
    data=request.form
    size = eval(data["size"])
    sqft = eval(data["sqft"])
    bath = eval(data["bath"])
    balcony = eval(data["balcony"])
    location = data["location"]

    price_predictor = HousePricePredictor(size,sqft,bath,balcony,location)
    price = price_predictor.get_house_price()

    return jsonify({"Result":f" House Price is {price}"})

app.run()

