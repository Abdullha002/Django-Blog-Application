# BlogMian

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-green?logo=django)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**BlogMian** is a Django-based blogging application that allows users to read, create, and manage blog posts. The project includes role-based access for managers and editors, user authentication, category management, comments, and a dashboard to manage posts, users, and categories.

---

## Table of Contents
1. [Features](#features)
2. [Tech Stack](#tech-stack)
3. [Project Structure](#project-structure)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Screenshots](#screenshots)
7. [Contributing](#contributing)
8. [License](#license)

---

## Features

### Public Features
- Home page with featured and non-featured blog posts.
- View blog posts by category.
- Read a single blog post with comments.
- Search blogs by keywords.
- User registration and login/logout.

### Dashboard (Admin/Manager/Editor)
- Role-based dashboard:
  - **Manager**: Access to all blogs, categories, users, and comments.
  - **Editor**: Access to only their own blogs and comments.
- Manage Categories: Add, edit, and delete categories.
- Manage Posts: Add, edit, and delete blog posts.
- Manage Users: Add, edit, and delete users.
- Manage Comments: View and delete comments.

---

## Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (default Django)
- **Authentication:** Django inbuilt authentication system
- **Other Libraries:** Django forms, Django slugify

---

## Project Structure

```
BlogMian/
│
├── blogs/                 # Blog app
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── templates/
│       ├── blogs.html
│       ├── post_by_category.html
│       └── search.html
│
├── dashboard/             # Dashboard app
│   ├── views.py
│   ├── forms.py
│   └── templates/dashboards/
│       ├── dashboard.html
│       ├── categories.html
│       ├── add_categories.html
│       ├── posts.html
│       ├── add_post.html
│       └── users.html
│
├── BlogMian/              # Main app
│   ├── views.py
│   └── templates/
│       ├── home.html
│       ├── auth/login.html
│       └── auth/register.html
│
├── manage.py
├── db.sqlite3
└── requirements.txt
```

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/BlogMian.git
cd BlogMian
```

2. **Create a virtual environment**

```bash
python -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate      # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create a superuser (admin)**

```bash
python manage.py createsuperuser
```

6. **Run the server**

```bash
python manage.py runserver
```

7. Open `http://127.0.0.1:8000/` in your browser.

---

## Usage

- Register a new user or login with existing credentials.
- Access the dashboard if you are a manager or editor.
- Add categories, create blog posts, and manage users and comments from the dashboard.
- Public users can read blogs, comment, and search posts.

---

## Screenshots

*Add screenshots of your application here, for example:*

- Home Page
- Dashboard
- Add Post Page
- Blog Details Page

---

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeature`
3. Make your changes.
4. Commit your changes: `git commit -m 'Add new feature'`
5. Push to the branch: `git push origin feature/YourFeature`
6. Create a pull request.

---

## License

This project is licensed under the MIT License.

