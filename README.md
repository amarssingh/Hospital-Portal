# Hospital-Portal

This is a Django-based web portal designed to streamline the interaction between doctors and patients. It includes user authentication for two types of users (Doctors and Patients), personalized dashboards, and a blog system where doctors can publish articles categorized by medical topics.

## Features

### User System
- **Signup/Login** functionality for both Doctors and Patients.
- Redirects each user to a customized dashboard after login.
- User details are stored and displayed on the dashboard.

### Doctor Dashboard
- View profile details.
- Create and manage blog posts.
- Blog categories include:
  - Mental Health
  - Heart Disease
  - Covid19
  - Immunization
- Save posts as **Draft** or **Published**.

### Patient Dashboard
- View personal details.
- Browse published blog posts by category.
- Blog post summaries are truncated to 15 words for easy preview.

### Blog System
- Doctors can create posts with:
  - Title
  - Image
  - Category
  - Summary
  - Content
  - Draft Status
- Patients can only see published posts.
- Posts are filterable by category.

### Backend
- Built with **Django**
- Uses **MySQL** as the database backend

---

## Tech Stack

- **Backend:** Django (Python)
- **Database:** MySQL
- **Frontend:** HTML, CSS (Django templates)
- **Optional:** JavaScript framework/library for enhanced interactivity

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/hospital-portal.git
cd hospital-portal
```

### 2. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Run the Development Server
```bash
python manage.py runserver
```

---

## Folder Structure

```bash
hospital-portal/
│
├── accounts/          
├── blog/              
├── templates/
├── static/            
├── hospital_portal/  
├── manage.py
└── README.md
```
