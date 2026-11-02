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

def add_book():
    print("\n--- Add New Book ---")
    bid = input("Book ID (jaise B101): ")
    title = input("Book Title: ")
    author = input("Author: ")
    try:
        cursor.execute("INSERT INTO books VALUES (?,?,?,1)", (bid, title, author))
        conn.commit()
        print(f"✅ '{title}' Save ho gaya!")
    except:
        print("❌ Ye ID pehle se hai!")

def view_books():
    print("\n--- All Books ---")
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    if not rows:
        print("Koi book nahi hai!")
        return
    for b in rows:
        status = "Available ✅" if b[3]==1 else "Issued 📚"
        print(f"ID:{b[0]} | {b[1]} by {b[2]} | {status}")

def issue_book():
    view_books()
    bid = input("\nIssue ID: ")
    cursor.execute("UPDATE books SET is_available=0 WHERE id=?", (bid,))
    conn.commit()
    print("📚 Issued!")

def return_book():
    bid = input("Return ID: ")
    cursor.execute("UPDATE books SET is_available=1 WHERE id=?", (bid,))
    conn.commit()
    print("✅ Returned!")

while True:
    print("\n========== SNEHAL'S LIBRARY ==========")
    print("1. Add Book\n2. View Books\n3. Issue Book\n4. Return Book\n5. Exit")
    ch = input("Choice: ")
    if ch=='1': add_book()
    elif ch=='2': view_books()
    elif ch=='3': issue_book()
    elif ch=='4': return_book()
    elif ch=='5': 
        print("Bye!")
        break