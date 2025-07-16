# Collaborators Management System with Python and PostgreSQL

A desktop application built with **PyQt5** that allows you to manage collaborators in a PostgreSQL database. You can **add, edit, and delete collaborators**, all through an intuitive graphical user interface.

---

## 📷 Screenshots

### ➤ Main View

![Main View](https://github.com/Kyara0797/Collabotators_with_Python_and_DB_Postgres/blob/main/images/Refence_Data.png)

### ➤ Delete Confirmation

![Delete Alert](https://github.com/Kyara0797/Collabotators_with_Python_and_DB_Postgres/blob/main/images/Reference_alert_delete.png)

---

## 🛠️ Tech Stack

- **Python 3**
- **PyQt5** – GUI
- **PostgreSQL** – Relational database
- **psycopg2** – Database driver
- **dotenv** – Environment variable management

---

## ⚙️ Features

- View list of collaborators in a table.
- Add new collaborators with name, role, and salary.
- Edit existing records.
- Delete collaborators with confirmation alert.
- Connects to a PostgreSQL database using credentials stored securely in a `.env` file.

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.8+
- PostgreSQL database (e.g. [Neon](https://neon.tech/) or local setup)

---

### 📦 Installation

1. **Clone this repository:**

```bash
git clone https://github.com/Kyara0797/Collabotators_with_Python_and_DB_Postgres.git
cd Collabotators_with_Python_and_DB_Postgres
```
2. **Create a virtual environment:**

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate 

3. **Install the dependencies:**

pip install -r requirements.txt

4. **Set up your .env file:**

DB_NAME=your_database
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=your_host
DB_PORT=5432
You can use .env.example as a reference.

🧪 Running the App
python collaborators_application.py

🗃️ Project Structure
Collabotators_with_Python_and_DB_Postgres/
├── images/                     # Screenshots for reference
├── util/
│   └── database.py             # Database config (uses .env)
├── main.py                     # Entry point
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

🛡️ Security Notes
DO NOT commit your actual .env file.
The .env file is included in .gitignore for your protection.


