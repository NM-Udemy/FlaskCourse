from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return '<h1>こんにちは</h1>'

@app.route('/hello/<string:name1>/<string:name2>')
def show_name(name1, name2):
    return f'<h1>こんにちは{name1}さん{name2}さん</h1>'

@app.route('/add/<int:num1>/<int:num2>')
def add_number(num1, num2):
    num = num1 + num2
    return f'<h1>{num}</h1>'

@app.route('/div/<float:num_float1>/<float:num_float2>')
def div_float(num_float1, num_float2):
    num_float = num_float1 // num_float2
    return f'<h1>{num_float}</h1>'

if __name__ == '__main__':
    app.run(debug=True)
