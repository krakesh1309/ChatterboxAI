# 🤖 ChatterboxAI

ChatterboxAI is a fully functional AI chatbot web application built using Django and OpenAI's GPT API. It features secure user authentication, real-time chat, message history, and a modern responsive UI. Users can interact with an intelligent assistant that responds contextually to their messages.

---

## 🌟 Features

- 🔐 **User Authentication** – Register, Login, Logout functionality
- 💬 **Chat with GPT** – Ask anything and receive intelligent responses from OpenAI
- 🧠 **Contextual Memory** – Conversations saved per user in the database
- 🖥️ **Responsive UI** – Clean, mobile-friendly interface using Bootstrap
- 🔐 **Secret Protection** – Uses `.env` and `.gitignore` to prevent accidental API key leaks

---

## 🛠️ Tech Stack

- **Framework**: Django (Python)
- **Frontend**: HTML, CSS (Bootstrap), JavaScript
- **Database**: SQLite (can be upgraded to PostgreSQL or MySQL)
- **AI Engine**: OpenAI GPT-3.5 Turbo via API
- **Environment Management**: `python-decouple` for loading secrets securely

---

## 📁 Project Structure
chatgpt/ │ ├── chatbot/ │ ├── migrations/ │ ├── templates/ │ │ ├── base.html │ │ ├── chatbot.html │ │ ├── login.html │ │ └── register.html │ ├── static/ │ ├── init.py │ ├── admin.py │ ├── apps.py │ ├── models.py │ ├── urls.py │ ├── views.py │ ├── chatgpt/ # project settings │ ├── init.py │ ├── asgi.py │ ├── settings.py │ ├── urls.py │ └── wsgi.py │ ├── .gitignore ├── .env ├── db.sqlite3 ├── manage.py ├── requirements.txt └── README.md

---

## 🧪 Installation & Setup

1. **Clone the Repository**

```bash
git clone https://github.com/krakesh1309/ChatterboxAI.git
cd ChatterboxAI
2. **Create and Activate Virtual Environment**
python -m venv venv
# Windows
venv\Scripts\activate
3. **Create .env File in Project Root**
   OPENAI_API_KEY=your_openai_api_key_here
5 **Make Sure .env is Ignored in Git Ensure your .gitignore file contains:**
   .env
6. **Run Migrations**
 python manage.py migrate

7. **Start the Development Server**
    python manage.py runserver

8. ** Visit http://127.0.0.1:8000 in browser for project **






🙋‍♂️ Author
Rakesh Kumar
🎓 B.Tech 2024 | 🧑‍💻 Python & Django Developer
📍 Bengaluru, India
🔗 GitHub | LinkedIn
