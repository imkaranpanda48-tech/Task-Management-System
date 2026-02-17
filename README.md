# 🚀 Task Management System

A role-based Task Management System built using Django, Django REST Framework, JWT Authentication, and Bootstrap.
The system supports Admin/Manager and Employee roles with separate dashboards and secure APIs.

---

# 📌 Features
🔐 Authentication & Authorization

- Django session-based authentication for HTML dashboards

- JWT authentication for REST APIs

- Role-based access control (Admin / Manager / Employee)

---

# 📋 Task Management

- Create, assign, update, and delete tasks (Admin/Manager)

- View assigned tasks (Employee)

- Update task status (Pending / Completed)

- Task deadline management

---

# 🖥 Dashboards

- Admin / Manager dashboard

- Employee dashboard

- Logout functionality

---

# 🔗 REST APIs

- Secure APIs built using Django REST Framework

---

# 🧰 Tech Stack
- Layer	Technology
- Backend	Django, Django REST Framework
- Authentication	JWT, Django Sessions
- Frontend	HTML, CSS, Bootstrap
- Database	SQLite
- API Testing	Thunder Client / Postman

- Protected using JWT

- Tested using Thunder Client / Postman

---


# 🔑 Authentication Flow
- HTML (Browser)

- Django session authentication

- Used for dashboards and forms

- API

- JWT authentication

- Access token required in headers:

- Authorization: Bearer <access_token>

---



# 📁 Project Structure

- task-management-system/
  │
- ├── accounts/         -  # Authentication & user roles
- ├── tasks/            -  # Task management app
- ├── templates/         - # HTML templates
     ├──login.html     -  #all html files
    
- ├── manage.py
- └── README.md



---

## 📸 Screenshots

### 🔐 Login Page
![Login Page]
<img width="1865" height="992" alt="login" src="https://github.com/user-attachments/assets/9a692f9d-41b8-42af-9cec-3475b920566f" />


### 🧑‍💼 Admin / Manager Dashboard
<img width="1920" height="1080" alt="manager _dashboared" src="https://github.com/user-attachments/assets/6444a259-fece-4673-9799-5d335be565b4" />


### 📌 Assign Task  (only manager/admin )
<img width="1920" height="1080" alt="assign" src="https://github.com/user-attachments/assets/bf343ce0-3aa7-443d-a85b-005a26cf2e8e" />


### 🧑‍💻 Add Employee (only manager/admin)
<img width="1920" height="1080" alt="add" src="https://github.com/user-attachments/assets/528f3277-3385-466e-995e-5db0e8a5e200" />


### 👨‍💻 Employee Dashboard (view task and mark)
<img width="1920" height="1080" alt="employee_dashboared" src="https://github.com/user-attachments/assets/d851e5d6-630d-477a-a631-7af7be5de267" />


### 💻 API 
<img width="1920" height="1080" alt="api root" src="https://github.com/user-attachments/assets/cf787deb-35c4-478b-9ea9-e9fd2509b600" />

- go to api/token to get authentiction token to access copy it through Thunder Client / Postman using POST
- and test on thunder client/postman to get user task assigned projects 


