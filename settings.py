from dotenv import load_dotenv
import os

load_dotenv()

APPENDONLY_FILENAME = os.getenv("APPENDONLY_FILENAME", "data.txt")
