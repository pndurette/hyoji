import os
import unittest
import tempfile

from hyoji import app
from hyoji import models

class HyojiTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, self.db_path = tempfile.mkstemp()
        app.config['DATABASE'] = 'sqliteext:///%s' % self.db_path
        app.config['TESTING'] = True
        self.app = app.test_client()
        models.init_db()

        #flaskr.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(self.db_path)

    def test_empty_db(self):
        rv = self.app.get('/api/urls')
        print app.config['DATABASE']
        print rv.data
        print app.config
        #assert 'No entries here so far' in rv.data

if __name__ == '__main__':
    unittest.main()

