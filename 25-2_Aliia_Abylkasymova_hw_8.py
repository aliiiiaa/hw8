import sqlite3


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


database = 'hw.db'
sql_create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL, 
price DOUBLE(10,2) NOT NULL DEFAULT 0.0,
quantity TINYINT(5) NOT NULL DEFAULT 0
)
'''


def create_products(conn, products):
    try:
        sql = '''INSERT INTO products (product_title, price, quantity) 
        VALUES (?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def delete_product(conn, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def select_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def update_product_quantity(conn, product):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def update_product_price(conn, product):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def select_all_products(conn):
    try:
        sql = '''SELECT * FROM products WHERE price > 1000 AND  quantity > 50'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def search_products(conn):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE '%soap' '''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


connection = create_connection(database)
if connection is not None:
    create_table(connection, sql_create_products_table)
    create_products(connection, ('baby soap', 50.4, 200))
    create_products(connection, ('household soap', 20.79, 500))
    create_products(connection, ('just soap', 70.5, 340))
    create_products(connection, ('soft soap', 120.69, 530))
    create_products(connection, ('soap', 46.66, 780))
    create_products(connection, ('table', 2500.45, 20))
    create_products(connection, ('square table', 5500.33, 22))
    create_products(connection, ('round table', 6400, 64))
    create_products(connection, ('rectangular table', 7540.5, 103))
    create_products(connection, ('coffee table', 4300, 56))
    create_products(connection, ('book', 320.5, 2005))
    create_products(connection, ('big book', 530.43, 2590))
    create_products(connection, ('beautiful book', 1070.7, 490))
    create_products(connection, ('mini book', 268, 834))
    create_products(connection, ('huge book', 2040.99, 56))

    search_products(connection)
    select_all_products(connection)
    update_product_price(connection, (1180.4, 13))
    update_product_quantity(connection, (478, 2))
    delete_product(connection, 5)
    select_products(connection)
    print('Done')
    connection.close()