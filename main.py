from db import create_tables,create_functions
from lang import tr
from admins import add_admin, get_admin
from cars import add_car, get_car, del_from_car
from clients import add_client, get_client, get_credit

if __name__=="__main__":
    # create_tables()
    # create_functions()
    while True:
        model=0
        print(tr('welcome'))
        choice=input()
        if choice=='1':
            get_admin()
            name=input(tr('admin_name'))
            if name=='0':
                continue
            age=int(input(tr("admin_age")))
            phone_num=input(tr("admin_phone"))
            email=input(tr("admin_email"))
            add_admin(name,age,phone_num,email)
        elif choice=='2':
            get_car()
            make=input(tr("car_make"))
            if make=='0':
                continue
            model=input(tr("car_model"))
            year=int(input(tr("car_year")))
            price=int(input(tr("car_price")))
            add_car(model,make, year, price)
        elif choice=='3':
            name=input(tr("client_name"))
            if name=='0':
                continue
            age=int(input(tr('client_age')))
            passport=input(tr("client_passport"))
            get_car()
            model=input(tr("car_choice_model"))
            model_id=int(input(f"{model}{tr('car_model_id')}"))
            while True:
                try:
                    period=int(input(tr("credit_period")))
                    if period==36:
                        credit=35
                    elif period==48:
                        credit = 40
                    elif period==60:
                        credit = 45
                    elif period==0:
                        break
                    else:
                        print(tr("credit_only_options"))
                        continue
                    print(f"{tr('credit_rate')}{credit}%")
                    add_client(name, age, passport, model, model_id, period, credit)
                    break
                except Exception:
                    print(tr("error"))
            if period==0:
                continue
        elif choice=='4':
            get_client()
        elif choice=='5':
            get_client()
            ids=int(input(tr("client_id_choose")))
            get_credit(ids)
        elif choice=='6':
            a=input(tr("confirm"))
            if a=='1':
                break
            else:
                continue