import psycopg2

params = {
    "host": "localhost",
    "database": "photon",
    "user": "student",
    "password": "student"
}

def get_connection():
    return psycopg2.connect(**params)

def get_codename(conn, player_id):
    with conn.cursor() as cur:
        cur.execute("SELECT codename FROM players WHERE id = %s;", (player_id,))
        result = cur.fetchone()

        if result:
            return result[0]
        return None

def insert_player(conn, player_id, codename):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO players (id, codename) VALUES (%s, %s)", (player_id, codename))
    
    conn.commit()