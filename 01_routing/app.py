from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

@app.route('/hello')
@app.route('/something')
def hello():
    return '<h2>my hello</h2>'

@app.route('/post/<int:post_id>/<post_name>')
def show_post(post_id, post_name):
    # print(type(post_id))
    return '{}: {}'.format(post_name, post_id)

@app.route('/user/<string:user_name>/<int:user_no>')
def show_user(user_name, user_no):
    user_name_no = user_name + str(user_no)
    return '<h1>{}</h1>'.format(user_name_no)

if __name__ == '__main__':
    app.run()
