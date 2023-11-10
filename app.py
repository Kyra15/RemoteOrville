from flask import Flask, render_template, request
from tankClass import Tank
from datetime import date
import pickle
import time

tank = Tank()
app = Flask(__name__)
today = date.today().strftime("%B %d, %y")

def pickleload(file): 
    f.open(file, "rb")
    returndict = pickle.load(f)
    f.close()
    return returndict

def picklewrite(file, dictio):
    f.open(file, "wb")
    pickle.dump(dictio, f)
    f.close()

@app.route('/')
def default():
    logdict = pickleload("logdict.pkl")
    logdict[today] = None
    return render_template('index.html')
    

@app.route('/moving', methods=['POST'])
def home():
    data = request.json
    pressed = data.get('button')
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
    return "Movement Successful"

@app.route('/login', methods=['GET', 'POST']
def loginpage():
    data = request.json
    user = data.get('username')
    psswd = data.get('password')
    return "Login Successful"

if __name__ == '__main__':
    app.run(debug=True, host=0.0.0.0, port=4200)
