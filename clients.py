from db import get_connection
from lang import tr,check

def add_client(name,age,passport,model,model_id,period,credit):
    connection=get_connection()
    cursor=connection.cursor()

    cursor.execute("""INSERT INTO client(name,age,passport,model,model_id,period,credit) VALUES(
    %s,%s,%s,%s,%s,%s,%s)""",(name,age,passport,model,model_id,period,credit))
    connection.commit()
    half1=''
    if check=='uz':
        half1=f"{name}, tabriklaymiz sizning '{model}'"
    elif check=='en':
        half1=f"Congratulations {name}, your application to purchase a '{model}' "
    print(f"{half1}{tr("client_applied")}")
    connection.close()

def get_client():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""SELECT * FROM client""")
    clients = cursor.fetchall()
    for client in clients:
        print(client)
    connection.close()

def get_credit(ids):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""SELECT client.name,client.age,client.passport,car.model,car.make,car.price,client.credit,client.period
FROM client
JOIN car ON model_id=car.id
WHERE client.id=%s""",(ids,))
    alls=cursor.fetchone()
    print(alls)
    typo = input(tr("credit_type"))
    if typo == '1':
        print(tr("monthly_payment"))
        cursor.execute("""SELECT monthly(car.price,client.credit,client.period)FROM client
            JOIN car ON model_id=car.id
            WHERE client.id=%s""", (ids,))
        month = cursor.fetchone()
        for m in month:
            print(m)
        print(tr('total_payment'))
        cursor.execute("""SELECT total(car.price,client.credit,client.period)FROM client
                JOIN car ON model_id=car.id
                WHERE client.id=%s""", (ids,))
        total = cursor.fetchone()
        for t in total:
            print(t)
    elif typo == '2':
        print(tr("monthly_payment"))
        cursor.execute("""SELECT monthly_na(car.price,client.credit,client.period)FROM client
                    JOIN car ON model_id=car.id
                    WHERE client.id=%s""", (ids,))
        month = cursor.fetchall()
        i = 0
        total = 0
        mm='oy'
        if check=='en':
            mm='month'
        for mo in month:
            for m in mo:
                i += 1
                print(f"{i}-{mm}: {m}$")
                total += m
        print(f"{tr('total_payment')}{total}")
    connection.close()