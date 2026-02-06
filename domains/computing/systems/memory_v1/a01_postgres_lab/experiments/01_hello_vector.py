
import psycopg2
from psycopg2.extensions import register_adapter, AsIs
import numpy as np

def test_vector_connection():
    try:
        # Credentials from 'docker inspect letta-pg'
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            user="letta",
            password="letta",
            dbname="letta"
        )
        cur = conn.cursor()
        
        print("[+] Connected to Postgres (letta-pg).")
        
        # 1. Enable Extension
        cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
        print("[+] Vector Extension Enabled.")
        
        # 2. Create Table
        cur.execute("DROP TABLE IF EXISTS test_vectors;")
        cur.execute("CREATE TABLE test_vectors (id bigserial PRIMARY KEY, embedding vector(3));")
        print("[+] Table 'test_vectors' created.")
        
        # 3. Insert Vector
        vec = [1.1, 2.2, 3.3]
        cur.execute("INSERT INTO test_vectors (embedding) VALUES (%s)", (str(vec),))
        print(f"[+] Inserted vector: {vec}")
        
        # 4. Query Vector
        cur.execute("SELECT * FROM test_vectors;")
        row = cur.fetchone()
        print(f"[+] Retrieved row: {row}")
        
        conn.commit()
        cur.close()
        conn.close()
        return True
        
    except Exception as e:
        print(f"[-] Error: {e}")
        return False

if __name__ == "__main__":
    test_vector_connection()
