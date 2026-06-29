# 🔐 Week 6 Authentication System

A secure authentication system built using **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **JWT Authentication**. This project demonstrates user authentication, authorization, role-based access control, password hashing, refresh tokens, and protected API endpoints.

---

# 🚀 Features

- User Registration
- User Login
- JWT Access Token Authentication
- Refresh Token Support
- Password Hashing using bcrypt
- OAuth2 Password Bearer Authentication
- Protected Routes
- Role-Based Authorization
- Admin-only APIs
- Employee Protected APIs
- Logout Endpoint
- Interactive Swagger Documentation

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| FastAPI | Backend Framework |
| PostgreSQL | Database |
| SQLAlchemy | ORM |
| JWT | Authentication |
| bcrypt + Passlib | Password Hashing |
| OAuth2PasswordBearer | Token Authentication |
| Uvicorn | ASGI Server |

---

# 📂 Project Structure

```
AuthSystem/
│
├── app/
│   ├── database/
│   ├── models/
│   ├── repositories/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project

```bash
cd AuthSystem
```

Create Virtual Environment

```bash
python -m venv .venv
```

Activate Virtual Environment

Windows

```bash
.venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

```bash
uvicorn app.main:app --reload
```

Application URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# 🔑 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /register | Register a new user |
| POST | /login | Login user |
| POST | /refresh-token | Generate new access token |
| POST | /logout | Logout user |
| GET | /me | Current logged-in user |
| GET | /profile | User profile |
| GET | /employees | Employee-only endpoint |
| GET | /admin | Admin-only endpoint |

---

# 🔒 Authentication Flow

```
Register User
      │
      ▼
Password Hashing (bcrypt)
      │
      ▼
Store User in PostgreSQL
      │
      ▼
User Login
      │
      ▼
Generate JWT Access Token
      │
      ▼
Generate Refresh Token
      │
      ▼
Access Protected APIs
      │
      ▼
Access Token Expires
      │
      ▼
Use Refresh Token
      │
      ▼
Generate New Access Token
```

---

# 🛡 Security Features

- Passwords are hashed using bcrypt.
- JWT-based authentication.
- Refresh Token implementation.
- OAuth2 Password Bearer.
- Protected API endpoints.
- Role-Based Authorization.
- Admin route protection.
- Employee route protection.

---

# 📸 API Testing

All endpoints were successfully tested using:

- Swagger UI
- Postman

---

# 📦 Dependencies

Generate the requirements file using:

```bash
pip freeze > requirements.txt
```

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

# 👨‍💻 Author

**Padma Sanjana**

Full Stack Developer

Tech Birds Consulting Pvt. Ltd.
