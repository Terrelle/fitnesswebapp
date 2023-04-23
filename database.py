import mysql.connector

def connect():
    # create database connection
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="fitnessApp"
    )
    return db


def get_products():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    db.close()

    return products

def add_product_db(name, price, description, image):
    db = connect()
    cursor = db.cursor()
    query = "INSERT INTO products (name, price, description, image) VALUES (%s, %s, %s, %s)"
    values = (name, price, description, image)
    cursor.execute(query, values)
    db.commit()
    db.close()

def remove_product_db(product_id):
    db = connect()
    cursor = db.cursor()
    query = "DELETE FROM products WHERE id = %s"
    cursor.execute(query, (product_id,))
    db.commit()
    db.close()


def get_events():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM events")
    events = cursor.fetchall()
    db.close()

    return events

def add_event_db(name, location, description, image):
    db = connect()
    cursor = db.cursor()
    query = "INSERT INTO events (name, location, description, image) VALUES (%s, %s, %s, %s)"
    values = (name, location, description, image)
    cursor.execute(query, values)
    db.commit()
    db.close()

def remove_event_db(event_id):
    db = connect()
    cursor = db.cursor()
    query = "DELETE FROM events WHERE id = %s"
    cursor.execute(query, (event_id,))
    db.commit()
    db.close()

