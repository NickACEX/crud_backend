from psycopg2 import connect

class Connector:

    def __init__(self,user="postgres",password="yourpassword",database="base_school"):#create a database
        self.user = user
        self.password = password
        self.database = database

    def __connection(self):
        self.con = connect(
        user = self.user,
        password = self.password,
        database = self.database
        )
        cursor = self.con.cursor()
        return cursor

    def register(self,table_name,**data):#register <student or professor
        cursor = self.__connection()
        sql = f"""INSERT INTO {table_name}{str(tuple(data.keys())).replace("'","")}
        VALUES({('%s,'*len(data))[:-1]})"""
        cursor.execute(sql,tuple(data.values()))
        self.__commit()
        self.__close()
        print("El usuario ha sido registrado con éxito")

    def get_data(self,table_name,fields,condition,*values):
        cursor = self.__connection()
        sql = f"""select {fields} 
        from {table_name} 
        where {condition}"""
        cursor.execute(sql,values)
        data = cursor.fetchone()
        self.__close()
        return data

    def get_all(self,table_name):
        cursor = self.__connection()
        sql = f"""select *
        from {table_name}"""
        cursor.execute(sql)
        data = cursor.fetchall()
        self.__close()
        return data

    def delete(self,table_name,conditions,*values):
        cursor = self.__connection()
        sql = f"""DELETE FROM {table_name}
        WHERE {conditions}"""
        cursor.execute(sql,values)
        self.__commit()
        self.__close()
        print("Se ha eliminado con éxito")

    def update(self,table_name,fields_set,conditions_where,*values):
        cursor = self.__connection()
        sql = f"""UPDATE {table_name}
        set {fields_set}
        where {conditions_where}"""
        cursor.execute(sql,values)
        self.__commit()
        self.__close()
        print("Se actualizó la base correctamente.")

    def __commit(self):
        self.con.commit()

    def __close(self):
        self.con.close()

