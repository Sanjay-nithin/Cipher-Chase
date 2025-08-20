# 🔐 Cipher Chase

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Django](https://img.shields.io/badge/Django-Framework-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Cipher Chase is an **interactive coding challenge game** where you solve coding problems and chase down hidden solutions and move through the world of **AZMARA**.  
It uses a self-hosted [Piston API](https://github.com/engineer-man/piston) for code execution.

---

## 📂 Project Structure

```bash
Cipher-Chase/
│── chase/ # Main Django app
│ ├── pycache/ # Compiled Python files
│ ├── migrations/ # Database migration files
│ ├── static/ # Static files (CSS, JS, images)
│ ├── templates/ # HTML templates
│ ├── init.py # Marks this as a Python package
│ ├── admin.py # Django admin configuration
│ ├── apps.py # App configuration
│ ├── models.py # Database models
│ ├── tests.py # Test cases
│ ├── urls.py # URL routing for the app
│ └── views.py # View functions / controllers
│
│── cipher/ # (Custom app/module, if applicable)
    │
    │── .env # Environment variables (Piston API, secrets)
    │── cypher-key.pem # Encryption key file
    │── db.sqlite3 # SQLite database
    │── manage.py # Django project manager
    │── requirements.txt # Python dependencies
    └── README.md # Project documentation
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Sanjay-nithin/Cipher-Chase.git
cd Cipher-Chase
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Environment Variables
You need to self-host the Piston API locally.
After hosting, create a .env file in the root directory and add your API URL:
```bash
# .env
PISTON_API=YOUR_PISTON_API_URL
```
🔄 Replace YOUR_PISTON_API_URL with your actual hosted Piston API URL.

### 4️⃣ Run the Server
python manage.py runserver


### 🌐 Usage

Once the server is running, open your browser and visit:

👉 http://127.0.0.1:8000

⚡ Pro Tip: Keep the Piston API server running in the background for smooth gameplay.
