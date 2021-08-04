from flask import Flask
import unittest

app = Flask(__name__)

from api.auth import bp_auth
app.register_blueprint(bp_auth, url_prefix='')

class BluePrintTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_health(self):
        rv = self.app.get('/api/auth')
        print rv.data


if __name__ == '__main__':
    unittest.main()