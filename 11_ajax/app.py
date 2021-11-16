from flask import Flask, jsonify, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# AJAXの処理を実行して結果をJSONで返す
@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify({'result': a + b})

if __name__ == '__main__':
    app.run(debug=True)
