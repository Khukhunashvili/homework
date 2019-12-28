from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/divisor', methods=["post"])
def display_divisor():
    value = request.form['number']
    return render_template('divisor.html', value=value, min_divisor=get_min_divisor(value))

def get_min_divisor(num):
    num = int(num)
    min_divisor = num

    for i in range(num//2, 1, -1):
        if num%i == 0:
            min_divisor = i
    return min_divisor

if __name__ == '__main__':
    app.run()
