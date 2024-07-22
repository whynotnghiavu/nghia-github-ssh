import os
# pip install python-dotenv
from dotenv import load_dotenv

FILE_ENV = "../env/host.env"
FILE_ENV = "../env/localhost.env"
FILE_ENV = "../env/.env"


load_dotenv(FILE_ENV)

SSH_PASSWORD = os.getenv("SSH_PASSWORD")
print(f"🚀 {SSH_PASSWORD}")
