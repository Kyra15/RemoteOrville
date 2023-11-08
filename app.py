from flask import Flask, render_template, request
from main import Tank

tank = Tank()
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form.get('stop') == 'Stop':
            tank.stop()
        elif request.form.get('forward') == 'Forward':
            tank.forward()
        elif request.form.get('left') == "Left":
            tank.leftturn()
        elif request.form.get('right') == "Right":
            tank.rightturn()
        elif request.form.get('backward') == "Backward":
            tank.backward()
        else:
            tank.stop()
    elif request.method == 'GET':
        return render_template('index.html')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, address="192.168.1.42", port=4200)
