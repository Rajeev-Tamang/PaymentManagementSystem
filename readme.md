# 🚀 Django & Tailwind CSS Installation Guide

A step-by-step guide to set up Django with Tailwind CSS for modern web development.

<div align="center">

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

</div>

## 📋 Table of Contents

- [Prerequisites](#-prerequisites)
- [Virtual Environment Setup](#-virtual-environment-setup)
- [Django Installation](#-django-installation)
- [Project Setup](#-project-setup)
- [Tailwind CSS Integration](#-tailwind-css-integration)
- [Development Server](#-development-server)
- [Tips & Troubleshooting](#-tips--troubleshooting)

## 🎯 Prerequisites

Before starting, ensure you have:
- Python 3.8+ installed
- Node.js 14+ installed (required for Tailwind)
- Basic knowledge of Django

## 🔧 Virtual Environment Setup

### 1. Create Virtual Environment
```bash
# Create virtual environment
virtualenv env
# 💡 Note: 'env' is the environment name - you can customize it!
```

### 2. Activate Virtual Environment
```bash
# On Linux/Mac
source env/bin/activate

# On Windows
env\Scripts\activate
```

> ✅ **Success Indicator**: Your terminal prompt should show `(env)` at the beginning

## 📦 Django Installation

### 1. Install Django
```bash
pip install django
```

### 2. Verify Installation
```bash
pip freeze
```

### 3. Install Additional Packages
```bash
# For image handling
pip install pillow
```

## 🏗️ Project Setup

### 1. Create Django Project
```bash
django-admin startproject project .
# 💡 The '.' creates the project in current directory
```

### 2. Create Django App
```bash
django-admin startapp app
```

### 3. Database Setup
```bash
# Apply initial migrations
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser
```bash
python manage.py createsuperuser
```

### 5. Test Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000` to see the Django welcome page! 🎉

## 🎨 Tailwind CSS Integration

### Step 1: Install Django-Tailwind
```bash
pip install django-tailwind
```

### Step 2: Update Settings
Add `tailwind` to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    # ... other Django apps
    'tailwind',
]
```

### Step 3: Initialize Tailwind Theme
```bash
python manage.py tailwind init
```

This creates a `theme` app with Tailwind configuration! 🎨

### Step 4: Register Theme App
Update `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    # ... other Django apps
    'tailwind',
    'theme',  # ← Add this line
]
```

### Step 5: Configure Tailwind App
Add this line to `settings.py`:

```python
TAILWIND_APP_NAME = 'theme'
```

### Step 6: Install Dependencies
```bash
python manage.py tailwind install
```

> ⏳ This might take a few minutes as it installs Node.js dependencies

## 🚀 Development Server

### Option 1: Django + Tailwind (Recommended)
```bash
python manage.py tailwind dev
```

This command:
- ✅ Starts Django development server
- ✅ Watches Tailwind files for changes
- ✅ Auto-compiles CSS on save

### Option 2: Separate Commands
```bash
# Terminal 1 - Django server
python manage.py runserver

# Terminal 2 - Tailwind watcher
python manage.py tailwind watch
```

## 📁 Project Structure

After setup, your project should look like:

```
your-project/
├── env/                    # Virtual environment
├── project/               # Django project
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── app/                   # Your Django app
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── theme/                 # Tailwind theme app
│   ├── static/
│   ├── templates/
│   └── static_src/
└── manage.py
```

## 🎯 Quick Test

Create a simple template to test Tailwind:

**`app/templates/app/index.html`**
```html
<!DOCTYPE html>
<html>
<head>
    {% load static tailwind_tags %}
    {% tailwind_css %}
    <title>Django + Tailwind</title>
</head>
<body class="bg-blue-500">
    <div class="container mx-auto p-8">
        <h1 class="text-4xl font-bold text-white text-center">
            🎉 Django + Tailwind CSS Works!
        </h1>
        <p class="text-white text-center mt-4">
            If you see this styled page, everything is working perfectly!
        </p>
    </div>
</body>
</html>
```

## 💡 Tips & Troubleshooting

### 🔥 Pro Tips
- Always activate your virtual environment before working
- Use `python manage.py tailwind dev` for the best development experience
- Keep Node.js and npm updated for better performance

### 🐛 Common Issues

**Issue**: `tailwind` command not found
```bash
# Solution: Ensure tailwind is in INSTALLED_APPS
# and TAILWIND_APP_NAME is set correctly
```

**Issue**: Styles not updating
```bash
# Solution: Restart the tailwind dev server
python manage.py tailwind dev
```

**Issue**: Node.js errors
```bash
# Solution: Update Node.js to latest LTS version
# Clear node_modules and reinstall
python manage.py tailwind install
```

## 🎊 What's Next?

Now you have Django with Tailwind CSS ready! You can:

- 🎨 Create beautiful, responsive designs
- ⚡ Enjoy lightning-fast development
- 🔄 See changes instantly with hot reload
- 📱 Build mobile-first applications

## 📚 Useful Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [Django-Tailwind GitHub](https://github.com/timonweb/django-tailwind)

---

