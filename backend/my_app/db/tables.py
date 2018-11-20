"""Set SQL queries for creating database tables"""

USERS = """ CREATE TABLE IF NOT EXISTS users(
        user_id serial PRIMARY KEY,
        name VARCHAR(48) NOT NULL,
        email VARCHAR(96) UNIQUE,
        password VARCHAR(255) NOT NULL,
        user_role VARCHAR(48) NOT NULL DEFAULT 'user'
        );
        """

PARCELS = """ CREATE TABLE IF NOT EXISTS parcels(
    parcel_id serial PRIMARY KEY,
    user_id serial NOT NULL,
    recipient VARCHAR(250) NOT NULL,
    status VARCHAR(48) NOT NULL DEFAULT 'pending delivery',
    weight INT NOT NULL,
    origin VARCHAR NOT NULL,
    destination VARCHAR(250) NOT NULL,
    current_location VARCHAR(250) NOT NULL,
    price INT NOT NULL,
    FOREIGN KEY (user_id)
            REFERENCES users (user_id)
            ON UPDATE CASCADE ON DELETE CASCADE
    );
            """

DROP_USERS = """ DROP TABLE IF EXISTS users CASCADE """

DROP_PARCELS = """ DROP TABLE IF EXISTS parcels """

TABLES_TO_DROP = [DROP_USERS, DROP_PARCELS]
