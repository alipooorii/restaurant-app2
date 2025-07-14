# سیستم مدیریت غذای شرکت

یک وب اپلیکیشن کامل برای مدیریت انتخاب غذای کارکنان در شرکت‌ها، ساخته شده با Flask و React.

## ویژگی‌ها

### برای کاربران عادی
- ثبت‌نام اولیه با تایید هویت (شماره پرسنلی + شماره ملی)
- ورود با شماره پرسنلی و رمز عبور
- مشاهده منوی غذای هفته جاری و آینده
- انتخاب غذا برای هر وعده (صبحانه، ناهار، شام)
- امکان تغییر رمز عبور
- داشبورد کاربرپسند با طراحی فارسی

### برای مدیران
- پنل مدیریت کامل
- ایجاد و مدیریت منوی هفتگی
- مدیریت لیست کاربران مجاز
- تنظیم بازه زمانی انتخاب غذا
- مشاهده آمار و گزارش انتخاب‌های غذا
- تغییر رمز عبور کاربران

## تکنولوژی‌های استفاده شده

### Backend
- **Flask**: فریمورک وب Python
- **SQLAlchemy**: ORM برای مدیریت پایگاه داده
- **SQLite**: پایگاه داده
- **Flask-CORS**: پشتیبانی از CORS
- **PyJWT**: مدیریت JWT tokens
- **Werkzeug**: هش کردن رمزهای عبور

### Frontend
- **React**: کتابخانه JavaScript
- **Vite**: ابزار build
- **Tailwind CSS**: فریمورک CSS
- **shadcn/ui**: کامپوننت‌های UI
- **Lucide React**: آیکون‌ها

## ساختار پروژه

```
restaurant-app/
├── src/
│   ├── main.py                 # فایل اصلی Flask
│   ├── models/                 # مدل‌های پایگاه داده
│   │   ├── user.py
│   │   ├── menu.py
│   │   ├── selection.py
│   │   └── setting.py
│   ├── routes/                 # API routes
│   │   ├── auth.py
│   │   ├── user.py
│   │   ├── menu.py
│   │   ├── selection.py
│   │   └── admin.py
│   ├── database/               # فایل‌های پایگاه داده
│   └── static/                 # فایل‌های استاتیک React
├── create_admin.py             # اسکریپت ایجاد مدیر
├── requirements.txt            # وابستگی‌های Python
├── test_report.md             # گزارش تست‌ها
└── README.md                  # این فایل
```

## نصب و راه‌اندازی

### پیش‌نیازها
- Python 3.11+
- Node.js 20+
- npm یا yarn

### مراحل نصب

1. **کلون کردن پروژه**
```bash
git clone <repository-url>
cd restaurant-app
```

2. **راه‌اندازی محیط مجازی Python**
```bash
python -m venv venv
source venv/bin/activate  # در Linux/Mac
# یا
venv\Scripts\activate     # در Windows
```

3. **نصب وابستگی‌های Python**
```bash
pip install -r requirements.txt
```

4. **ایجاد پایگاه داده و کاربر مدیر**
```bash
python create_admin.py
```

5. **راه‌اندازی سرور**
```bash
python src/main.py
```

سرور روی `http://localhost:5000` در دسترس خواهد بود.

## اطلاعات ورود پیش‌فرض

### مدیر
- شماره پرسنلی: `admin`
- رمز عبور: `admin123`

### کاربران نمونه (برای تست)
- شماره پرسنلی: `1001`, شماره ملی: `1234567890`
- شماره پرسنلی: `1002`, شماره ملی: `0987654321`
- شماره پرسنلی: `1003`, شماره ملی: `1122334455`

## API Documentation

### Authentication Endpoints

#### POST /api/auth/register-step1
تایید هویت برای ثبت‌نام
```json
{
  "employee_id": "1001",
  "national_id": "1234567890"
}
```

#### POST /api/auth/register-step2
تکمیل ثبت‌نام
```json
{
  "employee_id": "1001",
  "password": "newpassword",
  "confirm_password": "newpassword"
}
```

#### POST /api/auth/login
ورود کاربر
```json
{
  "employee_id": "1001",
  "password": "password"
}
```

### Menu Endpoints

#### GET /api/menus
دریافت لیست منوها

#### POST /api/menus
ایجاد منوی جدید (فقط مدیر)
```json
{
  "week_start_date": "2025-07-19",
  "food_items": [...]
}
```

### Selection Endpoints

#### GET /api/selections/my-selections
دریافت انتخاب‌های کاربر

#### POST /api/selections
ثبت انتخاب غذا
```json
{
  "menu_id": 1,
  "day_of_week": "شنبه",
  "meal_type": "ناهار",
  "food_item_id": 5
}
```

### Admin Endpoints

#### GET /api/admin/allowed-users
دریافت لیست کاربران مجاز (فقط مدیر)

#### POST /api/admin/allowed-users
اضافه کردن کاربران مجاز (فقط مدیر)

#### GET /api/admin/settings
دریافت تنظیمات سیستم (فقط مدیر)

#### POST /api/admin/settings
به‌روزرسانی تنظیمات (فقط مدیر)

## پایگاه داده

### جداول اصلی

1. **users**: اطلاعات کاربران
2. **allowed_users**: لیست کاربران مجاز برای ثبت‌نام
3. **menus**: منوهای هفتگی
4. **food_items**: آیتم‌های غذا در هر منو
5. **selections**: انتخاب‌های غذای کاربران
6. **settings**: تنظیمات سیستم

## امنیت

- رمزهای عبور با bcrypt هش می‌شوند
- احراز هویت با JWT tokens
- تفکیک دسترسی مدیر و کاربر عادی
- تایید هویت دو مرحله‌ای برای ثبت‌نام
- محدودیت دسترسی به API endpoints

## تست

پروژه شامل تست‌های جامع در موارد زیر است:
- تست احراز هویت
- تست رابط کاربری
- تست API endpoints
- تست امنیت
- تست عملکرد

برای اجرای تست‌ها، گزارش کامل در فایل `test_report.md` موجود است.

## استقرار (Deployment)

### استقرار محلی
```bash
python src/main.py
```

### استقرار در سرور
1. تنظیم متغیرهای محیطی
2. استفاده از WSGI server مثل Gunicorn
3. تنظیم reverse proxy با Nginx
4. تنظیم SSL certificate

### Docker (اختیاری)
```dockerfile
# Dockerfile نمونه
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "src/main.py"]
```

## مشارکت

برای مشارکت در پروژه:
1. Fork کنید
2. Branch جدید ایجاد کنید
3. تغییرات را commit کنید
4. Pull request ارسال کنید

## لایسنس

این پروژه تحت لایسنس MIT منتشر شده است.

## پشتیبانی

برای گزارش مشکلات یا درخواست ویژگی جدید، لطفاً issue جدید ایجاد کنید.

---

**نکته**: این سیستم برای استفاده در محیط شرکتی طراحی شده و شامل تمام ویژگی‌های مورد نیاز برای مدیریت غذای کارکنان است.

