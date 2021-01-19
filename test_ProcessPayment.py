# test_ProcessPayment

import unittest
import json
import datetime

from app import create_app
from app.logic import *


class ProcessPaymentTestCase(unittest.TestCase):

    def setUp(self):

        self.app = create_app('testing')
        self.client = self.app.test_client
        self.data = {
                        "CreditCardNumber":"4539148803436467",
                        "CardHolder":"Test Card",
                        "ExpirationDate": "2022-03-23T21:12:32.425",
                        "SecurityCode":"",
                        "Amount":20.48
                    }
    def test_wrong_ccn(self):
        data = self.data
        data["CreditCardNumber"] = "INVALID400"
        res = self.client().post('/ProcessPayment', json=data, content_type='application/json')
        self.assertEqual(res.status_code, 400)

    def test_invaild_expiry(self):
        data = self.data
        data["ExpirationDate"] = "2012-12-23T19:24:54.531"
        res = self.client().post('/ProcessPayment', json=data)
        self.assertEqual(res.status_code, 400)
    
    def test_invalid_amount(self):
        data = self.data
        data["Amount"] = -24
        res = self.client().post('/ProcessPayment', json=data)
        self.assertEqual(res.status_code, 400)

    def test_missing_fields(self):
        data = {"Amount": 50}
        res = self.client().post('/ProcessPayment', json=data)
        self.assertEqual(res.status_code, 400)

    def test_valid_input(self):
        data = self.data
        data["test"] = True
        res = self.client().post('/ProcessPayment', json=data)
        self.assertEqual(res.status_code, 200)

    def test_low_amount_false(self):
        data = self.data
        data["Amount"] = 12.56
        res = self.client().post('/ProcessPayment', json=data)
        self.assertEqual(res.status_code, 500)
    
    def test_low_amount_true(self):
        data = self.data
        data["Amount"] = 12.56
        data["test"] = True
        res = self.client().post('/ProcessPayment', json=data)
        self.assertEqual(res.status_code, 200)
    
    def test_med_amount_false(self):
        data = self.data
        data["Amount"] = 204.52
        res = self.client().post('/ProcessPayment', json=data)
        self.assertEqual(res.status_code, 500)
    
    def test_med_amount_true(self):
        data = self.data
        data["Amount"] = 204.52
        data["test"] = True
        res = self.client().post('/ProcessPayment', json=data)
        self.assertEqual(res.status_code, 200)

    def test_high_amount_false(self):
        data = self.data
        data["Amount"] = 1242.76
        res = self.client().post('/ProcessPayment', json=data)
        self.assertEqual(res.status_code, 500)
    
    def test_high_amount_true(self):
        data = self.data
        data["Amount"] = 1242.76
        data["test"] = True
        res = self.client().post('/ProcessPayment', json=data)
        self.assertEqual(res.status_code, 200)


if __name__ == "__main__":
    unittest.main()