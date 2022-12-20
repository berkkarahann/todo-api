from src import create_app
import os
from dotenv import load_dotenv

# loading environment variables from the .env file if exists
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# entry point for launching the flask app
app = create_app("production")
