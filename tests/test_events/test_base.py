from unittest import TestCase
from fastapi.testclient import TestClient
from recognition_serv.app.application import create_application


class TestBaseEventHandler(TestCase):
    def test_startup_handler(self):
        app = create_application()
        with self.assertLogs('recognition_serv', level='INFO') as cm:

            with TestClient(app):
                pass
            self.assertEqual(cm.output,
                             ['INFO:recognition_serv:Starting up ...',
                              'INFO:recognition_serv:Shutting down ...'])
