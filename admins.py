from db import get_connection
from lang import tr

def add_admin(name,age,phone_num,email):
    connection=get_connection()
    cursor=connection.cursor()

    cursor.execute("""
    INSERT INTO admin(name,age,phone_num,email) VALUES(
    %s,%s,%s,%s)""",(name,age,phone_num,email))
    connection.commit()
    print(f"Admin '{name}'{tr('admin_added')}")
    connection.close()

def get_admin():
    connection=get_connection()
    cursor=connection.cursor()

    cursor.execute("SELECT * FROM admin")
    admins=cursor.fetchall()
    for admin in admins:
        print(admin)
    connection.close()

def del_from_admin(ids):
    connection=get_connection()
    cursor=connection.cursor()

    cursor.execute("DELETE FROM admin WHERE id=%s",(ids,))
    connection.commit()
    connection.close()

