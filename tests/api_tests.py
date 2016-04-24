import os
import unittest
import tempfile
import json

from hyoji import app
from hyoji import models

class HyojiTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, self.db_path = tempfile.mkstemp()
        app.config['DATABASE'] = 'sqliteext:///%s' % self.db_path
        app.config['TESTING'] = True
        self.app = app.test_client()
        models.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(self.db_path)

    def test_empty_urls(self):
        rv = self.app.get('/api/urls')
        resp = json.loads(rv.data)
        # {"status": "success", "data": {"urls": []}}
        self.assertEqual(resp['status'],       'success')
        self.assertEqual(resp['data']['urls'], [])

    def test_post_url(self):
        rv = self.app.post('/api/url', data=dict(
        title='<Hello>',
        text='<strong>HTML</strong> allowed here'
    ), follow_redirects=True)

if __name__ == '__main__':
    unittest.main()

