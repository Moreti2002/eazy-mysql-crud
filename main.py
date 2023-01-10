"""
Main code

By: Joao Moreti®
"""
import mysql.connector

class Crud:
    """This class provide an stable SQL connection"""
    def __init__(self,host,database,user,password) -> None:
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    # <--< CONECTION >-------------------------------------------------------->
    def __con(self):
        con = mysql.connector.connect(user=self.user,
                            password=self.password,
                            host=self.host,
                            database=self.database)

    # <--< CURSOR >----------------------------------------------------------->
    def __cursor(self):
        cursor = self.__con.cursor()
        return cursor

    # <--< SELECT >----------------------------------------------------------->
    def select(self,table,fields,where=None,order_by=None) -> list:
        """CRUD select do mysql\n
            """

        query = "SELECT " + fields + " FROM " + table
        arg = (str(type(where)),str(type(order_by)))

        match arg:
            case ("<class 'str'>","<class 'NoneType'>"):
                query = "SELECT " + fields + " FROM " + table + " WHERE " + where
            case ("<class 'NoneType'>","<class 'str'>"):
                query = "SELECT " + fields + " FROM " + table + " ORDER BY " + order_by
            case ("<class 'str'>","<class 'str'>"):
                query = "SELECT " + fields + " FROM " + table + " WHERE " + where + " ORDER BY " + order_by
            case ("<class 'NoneType'>","<class 'NoneType'>"):
                query = "SELECT " + fields + " FROM " + table
        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    # <--< INSERT >----------------------------------------------------------->
    def insert(self,table,fields,values)-> list:
        """CRUD insert do mysql\n
            fields arg. exemplo --> field='(field1,field2,...,fieldn)'\n
            values arg. exemplo --> values='(valor1,valor2,...,valorn)'"""

        query = "INSERT INTO " + table + fields +" VALUES" + values

        # logging.info(query)

        self.__cursor.execute(query)
        self.__con.commit()

    # <--< DELETE >----------------------------------------------------------->
    def delete(self,table,where):
        """CRUD delete do sql"""

        query = "DELETE " + "FROM " + table + " WHERE " + where

        self.__cursor.execute(query)
        self.__con.commit()
    
    # <---< CLOSE CONNECTION >------------------------------------------------->
    def close_con(self):
        self.__con.close()