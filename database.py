import mysql.connector


def connect():

    return mysql.connector.connect(

        host="localhost",

        user="root",

        passwd="jee2024",

        database="restaurant"

    )
