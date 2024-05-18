import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_TOKEN = os.getenv("SECRET_TOKEN")
BOT_PREFIX = os.getenv("BOT_PREFIX")

