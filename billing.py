from database import connect


def bills():

    con=connect()
    cur=con.cursor()


    cur.execute(
    "SELECT * FROM Bills"
    )


    for x in cur.fetchall():

        print(x)
