# Secure Backend API with Role-Based Access Control (RBAC)

This project implements a secure and scalable REST API with authentication, role-based access control, and CRUD functionality.  
It also includes a basic frontend interface to interact with the APIs.

This assignment was developed as part of the **Backend Developer Intern task**.

---

# Features

## Authentication
- User registration
- User login
- Password hashing using bcrypt
- JWT-based authentication

## Role-Based Access Control
- Two roles:
  - **User**
  - **Admin**
- Admin routes are protected using role middleware

## CRUD API
Example entity: **Tasks**

Operations supported:

- Create task
- Read tasks
- Update task
- Delete task

Only authenticated users can perform operations.

---

# Tech Stack

Backend
- Node.js
- Express.js
- MongoDB
- JWT Authentication
- bcrypt password hashing

Frontend
- Simple UI (React / Vanilla JS depending on your implementation)

Tools
- Postman for API testing
- dotenv for environment variables

---

# Project Structure


secure-backend-api-rbac
│
├── controllers
├── middleware
│ ├── authMiddleware.js
│ └── roleMiddleware.js
│
├── models
│ ├── User.js
│ └── Task.js
│
├── routes
│ ├── authRoutes.js
│ └── taskRoutes.js
│
├── config
│ └── db.js
│
├── server.js
└── package.json


---

# API Endpoints

## Authentication

### Register

POST /api/v1/auth/register


### Login

POST /api/v1/auth/login


Returns a **JWT token**.

---

## Task APIs

### Get Tasks

GET /api/v1/tasks


### Create Task

POST /api/v1/tasks


### Update Task

PUT /api/v1/tasks/:id


### Delete Task

DELETE /api/v1/tasks/:id


---

# Security Practices

- Password hashing with **bcrypt**
- **JWT authentication middleware**
- **Role-based authorization**
- Input validation
- Environment variables for secrets

---

# Setup Instructions

## 1 Clone the repository


git clone https://github.com/ravimnm/secure-backend-api-rbac.git

cd secure-backend-api-rbac


## 2 Install dependencies


npm install


## 3 Configure environment variables

Create a `.env` file:


PORT=5000
MONGO_URI=your_database_connection
JWT_SECRET=your_secret_key


## 4 Run the server


npm start


Server will start at:


http://localhost:5000


---

# API Testing

You can test the APIs using:

- **Postman**
- **curl**
- or the included frontend interface

---

# Scalability Notes

This backend follows a **modular architecture** to allow easy scaling.

Future improvements:

- Redis caching
- Docker deployment
- Microservice architecture
- API rate limiting
- Centralized logging

---

# Author

Ravi Sankar  
GitHub: https://github.com/ravimnm
