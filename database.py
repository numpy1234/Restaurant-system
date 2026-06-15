import mysql.connector


def connect():

    return mysql.connector.connect(

        host="localhost",

        user="root",

        passwd="Put_your_own_password",

        database="restaurant"

    )
