# Job Board Backend API

A robust, production-ready REST API for a Job Board platform connecting Employers and Job Seekers. Built with Django Rest Framework, this system handles job postings, applications with resume uploads, and automated email notifications.

**🚀 Live Demo:** [Insert Your Vercel URL Here]  
**📚 API Documentation:** [Insert Your Vercel URL Here]/swagger/

---

## 🔥 Features

### 🔐 Authentication & Users
* **Custom User Model:** Distinct roles for **Employers** and **Job Seekers**.
* **JWT Authentication:** Secure access using Access and Refresh tokens.
* **Email Verification:** Account activation via email link.

### 💼 Job Management
* **CRUD Operations:** Employers can create, update, and delete their job posts.
* **Public Search:** Anyone can filter jobs by Category, Location, and Type.
* **Pagination:** Efficient listing handling.

### 📄 Application System
* **Resume Upload:** Integrated with **Cloudinary** for secure file storage.
* **Role-Based Access:** * Seekers can only view their own applications.
    * Employers can only view applicants for *their* jobs.
* **Duplicate Prevention:** Seekers cannot apply to the same job twice.

### 🔔 Notifications
* **Automated Emails:**
    * **New Application:** Notifies Employer (new applicant) and Seeker (confirmation).
    * **Status Update:** Notifies Seeker when their application status changes (e.g., "Accepted").

### 🛠 Technical Highlights
* **Documentation:** Interactive Swagger UI & Redoc.
* **Production Ready:** Configured for Vercel (Serverless) with PostgreSQL.
* **Static Files:** Served efficiently via Whitenoise.

---

## 🛠️ Tech Stack

* **Backend:** Python 3.9+, Django 4.2, Django Rest Framework
* **Database:** PostgreSQL (Production), SQLite (Local Dev)
* **Storage:** Cloudinary (Media/Resumes)
* **Authentication:** `djangorestframework-simplejwt`
* **Docs:** `drf-yasg`
* **Deployment:** Vercel

---

## 🚀 Getting Started

### Prerequisites
* Python 3.8 or higher
* Git
* A Cloudinary Account (for resume uploads)
* A Gmail Account (for email notifications)

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/job-board-backend.git](https://github.com/your-username/job-board-backend.git)
cd job_board_backend
