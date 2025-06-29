

def cur_lan():
    lan=''
    while True:
        lang=input("Choose language/Tilni tanlang:\n1 English\t2 O'zbek\n")
        if lang=='1':
            lan='en'
            break
        elif lang=='2':
            lan='uz'
            break
        else:
            print("Only 1 or 2/Faqat 1 yoki 2")
            continue
    return lan