import sqlite3
conn = sqlite3.connect("snehal_library.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id TEXT PRIMARY KEY,
    title TEXT,
    author TEXT,
    is_available INTEGER DEFAULT 1
)
""")
conn.commit()
# ... (baaki ka code jaisa maine diya tha)