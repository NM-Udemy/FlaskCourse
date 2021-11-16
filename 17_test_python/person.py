# person.py
import unittest
import requests
from unittest.mock import patch

class Person:

    tax_rate = 0.7

    def __init__(self, first_name, last_name, gross_income):
        self.first_name = first_name
        self.last_name = last_name
        self.gross_income = gross_income
    
    @property
    def email(self):
        return f'{self.first_name}_{self.last_name}@mail.com'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    @property
    def net_income(self):
        return int(self.gross_income * self.tax_rate)

    def compricated_method(self, text):
        pass

    def call_api(self, month):
        response = requests.get(f'https://www.api.com/{self.last_name}/{month}')
        if response.ok:
            return self.compricated_method(response.text)
            # return response.text
        else:
            return 'Request Error'

class TestPerson(unittest.TestCase):

    # テストの前に毎回呼ばれる
    def setUp(self):
        self.person = Person('Taro', 'Yamada', 100000)

    def tearDown(self):
        # テストの後に毎回呼ばれる
        print('tearDown called \n')

    @classmethod
    def setUpClass(cls):
        cls.answer_email = ['Taro_Yamada@mail.com', 'Taro_Tanaka@mail.com']
    
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass called \n')

    def test_email(self):
        # person = Person('Taro', 'Yamada', 100000)
        self.assertEqual(self.person.email, self.answer_email[0])
        self.person.last_name = 'Tanaka'
        self.assertEqual(self.person.email, self.answer_email[1])
    
    def test_full_name(self):
        # person = Person('Taro', 'Yamada', 100000)
        self.assertEqual(self.person.full_name, 'Taro Yamada')
        self.person.first_name = 'Jiro'
        self.assertEqual(self.person.full_name, 'Jiro Yamada')
    
    def test_net_income(self):
        # person = Person('Taro', 'Yamada', 100000)
        self.assertEqual(self.person.net_income, 70000)

    # def test_call_api(self):
    #     with patch('__main__.requests.get') as mocked_get:
    #         mocked_get.return_value.ok = True
    #         mocked_get.return_value.text = 'Success'
    #         caller = self.person.call_api('May')
    #         mocked_get.assert_called_with('https://www.api.com/Yamada/May')
    #         self.assertEqual(caller, 'Success')
    #         self.assertEqual(mocked_get.call_count, 1)

    #         mocked_get.reset_mock()
    #         mocked_get.return_value.ok = False
    #         caller = self.person.call_api('June')
    #         mocked_get.assert_called_with('https://www.api.com/Yamada/June')
    #         self.assertEqual(caller, 'Request Error')
    @patch('__main__.Person.compricated_method')
    @patch('__main__.requests.get')
    def test_call_api(self, mocked_get, mocked_method):
        mocked_get.return_value.ok = True
        mocked_get.return_value.text = 'Success'
        mocked_method.return_value = mocked_get.return_value.text + ' Method'
        caller = self.person.call_api('May')
        mocked_get.assert_called_with('https://www.api.com/Yamada/May')
        mocked_method.assert_called_with('Success')
        self.assertEqual(caller, 'Success Method')

        mocked_get.reset_mock()
        mocked_method.reset_mock()
        mocked_get.return_value.ok = False

        caller = self.person.call_api('June')
        mocked_get.assert_called_with('https://www.api.com/Yamada/June')
        mocked_method.assert_not_called()
        self.assertEqual(caller, 'Request Error')


if __name__ == '__main__':
    unittest.main()