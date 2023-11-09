from flask import Flask, render_template, request
from tankClass import Tank
import time

tank = Tank()
app = Flask(__name__)

@app.route('/')
def default():
    return render_template('index.html')
    

@app.route('/moving', methods=['POST'])
def home():
    button = request.json
    if button.get('button') == "forward":
        tank.forward()
    if button.get('button') == "go":
        tank.forward()
    elif button.get('button') == "stop":
        tank.stop()
    elif button.get('button') == "left":
        tank.leftturn()
    elif button.get('button') == "right":
        tank.rightturn()
    elif button.get('button') == "backward":
        tank.backward()
    else:
        tank.stop()
    return "Moved"


if __name__ == '__main__':
    app.run(debug=True, host=0.0.0.0, port=4200)
