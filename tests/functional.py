from flask import Flask
from TestApp.uni_devops_project_app import views
app = Flask(__name__)


def test_index_page():

    with app.test_client() as test_client:
        r = test_client.get('/')

        assert r.status_code == 200
        assert b"WELCOME" in r.data
