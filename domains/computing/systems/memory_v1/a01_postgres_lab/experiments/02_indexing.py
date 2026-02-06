
import psycopg2
import numpy as np
import time

def run_indexing_race():
    try:
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            user="letta",
            password="letta",
            dbname="letta"
        )
        cur = conn.cursor()
        print("[+] Connected to Postgres (letta-pg).")

        # 1. Setup Fresh Table (No Index yet)
        cur.execute("DROP TABLE IF EXISTS race_vectors;")
        cur.execute("CREATE TABLE race_vectors (id bigserial PRIMARY KEY, embedding vector(1536));")
        print("[+] Created table 'race_vectors' (1536 dim).")

        # 2. Bulk Insert (10k vectors)
        print("[*] Generating 10k random vectors (simulating OpenAI dim)...")
        vectors = np.random.rand(10000, 1536).astype(np.float32)
        
        print("[*] Inserting vectors...")
        start_time = time.time()
        # Use copy_from for speed? Or just loop for simplicity here? Loop is fine for 10k.
        # Actually 10k might be slow with single inserts. efficient batching:
        args_str = ','.join(cur.mogrify("(%s)", (v.tolist(),)).decode('utf-8') for v in vectors)
        cur.execute("INSERT INTO race_vectors (embedding) VALUES " + args_str)
        conn.commit()
        print(f"[+] Inserted 10k vectors in {time.time() - start_time:.2f}s.")

        # 3. Race 1: Sequential Scan (No Index)
        query_vec = np.random.rand(1536).tolist()
        print("[*] Race 1: Sequential Scan...")
        start_time = time.time()
        cur.execute("SELECT id, embedding <=> %s::vector FROM race_vectors ORDER BY embedding <=> %s::vector LIMIT 5;", (str(query_vec), str(query_vec)))
        rows = cur.fetchall()
        seq_time = time.time() - start_time
        print(f"[-] Sequential Scan Time: {seq_time:.4f}s")

        # 4. Add Index (HNSW)
        print("[*] Building HNSW Index (ivfflat is simpler, but let's try hnsw if pg15+)...")
        # vector < 0.5.0 uses ivfflat usually, typically users install latest.
        # Let's try HNSW.
        start_time = time.time()
        cur.execute("CREATE INDEX ON race_vectors USING hnsw (embedding vector_cosine_ops);")
        conn.commit()
        print(f"[+] Index Built in {time.time() - start_time:.2f}s.")

        # 5. Race 2: Index Scan
        print("[*] Race 2: HNSW Index Scan...")
        start_time = time.time()
        cur.execute("SELECT id, embedding <=> %s::vector FROM race_vectors ORDER BY embedding <=> %s::vector LIMIT 5;", (str(query_vec), str(query_vec)))
        rows = cur.fetchall()
        idx_time = time.time() - start_time
        print(f"[-] Index Scan Time: {idx_time:.4f}s")
        
        # Results
        speedup = seq_time / idx_time
        print(f"\n[=] RESULTS: Index is {speedup:.2f}x faster.")

        cur.close()
        conn.close()

    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    run_indexing_race()
