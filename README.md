
# **🌟 AI Chatbot Project**

Welcome to the **AI Chatbot Project**, a Django-based web application that leverages OpenAI's GPT-3.5-turbo model to deliver real-time conversational AI capabilities 🤖💬. Users can securely register, authenticate, and interact with the chatbot in a clean, intuitive interface. All conversations are saved and displayed dynamically for the user 🗂️.

---

## **✨ Features**

### **🌐 Core Functionality**
- **🤖 AI-Powered Conversations**: Engage in real-time conversations with OpenAI's GPT-3.5-turbo chatbot.
- **🔒 User Authentication**: Secure login, registration, and logout functionality.
- **📜 Dynamic Chat History**: View past conversations with timestamps displayed in descending order.

### **⚙️ Backend Highlights**
- Built with **Django Framework** for robust and scalable application architecture.
- **🔗 OpenAI API Integration** for intelligent chatbot responses.
- **💾 Database-Driven Storage**: User chats are stored in a PostgreSQL-compatible database (easily switchable to other backends).

### **🖥️ Frontend Highlights**
- Responsive UI powered by **Bootstrap 4.3**.
- Dynamic **⚡ AJAX-based message handling** for a smooth user experience.
- Intuitive design with consistent styling and accessibility features.

---

## **🛠️ Technologies Used**

### **💻 Backend**
- **Django** (Python web framework)
- **Python-decouple**: Securely manage sensitive keys (e.g., OpenAI API key) using `.env` files.
- **OpenAI API**: GPT-3.5-turbo for chatbot responses.

### **🎨 Frontend**
- **HTML5** and **CSS3**: Build a responsive and accessible layout.
- **Bootstrap 4.3**: Modern design and styles for UI.
- **JavaScript**: Fetch API for dynamic interaction with the backend.

### **📂 Database**
- **SQLite** (default): Used during development. Can be switched to PostgreSQL/MySQL for production.

---

## **🚀 Project Setup**

### **Step 1: Clone the Repository** 🗂️
```bash
git clone https://github.com/your-username/ai-chatbot-project.git
cd ai-chatbot-project
```

### **Step 2: Set up a Virtual Environment** 💻
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **Step 3: Install Dependencies** 📦
```bash
pip install -r requirements.txt
```
### **Step 4: Configure the Environment Variables** 🔑
- Create a `.env` file in the root directory:
  ```env
  OPENAI_API_KEY=your-openai-api-key
  DEBUG=True
  ```
- Replace `your-openai-api-key` with your OpenAI API key from [OpenAI's account settings](https://platform.openai.com/account/api-keys).

### **Step 5: Apply Migrations** 📊
```bash
python manage.py makemigrations
python manage.py migrate
```

### **Step 6: Run the Development Server** 🌐
```bash
python manage.py runserver
```
Access the application at `http://127.0.0.1:8000/`.

---

## **🎯 Usage**

1. **🔏 Register** a new account or **🔑 Login** using existing credentials.
2. Type your queries or prompts in the chat input box and interact with the chatbot 🤖💬.
3. View your **📜 Chat History** directly in the interface.
4. **🚪 Logout** securely when done.

---

## **📂 Codebase Overview**

```
project/
├── app/
│   ├── models.py       # Chat model storing user conversations
│   ├── views.py        # Core logic for chatbot, login, register, and logout
│   ├── urls.py         # Routes specific to the application
│   ├── templates/      # HTML templates (chatbot.html, login.html, register.html)
│   └── static/         # Static assets (CSS, JS, etc.)
├── project/
│   ├── settings.py     # Django settings and API configurations
│   ├── urls.py         # Project-level URL configurations
├── .env                # Contains environment variables
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
```

---

## **🔍 Key Files Explained**

### **1. chatbot.html**
- Provides the user interface for chatbot interaction 💬.
- Sends and receives data dynamically using JavaScript `fetch()` ⚡.

### **2. login.html / register.html**
- Designed with responsive forms for secure user authentication 🔒.

### **3. views.py**
- Contains:
  - `chatbot`: Handles chat requests and responses via OpenAI API 🤖.
  - `login` and `register`: Manage user authentication 🔏.
  - `ask_openai`: Communicates with OpenAI to fetch chatbot responses 🔗.

### **4. urls.py**
- Maps URLs to corresponding views:
  - `/`: Chatbot interface 💬.
  - `/login/`, `/register/`, `/logout/`: Authentication endpoints 🔑.

---

## **⚠️ Error Handling**

### **Common Issues**
1. **OpenAI API Errors**:
   - **❌ Invalid API Key**: Ensure the key in `.env` is correct.
   - **🔄 Rate Limits**: Retry after some time or upgrade your OpenAI plan.
2. **CSRF Errors**:
   - Ensure `{% csrf_token %}` is included in all forms and AJAX requests.
3. **Fetch Request Fails**:
   - Check the browser Network tab for detailed error diagnostics.
   - Verify the backend URL (`"/"` or `"/chatbot/"`) matches the fetch request.
4. **Database Issues**:
   - Apply migrations using `python manage.py migrate`.

---

## **🤝 Contributing**

Contributions are welcome! 🌟 If you want to report bugs 🐞, request new features ✨, or contribute code 💻, please follow these steps:
1. Fork the repository.
2. Create a new branch (`feature/my-new-feature`).
3. Commit your changes.
4. Push the branch and create a pull request.

---


## **📧 Contact**

For any queries or support, please contact:
- **Name**: Rakesh
- **Email**: sprakesh4114@gmail.com
- **GitHub**: [krakesh1309](https://github.com/krakesh1309)

---

Let me know if you'd like additional changes or tweaks! This should really stand out now! 🚀✨
