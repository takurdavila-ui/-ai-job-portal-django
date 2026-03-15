# AI-Powered Job Portal (Django)

A full-stack **Job Portal Web Application** built using Django and Python, featuring an **AI-based job recommendation system** that suggests jobs to candidates based on their skills. The portal supports **candidates, employers, and admin functionalities**.

---

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Future Improvements](#future-improvements)
- [Author](#author)

---

## Features

### Candidate Features
- User authentication (Login / Logout)
- Browse jobs with **search** and **location filter**
- View job details
- Apply to jobs with **resume upload**
- Prevent duplicate applications
- View applied jobs (**My Applications**)
- **AI Recommended Jobs** based on user skills
- Save jobs for later (future feature)

### Employer Features
- Employer login and authentication
- Post new jobs
- View jobs posted
- View applicants per job
- Accept / Reject applications
- Dashboard showing **applicant count per job**

### Admin Features
- Manage **users, companies, jobs, applications, profiles**
- Full CRUD operations for jobs and companies

---

## Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Django Templates
- **Database:** SQLite
- **AI/ML Feature:** TF-IDF + Cosine Similarity for job recommendation (`scikit-learn`)
- **File Uploads:** Resume uploads via Django FileField

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/<your-username>/ai-job-portal.git
cd ai-job-portal

# Clone repo
git clone https://github.com/<username>/ai-job-portal.git
cd ai-job-portal

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows PowerShell
venv\Scripts\Activate.ps1
# Linux / Mac
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver

#Admin Panel
Access via: http://127.0.0.1:8000/admin/

Add Companies, Jobs, and User Profiles (skills).

#Candidate

Login → Browse jobs → Apply → View recommended jobs

Recommended jobs are generated using TF-IDF similarity between candidate skills and job skills.

#Employer

Login → Post jobs → View applicants → Accept/Reject applications

Dashboard shows number of applicants per job.

#AI Recommended Jobs

Candidate skills are compared with job required skills

Top matching jobs are displayed in Recommended Jobs page

#Screenshorts
-Home Page
-Job Listing Page
-Job Detail Page
-Apply Job Page
-My Applications Page
-Employer Dashboard
-View Applicants
-Accept / Reject Application
-Admin Panel
-AI Recommended Jobs Page 

#Future Improvements
-Resume download option for employers

-Pagination for job listings

-Mobile responsive UI

-Saved jobs feature

-Advanced AI recommendations using machine learning

-LinkedIn/Naukri-like suggested jobs and notifications

#Author

Devisri Thakur

BTech Student | AI & Web Development Enthusiast

Email: [takurdavila@gmail.com]

GitHub: https:https://github.com/takurdavila-ui

## License

This project is licensed under the MIT License.
