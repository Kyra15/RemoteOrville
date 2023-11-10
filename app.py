from flask import Flask, render_template, request
from tankClass import Tank
from datetime import date
import time

tank = Tank()
app = Flask(__name__)
date = date.today().strftime("%B %d, %y")

logdict = {}

f.open

@app.route('/')
def default():
    return render_template('index.html')
    

@app.route('/moving', methods=['POST'])
def home():
    button = request.json
    pressed = button.get('button')
    if pressed == "forward" or pressed == "go":
        tank.forward()
        logdict.append(pressed)
    elif pressed == "stop":
        tank.stop()
    elif pressed == "left":
        tank.leftturn()
    elif pressed == "right":
        tank.rightturn()
    elif pressed == "backward":
        tank.backward()
    else:
        tank.stop()
    return "Moved"


if __name__ == '__main__':
    app.run(debug=True, host=0.0.0.0, port=4200)
