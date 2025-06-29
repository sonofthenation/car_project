import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="car_project",
        user="postgres",
        password="just0",
        host="localhost",
        port="5432"
    )

def create_tables():
    connection=get_connection()
    cursor=connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS admin(
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        age INT,
        phone_num VARCHAR(12) UNIQUE,
        email VARCHAR(50) UNIQUE
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS car(
        id SERIAL PRIMARY KEY,
        model VARCHAR(20),
        make VARCHAR(20),
        year INT,
        price INT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS client(
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        age INT,
        passport VARCHAR(20) NOT NULL,
        model VARCHAR(20),
        model_id INT REFERENCES car(id),
        period INT,
        credit INT
    );
    """)

    connection.commit()
    print("Barcha jadvallar yaratildi!")
    connection.close()


def create_functions():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        create function monthly(price integer, credit integer, period integer) returns numeric
    language plpgsql
as
$$
begin
    return round(price*((credit/1200.0)*POWER((1+credit/1200.0),period))/(POWER((1+credit/1200.0),period)-1),2);
exception
    when division_by_zero then
        return 0;
    end;
$$;

alter function monthly(integer, integer, integer) owner to postgres;
        """)

    cursor.execute("""
        create function total(price integer, credit integer, period integer) returns numeric
    language plpgsql
as
$$
begin
    return round(price*((credit/1200.0)*POWER((1+credit/1200.0),period))/(POWER((1+credit/1200.0),period)-1)*period,2);
exception
    when division_by_zero then
        return 0;
end;
$$;

alter function total(integer, integer, integer) owner to postgres;
        """)

    cursor.execute("""
        create function monthly_na(price integer, credit integer, period integer)
    returns TABLE(month numeric)
    language plpgsql
as
$$
begin
    for i in 1..period loop
        month := round((price/period)+((price-(price/period)*(i-1))*(credit/1200.0)),2);
        RETURN NEXT;
    end loop;
exception
    when division_by_zero then
        return next;
end;
$$;

alter function monthly_na(integer, integer, integer) owner to postgres;
        """)

    connection.commit()
    print("Success")
    connection.close()