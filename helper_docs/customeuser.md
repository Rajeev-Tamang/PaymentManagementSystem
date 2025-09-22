# Django Custom User Model Guide

A comprehensive guide to creating custom user models in Django with two different approaches.

## Table of Contents

- [Overview](#overview)
- [Method 1: Using AbstractUser](#method-1-using-abstractuser)
- [Method 2: Using AbstractBaseUser](#method-2-using-abstractbaseuser)
- [Summary](#summary)
- [Installation](#installation)

## Overview

Django provides two main ways to customize the default User model:

1. **AbstractUser** - Extends the default user model with additional fields
2. **AbstractBaseUser** - Creates a completely custom user model from scratch

## Method 1: Using AbstractUser

✅ **Recommended for**: Adding extra fields to the default User model (e.g., age, phone number)

### Step 1: Create Custom User Model

**`accounts/models.py`**
```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.username
```

### Step 2: Configure Admin

**`accounts/admin.py`**
```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('age', 'phone_number')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
```

### Step 3: Update Settings

**`settings.py`**
```python
AUTH_USER_MODEL = 'accounts.CustomUser'
```

### Step 4: Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## Method 2: Using AbstractBaseUser

✅ **Recommended for**: Complete control over user fields and authentication behavior

### Step 1: Create Custom User Model

**`accounts/models.py`**
```python
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email
```

### Step 2: Configure Admin

**`accounts/admin.py`**
```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

class CustomUserAdmin(BaseUserAdmin):
    ordering = ['email']
    list_display = ['email', 'name', 'is_staff']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
```

### Step 3: Update Settings

**`settings.py`**
```python
AUTH_USER_MODEL = 'accounts.CustomUser'
```

### Step 4: Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## Summary

| Method | Use Case | Setup Complexity |
|--------|----------|------------------|
| **AbstractUser** | Need to add extra fields to default user model | ⭐ Low |
| **AbstractBaseUser** | Need complete control over user authentication | ⭐⭐⭐ High |

## Installation

1. Create a Django app for accounts:
   ```bash
   python manage.py startapp accounts
   ```

2. Add the app to your `INSTALLED_APPS` in `settings.py`:
   ```python
   INSTALLED_APPS = [
       # ... other apps
       'accounts',
   ]
   ```

3. Follow one of the methods above
4. Create and apply migrations
5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

## 🔧 Tips

- Always set `AUTH_USER_MODEL` **before** your first migration
- If you're starting a new project, implement custom user model from the beginning
- For existing projects with data, migrating to a custom user model can be complex

## 📚 Additional Resources

- [Django Official Documentation - Customizing authentication](https://docs.djangoproject.com/en/stable/topics/auth/customizing/)
- [Django Best Practices for Custom User Models](https://learndjango.com/tutorials/django-custom-user-model)

---

