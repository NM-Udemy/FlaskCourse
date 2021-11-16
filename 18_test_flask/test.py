from flask_testing import TestCase
from flaskr import create_app, db
from flask import url_for
from flaskr.models import User
import os
import unittest
from flask_login import current_user


app = create_app()

class TestConfig:
    TESTING = True
    WTF_CSRF_ENABLED = False
    basedir = os.path.abspath(os.path.dirname(__name__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
        

class MyTest(TestCase):

    def create_app(self):
        # app.config['TESTING'] = True
        # app.config['WTF_CSRF_ENABLED'] = False
        # basedir = os.path.abspath(os.path.dirname(__name__))
        # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        app.config.from_object('test.TestConfig') # 設定を読み込む
        return app
    
    def setUp(self): # 各テスト毎に呼ばれる
        db.create_all() # テーブル全作成
    
    def tearDown(self): # 各テスト毎に呼ばれる
        db.session.remove() # セッション削除
        db.drop_all() # テーブル全削除

    def test_register(self):
        with self.client as client:
            self.assertEqual(User.query.count(), 0)
            response = client.post(url_for('app.register'),
                data = {
                    'username': 'test',
                    'email': 'test@mail.com',
                    'password': 'password',
                    'password_confirm': 'password',
                }
            )
            self.assertEqual(User.query.count(), 1)
            self.assertEqual(User.query.all()[-1:][0].username, 'test')
            self.assert_status(response, 302) # ステータスコード(redirectの場合302)
            self.assert_redirects(response, url_for('app.login')) # リダイレクト先の確認

    def test_register_error(self):
        with self.client as client:
            self.assertEqual(User.query.count(), 0)
            response = client.post(url_for('app.register'),
                data = {
                    'username': 'test',
                    'email': 'test@mail.com',
                    'password': 'passwor',
                    'password_confirm': 'password',
                }
            )
            self.assertEqual(User.query.count(), 0)
            self.assert_status(response, 200)

    def test_register_error2(self):
        with self.client as client:
            self.assertEqual(User.query.count(), 0)
            response = client.post(url_for('app.register'),
                data = {
                    'username': 'test',
                    'email': 'test@mail.com',
                    'password': 'password',
                    'password_confirm': 'password',
                }
            )
            self.assertEqual(User.query.count(), 1)
            response = client.post(url_for('app.register'),
                data = {
                    'username': 'test',
                    'email': 'test@mail.com',
                    'password': 'password',
                    'password_confirm': 'password',
                }
            )
            self.assertEqual(User.query.count(), 1)
            

    def test_login(self):
        with self.client as client:
            response = client.post(url_for('app.register'),
                data = {
                    'username': 'test',
                    'email': 'test@mail.com',
                    'password': 'password',
                    'password_confirm': 'password',
                }
            )
            self.assertTrue(current_user.is_anonymous)
            response = client.post(url_for('app.login'),
                data = {
                    'email': 'test@mail.com',
                    'password': 'password',
                }
            )
            self.assert_status(response, 302)
            self.assert_redirects(response, url_for('app.welcome'))
            self.assertEqual(current_user.username, 'test')

    def test_logout(self):
        with self.client as client:
            response = client.post(url_for('app.register'),
                data = {
                    'username': 'test',
                    'email': 'test@mail.com',
                    'password': 'password',
                    'password_confirm': 'password',
                }
            )
            response = client.post(url_for('app.login'),
                data = {
                    'email': 'test@mail.com',
                    'password': 'password',
                }
            )
            response = client.get(url_for('app.logout'))
            self.assertTrue(current_user.is_anonymous)


if __name__ == '__main__':
    unittest.main()
