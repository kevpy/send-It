import psycopg2

conn = None

try:
    connect_str = "dbname='pg' user='kibet' host='localhost' " + \
                  "password='newpassword'"
    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()

    sql1 = """ CREATE TABLE IF NOT EXISTS users(
            user_id serial PRIMARY KEY,
            username VARCHAR(250) NOT NULL,
            email VARCHAR(96) UNIQUE,
            password VARCHAR(48) NOT NULL,
            status VARCHAR(48) NOT NULL DEFAULT 'pending delivery',
            user_role VARCHAR(48) NOT NULL DEFAULT 'user'
            );
            """

    sql2 = """ CREATE TABLE IF NOT EXISTS parcels(
            parcel_id serial PRIMARY KEY,
            recipient VARCHAR(250) NOT NULL,
            weight INT NOT NULL,
            destination VARCHAR(250) NOT NULL,
            price INT NOT NULL
            );
            """

    queries = [sql1, sql2]
    # create a new table with a single column called "name"

    for item in queries:
        cursor.execute(item)
    conn.commit()
    # run a SELECT statement - no data in there, but we can try it
    cursor.execute("""SELECT * from users""")
    rows = cursor.fetchall()
    print(rows)
except Exception as e:
    print("Uh oh, can't connect. Invalid dbname, user or password?")
    print(e)
