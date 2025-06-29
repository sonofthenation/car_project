from config import cur_lan

text={
    "welcome": {
        "uz": """Assalomu aleykum, halol nasiyaga xush kelibsiz!
        1 Admin qo'shish
        2 Mashina olibkelish
        3 Kredit rasmiylashtirish
        4 Mijozlarni ko'rish
        5 Kredit id
        6 Chiqish
        """,
        "en": """Welcome to the honest installment system!
        1 Add Admin
        2 Add Car
        3 Apply for Credit
        4 View Clients
        5 Credit by ID
        6 Exit
        """
    },
    "choose": {
        "uz": "Iltimos, tanlang: ",
        "en": "Please choose an option: "
    },
    "confirm": {
        "uz": "Tasdiqlaysizmi? (1 Ha / 2 Yo'q): ",
        "en": "Are you sure? (1 Yes / 2 No): "
    },
    "admin_name": {
        "uz": "Admin ismi (0-bekor qilish): ",
        "en": "Admin name (0 to cancel): "
    },
    "admin_age": {
        "uz": "Admin yoshi: ",
        "en": "Admin age: "
    },
    "admin_phone": {
        "uz": "Admin telefon raqami: ",
        "en": "Admin phone number: "
    },
    "admin_email": {
        "uz": "Admin email pochtasi: ",
        "en": "Admin email: "
    },
    "car_make": {
        "uz": "Mashina brendini kiriting (0-bekor qilish): ",
        "en": "Enter car brand (0 to cancel): "
    },
    "car_model": {
        "uz": "Mashina modelini kiriting: ",
        "en": "Enter car model: "
    },
    "car_year": {
        "uz": "Mashina yilini kiriting: ",
        "en": "Enter car year: "
    },
    "car_price": {
        "uz": "Mashina narxini kiriting: ",
        "en": "Enter car price: "
    },
    "client_name": {
        "uz": "Assalomu aleykum, Ismingiz?😊 (0-bekor qilish): ",
        "en": "Hello! What's your name?😊 (0 to cancel): "
    },
    "client_age": {
        "uz": "Hamda yoshingiz😊: ",
        "en": "And your age😊: "
    },
    "client_passport": {
        "uz": "Iltimos pasport ma'lumotlaringizni kiriting(AA1234567): ",
        "en": "Please enter your passport (AA1234567): "
    },
    "car_choice_model": {
        "uz": "Olmoqchi bo'lgan mashinangiz modelini kiriting😊: ",
        "en": "Which car model would you like to buy?😊: "
    },
    "car_model_id": {
        "uz": " rusumli mashina id-si: ",
        "en": " model car ID: "
    },
    "credit_period": {
        "uz": "Qaysi muddatga harid qilmoqchisiz(36-48-60 oy, 0-bekor qilish): ",
        "en": "For how many months? (36-48-60, 0 to cancel): "
    },
    "credit_only_options": {
        "uz": "Bizda faqat 36, 48 yoki 60 oy muddatli kredit mavjud!",
        "en": "Only 36, 48 or 60-month installments are available!"
    },
    "client_id_choose": {
        "uz": "Qaysi id: ",
        "en": "Choose the ID: "
    },
    "tables_created": {
        "uz": "Barcha jadvallar yaratildi!",
        "en": "All tables have been created!"
    },
    "admin_added": {
        "uz": " qo'shildi",
        "en": " has been added"
    },
    "car_added": {
        "uz": " mashinasi qo'shildi",
        "en": " car has been added"
    },
    "client_applied": {
        "uz": " rusumli mashinani muddatli to'lov orqali harid qilish uchun so'rovingiz qabul qilindi!",
        "en": " car in installments has been accepted!"
    },
    "monthly_payment": {
        "uz": "Oy ma oy to'lovingiz: ",
        "en": "Your monthly payment: "
    },
    "total_payment": {
        "uz": "Umumiy to'lovingiz: ",
        "en": "Your total payment: "
    },
    "credit_type": {
        "uz": "Kerdit turini tanlang\n1 Fiks\t2 Differensial\n",
        "en": "Choose credit type\n1 Fixed\t2 Differential\n"
    },
    "credit_rate": {
        "uz": "Bu muddat uchun kredit foizi: ",
        "en": "Credit rate for this term: "
    },
    "error": {
        "uz": "Xato, faqat son kiriting",
        "en": "Error, enter only number"
    }
}

check=cur_lan()

def tr(key):
    return text[key][check]