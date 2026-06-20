# 📚 Study Tracker

A personal study management application built with Django that helps users track daily study progress, maintain study notes, upload study-related images, and monitor learning progress through a dashboard and calendar interface.

---

## 🚀 Features

### 👤 User Authentication

* User Registration (Sign Up)
* User Login
* User Logout
* Session-based Authentication
* Protected Routes using Django Authentication

---

### 📅 Calendar-Based Study Tracking

* View study records in a monthly calendar format
* Navigate between previous and next months
* Highlight study entries for specific dates
* Organized study history by date

---

### 📝 Study Entry Management

Users can:

* Create study entries
* Edit existing entries
* Delete study entries
* View detailed study records

Each study entry contains:

| Field       | Description              |
| ----------- | ------------------------ |
| Topic       | Study topic name         |
| Study Date  | Date of study            |
| Progress    | Completion percentage    |
| Description | Detailed study content   |
| Notes       | Additional notes         |
| Created At  | Auto-generated timestamp |

---

### ✨ Rich Text Editor Support

The project uses **Django CKEditor** for:

* Study Description
* Study Notes

Users can format content with:

* Bold
* Italic
* Underline
* Lists
* Links
* Headings

---

### 🖼️ Image Upload Support

Users can upload multiple images related to study entries.

Examples:

* Notes screenshots
* Project screenshots
* Diagrams
* Learning materials

Features:

* Multiple image uploads
* Image deletion
* Entry-wise image organization

---

### 📊 Dashboard

Dashboard provides:

* List of all study entries
* Overall study progress calculation
* Quick learning overview

Progress is calculated as:

Overall Progress = Sum of Progress Values / Total Entries

Example:

Entry 1 = 80%

Entry 2 = 60%

Entry 3 = 100%

Overall = (80 + 60 + 100) / 3 = 80%

---

## 🏗️ Tech Stack

### Backend

* Python
* Django 6.0.3

### Frontend

* HTML5
* CSS3
* Bootstrap

### Database

* SQLite (Default)

### Rich Text Editor

* Django CKEditor

### Image Processing

* Pillow

---

## 📦 Requirements

```txt
asgiref==3.11.1
Django==6.0.3
django-ckeditor==6.7.3
django-js-asset==3.1.2
pillow==12.1.1
sqlparse==0.5.5
tzdata==2025.3
```

---

## 📂 Project Structure

```text
study_tracker/
│
├── tracker/
│   ├── migrations/
│   ├── templates/
│   │   └── tracker/
│   │       ├── login.html
│   │       ├── signup.html
│   │       ├── calendar.html
│   │       ├── add_study.html
│   │       ├── edit_study.html
│   │       ├── detail.html
│   │       ├── dashboard.html
│   │       └── delete_confirm.html
│   │
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
│
├── media/
├── static/
├── manage.py
└── requirements.txt
```

---

## 🗄️ Database Models

### StudyEntry

```python
class StudyEntry(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    topic = models.CharField(max_length=200)

    study_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    progress = models.IntegerField()

    description = RichTextField()

    notes = RichTextField()
```

### StudyImage

```python
class StudyImage(models.Model):

    entry = models.ForeignKey(
        StudyEntry,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image = models.ImageField(
        upload_to="study_images/"
    )
```

---

## 🔐 Authentication Flow

### Signup

User creates account using:

* Username
* Password
* Confirm Password

After successful registration:

```python
login(request, user)
```

User is automatically logged in.

---

### Login

Authentication is performed using:

```python
authenticate(
    request,
    username=username,
    password=password
)
```

Authenticated users are redirected to:

```python
calendar
```

---

### Logout

```python
logout(request)
```

User session is destroyed and redirected to login page.

---

## 📅 Calendar Workflow

1. User opens calendar page
2. Current month is loaded
3. Study entries are filtered by:

```python
study_date__year
study_date__month
```

4. Calendar is generated using:

```python
calendar.monthcalendar()
```

5. User can move to:

* Previous month
* Next month

---

## 📝 Add Study Entry Workflow

1. User clicks Add Study
2. Fills study form
3. Uploads images
4. Form validation occurs
5. Study entry is saved
6. Images are attached to entry
7. User redirected to calendar

---

## 🖼️ Image Upload Workflow

```python
files = request.FILES.getlist('images')
```

For each uploaded file:

```python
StudyImage.objects.create(
    entry=entry,
    image=f
)
```

Images are stored inside:

```text
media/study_images/
```

---

## 📊 Dashboard Workflow

Dashboard calculates overall progress:

```python
entries = StudyEntry.objects.filter(
    user=request.user
)

total = sum(e.progress for e in entries)

count = entries.count()

overall = total // count
```

Displayed information:

* Total Entries
* Progress Percentage
* Learning Overview

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/study-tracker.git
```

```bash
cd study-tracker
```

---

### Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Apply Migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

### Create Superuser

```bash
python manage.py createsuperuser
```

---

### Run Server

```bash
python manage.py runserver
```

Visit:

```text
http://127.0.0.1:8000/
```

---

## 🔧 Settings Configuration

### MEDIA Settings

```python
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

### URL Configuration

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
```

---

## 🔒 Security Features

* Login Required Decorators
* User-Specific Data Isolation
* Protected CRUD Operations
* Session Authentication
* CSRF Protection

Example:

```python
@login_required
def dashboard(request):
    ...
```

---

## 📈 Future Enhancements

* Search Study Entries
* Study Categories
* Tags
* Export to PDF
* Dark Mode
* Email Verification
* Monthly Statistics
* Charts & Graphs
* REST API Integration
* Mobile Responsive Enhancements

---

## 🎯 Learning Outcomes

This project demonstrates:

* Django Authentication
* Django Models
* ModelForms
* CRUD Operations
* File Uploads
* Rich Text Editors
* Calendar Integration
* User Authorization
* Dashboard Analytics
* Database Relationships

---

## 👨‍💻 Author

**Amal Saju**

Computer Science Graduate | Python Django Developer

GitHub: https://github.com/Amalsaju13/Study_Tracker
---

## 📄 License

This project is developed for educational and portfolio purposes.
