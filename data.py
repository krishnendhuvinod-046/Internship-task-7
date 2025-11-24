import sqlite3

conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT,
        quantity INTEGER,
        price REAL
    )
''')

sales_data = [
    ('Laptop', 3, 50000),
    ('Mouse', 10, 500),
    ('Keyboard', 5, 1500),
    ('Laptop', 1, 50000),
    ('Mouse', 5, 500)
]

cursor.executemany('INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)', sales_data)

conn.commit()
conn.close()
print("Database 'sales_data.db' created successfully with self made data.")