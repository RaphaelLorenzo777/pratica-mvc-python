import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
from os import getenv

class Database:
    def __init__(self):
        load_dotenv()
        self.host =