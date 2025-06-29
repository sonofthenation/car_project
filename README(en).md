# 🚗 Car Credit Project

A multilingual console application for registering and processing car loan applications.
It allows users to choose a car, enter their personal information, and receive a calculation of monthly and total payments using either the fixed or differentiated system.

---

## 🔧 Technologies Used

- 🐍 Python 3.10+
- 🛢 PostgreSQL (via psycopg2)
- 🌐 Bilingual interface: 🇺🇿 Uzbek / en English
- 📊 Loan calculation formulas embedded in the database as SQL functions
---

## 🧩 Main Features

- Registration of administrators, cars, and clients
- Instant payment calculation based on term and interest rate
- Choice between fixed and differentiated loan types
- Terminal-based management with interactive menu
- Full localization of the interface

---

## 🚀 How to Run

1. **Clone the repository:**

```bash
git clone https://github.com/sonofthenation/car_project.git
cd car_project
```

2. **Create a virtual environment and install dependencies:**

```bash
python -m venv venv
venv\Scripts\activate        # For Windows
# source venv/bin/activate    # For Linux/macOS
pip install psycopg2
```

3. **Configure the PostgreSQL connection:**

Open the [`db.py`](./db.py) file and enter your PostgreSQL password:

```python
password = "YOUR_PASSWORD"
```

Make sure that a database named `car_project` has already been created.

4. **Create tables and SQL functions:**
In `main.py`, uncomment the lines:
```python
create_tables()
create_functions()
```
Then run:
```bash
python main.py
```
After the first launch, you can comment these lines back again.

---

## 🗂 Project Structure

```
car_project/
├── main.py              # Entry point
├── config.py            # Default language
├── lang.py              # Translations
├── db.py                # Database connection
├── admins.py            # Administrator management
├── cars.py              # Car management
├── clients.py           # Client and loan management
```

---

## 🌐 Language Selection

When launched, the program prompts:
```
Choose language/Tilni tanlang:
1 English    2 O'zbek
```

---

## 📬 Contact

This project was developed by [@sonofthenation](https://github.com/sonofthenation).

---

