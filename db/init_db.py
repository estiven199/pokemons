import pymysql


class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="user",
            password="password",
            db="db"
        )
        self.cursor = self.connection.cursor()



