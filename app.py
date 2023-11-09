from flask import Flask, render_template, request
from tankClass import Tank
import time

tank = Tank()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    n = 0
    while n < 2:
        time.sleep(0.5)
        if request.method == 'GET':
            if request.args.get('button') == "forward":
                tank.forward()
            if request.args.get('button') == "go":
                tank.forward()
                n -= 1
            elif request.args.get('button') == "stop":
                tank.stop()
                n += 1
            elif request.args.get('button') == "left":
                tank.leftturn()
            elif request.args.get('button') == "right":
                tank.rightturn()
            else:
                tank.stop()
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, address="192.168.1.42", port=4200)
