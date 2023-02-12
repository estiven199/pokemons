from db.init_db import DataBase
import ast


class CrudBase(DataBase):
    

    def select(self, table: str, condiction: str, fields: str = '*', ):
        query  = 'SELECT {}  FROM {} {}'.format(fields, table, condiction)
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            raise

    def insert_data(self, table, fields, values, markers_num: int = 2):
        # Insertar el pokemon en la tabla pokemons (name, image_url) (data["name"], data["sprites"]["front_default"])
        markers = "%s," * markers_num
        markers = markers[:-1] 
        query  = "INSERT INTO {} {} VALUES ({}),{}".format(table, fields, markers, values)
        try:
            self.cursor.execute(query , values)
            self.connection.commit()
            return self.cursor.lastrowid
        except Exception as e:
            raise


crudbase = CrudBase()
