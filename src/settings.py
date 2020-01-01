import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path('..') / '.env'
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
WEATHER_API_URL = os.getenv('WEATHER_API_URL')
X_RAPIDAPI_HOST = os.getenv('X_RAPIDAPI_HOST')
X_RAPIDAPI_KEY = os.getenv('X_RAPIDAPI_KEY')

if __name__ == '__main__':
    print(TOKEN)
