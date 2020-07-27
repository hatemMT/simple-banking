import json
import random
import unittest

from flaskr import create_app
from flaskr.models import setup_db, db, Category

DATABASE_HOST = '192.168.99.100'
DATABASE_PORT = '5432'
DATABASE_NAME = "db_test"
DATABASE_USER_PASSWORD = "admin:secret"

HOST = 'http://localhost:5000'


class AppTestCase(unittest.TestCase):
    """This class represents the trivia endpoint's tests"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.database_path = f"postgresql://{DATABASE_USER_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
        setup_db(self.app, self.database_path)
        self.db = db
        self.db.create_all()  # Create the schema
        self.client = self.app.test_client()  # initialize the http client

    def tearDown(self):
        self.db.drop_all()  # Drop the schema

    
    

    

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
