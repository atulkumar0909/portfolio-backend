from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'change-this-in-production-use-env-var')
DEBUG = False

ALLOWED_HOSTS = [
    "web-production-8fa5c.up.railway.app",
] # Restrict to your domain in production

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third party
    'rest_framework',
    'corsheaders',
    # Local
    'contact',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Must be first
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio_backend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ── REST Framework ────────────────────────────────────────────────────────────
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': ['rest_framework.renderers.JSONRenderer'],
    'DEFAULT_THROTTLE_CLASSES': ['rest_framework.throttling.AnonRateThrottle'],
    'DEFAULT_THROTTLE_RATES': {'anon': '10/hour'},  # Prevent spam
}

# ── CORS — allow your portfolio frontend ─────────────────────────────────────
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5500",   # Live Server (VS Code)
    "http://127.0.0.1:5500",
    "http://localhost:3000",  # React dev server
    "https://portfolio-bay-tau-98.vercel.app", 
    # "https://yourportfolio.com",  # Add your live domain here
]
CORS_ALLOW_ALL_ORIGINS = DEBUG  # Allow all in dev, restrict in production

# ── Email via Gmail SMTP ──────────────────────────────────────────────────────
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'atulkumargupta7654@gmail.com'
EMAIL_HOST_PASSWORD = 'bipp ujoc azde ufby'   # your 16-char app password
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# ── Your email — where contact notifications land ─────────────────────────────
CONTACT_RECEIVER_EMAIL = os.environ.get('CONTACT_RECEIVER_EMAIL', 'atulkumargupta7654@gmail.com')

# ── Simple admin secret for viewing messages via API ─────────────────────────
ADMIN_SECRET_KEY = os.environ.get('ADMIN_SECRET_KEY', 'change-this-secret-key')

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
