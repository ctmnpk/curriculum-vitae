# Libraries importing
from decouple import config 
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# Credentials
MONGODB_USER = config("MONGODB_USER")
MONGODB_PASSWORD = config("MONGODB_PASSWORD")
MONGODB_CLUSTER = config("MONGODB_CLUSTER")

class AtlasConnection:
    """
    This class handle the database connection.   
    """
    def __init__(self): 
        self.user = MONGODB_USER
        self.password = MONGODB_PASSWORD
        self.cluster = MONGODB_CLUSTER
        self.uri = f"mongodb+srv://{self.user}:{self.password}@{self.cluster}"

    def test_connection(self):
        """
        This function does the test connection with database by using ping command.
        """
        client = self.client_setup()
        try: 
            client.admin.command("ping")
            print("Succesfully connected to cloud database")
        except ConnectionFailure as err:
            print(f"An error happens while trying connection: {err}")
        finally:
            client.close()
            print("Closing connection...")

    def client_setup(self):
        """
        This function does the client initialization then returns it.
        """
        client = MongoClient(self.uri)
        return client
