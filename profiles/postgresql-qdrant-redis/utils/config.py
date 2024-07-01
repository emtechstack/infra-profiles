from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = f"postgresql+asyncpg://{os.getenv('POSTGRE__DATABASE_USERNAME')}:{os.getenv('POSTGRE__DATABASE_PASSWORD')}@{os.getenv('POSTGRE__DATABASE_HOST')}/{os.getenv('POSTGRE__DATABASE_NAME')}"
