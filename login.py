from database import connect


def check_login(u,p):

    con=connect()

    cur=con.cursor()


    cur.execute(

    """
    SELECT *
    FROM Users
    WHERE username=%s
    AND password=%s

    """,

    (u,p)

    )


    result=cur.fetchone()


    con.close()


    return result is not None
