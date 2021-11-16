from flask import Flask, render_template, redirect, url_for, g, request
import logging
import time

app = Flask(__name__)

class UserInfo:

    def __init__(self, number, name, age, gender, major, picture_path):
        self.number = number
        self.name = name
        self.age = age
        self.gender = gender
        self.major = major
        self.picture_path = picture_path

member_list = [
    UserInfo(0, '太郎', 21, '男', '法学部', 'image/taro.jpg'),
    UserInfo(1, '次郎', 20, '男', '理学部', 'image/jiro.jpg'),
    UserInfo(2, '良子', 22, '女', '文学部', 'image/ryoko.jpg'),
    UserInfo(3, '花子', 21, '女', '工学部', 'image/hanako.jpg')    
]

@app.route('/') # メインページ
def main():
    app.logger.debug('メインページです')
    return render_template('main.html')

@app.route('/memberlist') # メンバー一覧ページ
def load_member_list():
    app.logger.debug('メイン一覧です')
    return render_template('member_list.html', member_list=member_list)

@app.route('/member/<int:member_number>') #　メンバー詳細ページ
def member_detail(member_number):
    app.logger.debug('メンバー詳細です')
    for member in member_list:
        if member.number == member_number:
            return render_template('member_detail.html', member=member)
    return redirect(url_for('main'))

@app.route('/terms') # 利用規約
def terms_of_service():
    app.logger.debug('利用規約です')
    return render_template('terms.html')

@app.errorhandler(404) # ページが間違うとmain
def redirect_main_page(error):
    app.logger.error('ページが誤っています')
    return redirect(url_for('main'))

@app.before_request
def before_request():
    g.start_time = time.time()
    app.logger.info(
        f'{request.remote_addr}, {request.method}, {request.url}, {request.data}'
    )

@app.after_request
def after_request(response):
    app.logger.info(
        f'{request.remote_addr}, {request.method}, {request.url}, {request.data}, {response.status}'
    )
    end_time = time.time()
    logging.getLogger('performance').info(
        f'{request.method}, {request.url}, exection time = {end_time - g.start_time}'
    )

    return response

if __name__ == '__main__':
    import logging.config
    import os
    basedir = os.path.abspath(os.path.dirname(__name__))
    log_config_path = os.path.join(basedir, 'config', 'logger.conf')
    logging.config.fileConfig(fname=log_config_path)
    app.run(debug=True)
