from db import get_connection
from lang import tr


def add_car(model,make,year,price):
    connection=get_connection()
    cursor=connection.cursor()

    cursor.execute("""
    INSERT INTO car(model,make,year,price) VALUES(
    %s,%s,%s,%s)""",(model,make,year,price))
    connection.commit()
    print(f"'{model}'{tr('car_added')}")
    connection.close()

def get_car():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM car")
    cars = cursor.fetchall()
    for car in cars:
        print(car)
    connection.close()

def del_from_car(ids):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM car WHERE id=%s", (ids,))
    connection.commit()
    connection.close()