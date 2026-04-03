# 🎓 Student Management System API

A **Student Management System** backend project built using **Django** and **Django REST Framework (DRF)**.  
This project provides REST APIs to manage **Students**, **Courses**, and **Attendance**, with secure **JWT Authentication** and interactive **Swagger API Documentation**.

---

## 🚀 Features
- JWT Authentication (Login / Refresh Token)
- Student CRUD (Create, Read, Update, Delete)
- Course CRUD (Create, Read, Update, Delete)
- Attendance Management System
- Role-based Permissions (Admin / Teacher)
- Swagger UI Documentation using `drf-spectacular`
- Search, Filtering and Ordering Support (Optional)

---

## 🛠 Tech Stack
- Python
- Django
- Django REST Framework
- SimpleJWT (JWT Authentication)
- MySQL (Local Database)
- PostgreSQL (Deployment Ready)
- drf-spectacular (Swagger Documentation)

---

## 📂 Project Modules
- **Students Module** → Manage student details
- **Courses Module** → Manage courses and subjects
- **Attendance Module** → Mark and track attendance

---

## 🔑 Authentication (JWT)
This API uses JWT tokens for secure authentication.

### Get Access Token
- Login endpoint returns **Access Token** and **Refresh Token**
- Use the Access Token in API requests:

```http
Authorization: Bearer <your_access_token>