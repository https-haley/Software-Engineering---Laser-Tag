import psycopg2

# Database connection parameters
params = {
    "host": "localhost",
    "database": "photon",
    "user": "student",
    "password": "student"
}

# Establish and return a connection to the database
def get_connection():
    return psycopg2.connect(**params)

# Retrieve a player's codename using their player ID
def get_codename(conn, player_id):
    with conn.cursor() as cur:
        cur.execute("SELECT codename FROM players WHERE id = %s;", (player_id,))
        result = cur.fetchone()

        if result:
            return result[0]
        return None

# Insert a new player into the database
def insert_player(conn, player_id, codename):
    with conn.cursor() as cur:
        # Insert player ID and codename into players table
        cur.execute("INSERT INTO players (id, codename) VALUES (%s, %s)", (player_id, codename))
        conn.commit()

# Look up a player ID using a codename (used to detect duplicates or existing players)
def get_player_id(conn, codename):
    with conn.cursor() as cur:
        # Search for player ID with matching codename
        cur.execute("SELECT id FROM players WHERE codename = %s", (codename,))
        row = cur.fetchone()
        return row[0] if row else None

# Update an existing player's codename using their player ID
def update_codename(conn, player_id, new_codename):
    with conn.cursor() as cur:
        # Update codename for the specified player ID
        cur.execute("UPDATE players SET codename = %s WHERE id = %s;", (new_codename, player_id))
    conn.commit()

# Delete a player record from the database using their unique player ID
def delete_player(conn, player_id):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM players WHERE id = %s;", (player_id,))
    conn.commit()



