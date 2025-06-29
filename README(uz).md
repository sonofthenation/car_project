# 🚗 Avtokredit Loyihasi

Ro‘yxatdan o‘tkazish va avtokredit arizalarini qayta ishlash uchun mo‘ljallangan ko‘p tilli konsol ilovasi.
Foydalanuvchilarga avtomobil tanlash, o‘z ma’lumotlarini kiritish va har oylik hamda umumiy to‘lovlarni hisoblab olish imkonini beradi — bu jarayon an’anaviy (annuitet) yoki differensial usulda amalga oshiriladi.

---

## 🔧 Foydalanilgan texnologiyalar

- 🐍 Python 3.10+
- 🛢 PostgreSQL (psycopg2 orqali)
- 🌐 Ikki tilli interfeys: 🇺🇿 O‘zbek / en English
- 📊 Kredit hisoblash formulalari SQL-funksiyalar ko‘rinishida ma’lumotlar bazasiga kiritilgan
---

## 🧩 Asosiy imkoniyatlar

- Administratorlar, avtomobillar va mijozlarni ro‘yxatdan o‘tkazish
- Muddat va foiz stavkasi asosida zudlik bilan to‘lov hisoblash
- An’anaviy (annuitet) yoki differensial kredit turini tanlash imkoniyati
- Interaktiv menyuli terminal orqali boshqaruv
- To‘liq tilga moslashtirilgan interfeys

---

## 🚀 Qanday ishga tushirish mumkin

1. **Repodagi fayllarni klonlang:**

```bash
git clone https://github.com/sonofthenation/car_project.git
cd car_project
```

2. **Virtual muhit yarating va kerakli kutubxonalarni o‘rnating:**

```bash
python -m venv venv
venv\Scripts\activate        # For Windows
# source venv/bin/activate    # For Linux/macOS
pip install psycopg2
```

3. **PostgreSQL ulanishini sozlang:**

[`db.py`](./db.py) faylini oching va PostgreSQL parolingizni kiriting:

```python
password = "YOUR_PASSWORD"
```

`car_project` nomli ma’lumotlar bazasi yaratilganligiga ishonch hosil qiling.

4. **Jadvallar va SQL-funksiyalarni yarating:**
`main.py` faylida quyidagi qatorlarning izohini olib tashlang:
```python
create_tables()
create_functions()
```
So‘ng ishga tushiring:
```bash
python main.py
```
Ilovani birinchi marta ishga tushirgandan so‘ng bu qatorlarni qayta izohga olishingiz mumkin.

---

## 🗂 Loyihaning tuzilmasi

```
car_project/
├── main.py              # Kirish nuqtasi
├── config.py            # Standart til
├── lang.py              # Tarjimalar
├── db.py                # Ma’lumotlar bazasiga ulanish
├── admins.py            # Administratorlar bilan ishlash
├── cars.py              # Avtomobillar bilan ishlash
├── clients.py           # Mijozlar va kreditlar bilan ishlash
```

---

## 🌐 Tilni tanlash

Dastur ishga tushirilganda quyidagicha so‘rov ko‘rsatiladi:
```
Choose language/Tilni tanlang:
1 English    2 O'zbek
```

---

## 📬 Aloqa

Loyiha muallifi: [@sonofthenation](https://github.com/sonofthenation).

---

