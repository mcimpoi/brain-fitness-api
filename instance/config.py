# The instance folder is located outside the package and can hold local data that shouldn’t be
# committed to version control, such as configuration secrets and the database file.
# TODO: put this in gitignore?
# instance/config.py

TEST_DATABASE = ""
PROD_DATABASE = ""
SECRET_KEY = ""
API_KEY = ""
URL = ""
DEBUG = True  # Turns on debugging features in Flask
