# import all necessary libraries
from flask import Flask, render_template, request
from tankClass import Tank
from datetime import date
import pickle
import time

# create the tank object
tank = Tank()

# create the flask server
app = Flask(__name__)

# initialize a global variable with today's date formatted correctly
today = date.today().strftime("%B %d, %y")

# define a function that will load the information from a pickle file to a dictionary
def pickleload(file): 
    f.open(file, "rb")
    returndict = pickle.load(f)
    f.close()
    return returndict

# define a function that will write a dictionary to a pickle file
def picklewrite(file, dictio):
    f.open(file, "wb")
    pickle.dump(dictio, f)
    f.close()

# this is the main page, which will first load the logdict pickle file to a dictionary and then create a key with today's date
@app.route('/')
def default():
    logdict = pickleload("logdict.pkl")
    logdict[today] = None
    return render_template('index.html')
    
# this is the endpoint for the API, it gets a json file of the data from the html page and sets all the data from the 'button' key to a variable
# then, it checks what that button data is, calls the appropriate function, and adds that movement to the log dictionary
@app.route('/moving', methods=['POST'])
def home():
    data = request.json
    pressed = data.get('button')
    if pressed == "forward" or pressed == "go":
        tank.forward()
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


# runs the program and API server
if __name__ == '__main__':
    app.run(debug=True, host=0.0.0.0, port=4200)
