# Image Upload Process in Django

This document outlines the complete process for implementing image uploads in Django using `forms.Form` (not ModelForm).

## 📋 Requirements Checklist

### 1. **Settings Configuration** (`settings.py`)

```python
# Media files configuration
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Custom user model (if using)
AUTH_USER_MODEL = 'accounts.CustomUser'
```

### 2. **URL Configuration** (`main_project/urls.py`)

```python
from django.conf import settings
from django.conf.urls.static import static

# Add this at the end of urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### 3. **Model Setup** (`models.py`)

```python
from django.db import models

class CustomUser(AbstractUser):
    # other fields...
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
```

### 4. **Form Configuration** (`forms.py`)

```python
from django import forms
from .models import CustomUser

class SchoolAdminRegistrationForm(forms.Form):
    # Regular fields...
    profile_pic = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'input-file w-full p-2'}), 
        required=False
    )

    def clean(self):
        cleaned_data = super().clean()
        # validation logic
        return cleaned_data

    def save(self, commit=True):
        user = CustomUser(
            # other fields...
            profile_pic=self.cleaned_data.get('profile_pic')  # Use .get() for optional fields
        )
        if commit:
            user.save()
        return user
```

### 5. **Template Configuration** (`register.html`)

**🚨 CRITICAL**: Must include `enctype="multipart/form-data"`

```html
<form action="" method="post" enctype="multipart/form-data" class="w-[600px] flex flex-col">
    {% csrf_token %}
    <!-- form fields -->
    {% for field in form %}
        <fieldset class="fieldset">
            <legend class="fieldset-legend">{{field.label}}</legend>
            {{field}}
            {% for error in field.errors %}
                <div class="alert alert-error alert-soft"><span>{{error}}</span></div>
            {% endfor %}
        </fieldset>
    {% endfor %}
    <button class="btn btn-primary" type="submit">Register</button>
</form>
```

### 6. **View Configuration** (`views.py`)

**🚨 CRITICAL**: Must pass both `request.POST` and `request.FILES`

```python
from django.shortcuts import render, redirect
from .forms import SchoolAdminRegistrationForm

def school_admin_register(request):
    if request.method == 'POST':
        # MUST include request.FILES for file uploads
        form = SchoolAdminRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('success_page')
    else:
        form = SchoolAdminRegistrationForm()
    
    return render(request, 'accounts/register.html', {'form': form})
```

## ⚠️ Common Issues & Solutions

### Issue 1: Image not saving to database
**Solution**: Ensure `enctype="multipart/form-data"` is in the form tag

### Issue 2: `request.FILES` is empty
**Solution**: Pass `request.FILES` to form constructor in view

### Issue 3: File field validation errors
**Solution**: Use `.get()` method for optional fields in form's save method

### Issue 4: Media files not serving in development
**Solution**: Add static URL configuration in main `urls.py`

## 🔄 Complete Flow

1. **User uploads file** → Browser sends multipart data (due to `enctype`)
2. **Django receives request** → Separates POST data and FILES data
3. **View processes request** → Passes both `request.POST` and `request.FILES` to form
4. **Form validates data** → Includes file validation
5. **Form saves data** → Creates model instance with file
6. **Django saves file** → Stores file in `MEDIA_ROOT/upload_to/` directory
7. **Database stores path** → Saves file path in database field

## 📁 File Storage Structure

```
project/
├── media/
│   └── profile_pics/
│       ├── user1_profile.jpg
│       └── user2_profile.png
├── static/
└── db.sqlite3
```

## 🧪 Testing Checklist

- [ ] Form renders file input field
- [ ] File uploads without errors
- [ ] File is saved to correct directory
- [ ] Database stores file path
- [ ] File can be accessed via URL
- [ ] Validation works for file size/type (if implemented)

## 📝 Notes

- Always use `enctype="multipart/form-data"` for file uploads
- Always pass `request.FILES` to form constructor
- Use `.get()` for optional file fields in form save method
- Configure media settings properly for file serving

project/
- media/
  - profile_pics/
    - user1_profile.jpg
    - user2_profile.png
- static/
- db.sqlite3