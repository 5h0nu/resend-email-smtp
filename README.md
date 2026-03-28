# 📧 Simple Mailer API | @5h0nu

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Resend-000000?style=for-the-badge&logo=resend&logoColor=white" alt="Resend" />
  <a href="https://github.com/5h0nu/resend-email-smtp/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/MIT-License-green?style=for-the-badge" alt="License" />
  </a>
</p>

---

### 📝 Project Overview
A lightweight **FastAPI-based** broadcast system designed to send high-speed emails using the **Resend API**. This tool is optimized for developers who need a simple, no-fuss way to send notifications, scholarship alerts, or student updates.

### 🚀 Key Features
* **Lightning Fast**: Built on an asynchronous Python stack (FastAPI + HTTPX).
* **Privacy Protected**: Automatic **BCC Support** ensures recipients never see each other's email addresses.
* **Auto-Docs**: Includes built-in interactive testing via Swagger UI at `/docs`.
* **Simplified Logic**: No complex databases or templates required—just send and go.

---

### 🛠️ Setup & Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/5h0nu/simple-mailer-api.git](https://github.com/5h0nu/simple-mailer-api.git)
    cd simple-mailer-api
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure API Key:**
    Create an environment variable named `RESEND_API_KEY` or replace the placeholder directly in `main.py`.

4.  **Launch the API:**
    ```bash
    python main.py
    ```

---

### 📩 API Usage Guide

Once the server is running, send a **POST** request to `/send-email`.

**Request Body (JSON):**
```json
{
  "to": ["student1@example.com", "student2@example.com"],
  "subject": "Important Academic Update",
  "message": "Hello! This is a broadcast message sent via Shonu's Mailer API."
}
 ```
### 📬 Connect with Me

<p align="center">
  <a href="https://instagram.com/5h0nu" target="_blank">
    <img src="https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white" alt="Instagram" />
  </a>
  <a href="https://threads.net/@5h0nu" target="_blank">
    <img src="https://img.shields.io/badge/Threads-000000?style=for-the-badge&logo=Threads&logoColor=white" alt="Threads" />
  </a>
  <a href="mailto:mdkhasimgs@gmail.com">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
  </a>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=5h0nu&color=purple&style=flat-square&label=PROFILE+VIEWS" alt="Profile Views" />
</p>
