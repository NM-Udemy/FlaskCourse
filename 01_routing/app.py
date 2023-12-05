from flask import Flask

app = Flask(__name__) # __main__


@app.route('/')
def index():
    """ ルートURLへのアクセス """
    return '<h1>Hello World</h1>'

@app.route('/hello')
@app.route('/hello2')
def hello():
    """ /hello, /hello2に対応  """
    return '<h1>hello</h1>'

posts = {
    1: "POST1",
    2: "POST2",
}

@app.route('/post/<int:post_id>/<post_name>')
def show_post(post_id, post_name):
    """ 特定の投稿を表示 post_id: 整数値 """
    # if post_id not in posts:
    #     return f'{post_id}が存在しません'
    post = posts[post_id]
    return f"{post_id}: {post_name}"

@app.route('/user/<string:user_name>/<int:user_number>/<path:user_path>')
def show_user(user_name, user_number, user_path):
    user_name_number = f"{user_name}: {user_number}({user_path})"
    return f"<h1>{user_name_number}</h1>"
    
if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=80)
    app.run(debug=True)
