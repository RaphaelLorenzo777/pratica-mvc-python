import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
from os import getenv

class Database:
    def __init__(self):
        load_dotenv()
        self.host = getenv( 'DB_HOST' )
        self.username = getenv( 'DB_USER' )
        self.password = getenv( 'DB_PSWD' )
        self.database = getenv( 'DB_NAME' )
        self.connection = None
        self.cursor = None

    def conectar(self):
        """Estabelece uma conexão com o banco de dados."""
        try:
            self.connectionn = mysql.connector.connect(
                host = self.host,
                database = self.database, 
            )