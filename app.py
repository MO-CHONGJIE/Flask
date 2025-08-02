from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Hello World!</h1>"


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"<h2>Hello {name}</h2>"

@app.route('/convert/<celsius>')# covert temperature
def convert(celsius):
    try:
        c = float(celsius)
        f = c * 9.0 / 5 + 32
        return f"<p>{c}°C = {f:.1f}°F</p>"
    except ValueError:
        return "<p>Invalid number!</p>"


if __name__ == '__main__':
    app.run(debug=True)
