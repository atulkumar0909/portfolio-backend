# Portfolio Contact Backend — Django REST API

A clean Django backend that powers the contact form on Atul Kumar's portfolio.
Every submission is **saved to SQLite** and **emailed to your Gmail**.

---

## Project Structure

```
portfolio_backend/
├── contact/
│   ├── models.py        ← ContactMessage DB model
│   ├── serializers.py   ← Validation + serialization
│   ├── views.py         ← POST /api/contact/ logic
│   ├── urls.py          ← URL routing
│   └── admin.py         ← Django admin panel config
├── portfolio_backend/
│   ├── settings.py      ← All config (SMTP, CORS, etc.)
│   └── urls.py          ← Root URL config
├── contact_section.html ← Drop-in frontend HTML + JS
├── .env.example         ← Environment variable template
└── README.md
```

---

## Setup (Step by Step)

### 1. Install dependencies
```bash
pip install django djangorestframework django-cors-headers
```

### 2. Configure environment variables
```bash
cp .env.example .env
# Edit .env with your Gmail credentials
```

### 3. Get Gmail App Password
1. Go to your Google Account → **Security**
2. Enable **2-Step Verification**
3. Go to **App Passwords** → Select "Mail" → Generate
4. Paste the 16-char password into `.env` as `EMAIL_HOST_PASSWORD`

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Create admin user (to view messages in Django Admin)
```bash
python manage.py createsuperuser
```

### 6. Start the server
```bash
python manage.py runserver
```

---

## API Endpoints

### POST `/api/contact/`
Submit a contact message.

**Request body:**
```json
{
  "name": "Recruiter Name",
  "email": "recruiter@company.com",
  "message": "We'd love to discuss an opportunity with you!"
}
```

**Success response (201):**
```json
{
  "success": true,
  "message": "Thanks for reaching out! I'll get back to you soon."
}
```

**Validation error (400):**
```json
{
  "success": false,
  "errors": {
    "message": ["Message must be at least 10 characters."]
  }
}
```

---

### GET `/api/contact/messages/`
View all saved messages (admin only).

**Header required:**
```
X-Admin-Secret: your-secret-admin-key-here
```

---

## Django Admin Panel

Visit `http://127.0.0.1:8000/admin/` after creating a superuser.
You can view, search, and mark messages as read.

---

## Connecting to Your Portfolio HTML

1. Copy the contents of `contact_section.html` into your portfolio
2. Make sure the server is running on `http://127.0.0.1:8000`
3. When deploying, update `API_URL` in the JS to your live domain

---

## Deployment (Free Options)

| Platform | Notes |
|----------|-------|
| **Railway.app** | Easiest — connects GitHub, free tier available |
| **Render.com** | Free Django hosting, add env vars in dashboard |
| **PythonAnywhere** | Beginner-friendly, free tier |

When deploying:
- Set `DEBUG=False` in `.env`
- Add your live domain to `ALLOWED_HOSTS` in `settings.py`
- Add your portfolio URL to `CORS_ALLOWED_ORIGINS` in `settings.py`

---

## Rate Limiting
The API is throttled to **10 requests/hour per IP** to prevent spam.
Adjust in `settings.py` → `REST_FRAMEWORK → DEFAULT_THROTTLE_RATES`.
