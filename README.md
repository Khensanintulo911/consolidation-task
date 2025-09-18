# Django Math Voting Platform & Blog System

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)

A consolidated Django project featuring:
- Math poll voting system
- Blog functionality
- User authentication
- Sphinx documentation
- Docker support

## 🌟 Key Features

### 🧮 Math Voting Platform
- View available math poll questions
- Vote on selected questions
- Instant results visualization
- Responsive Bootstrap interface
- Form validation with friendly errors

### ✍️ Blog System
- Create and manage blog posts
- User authentication system
- Admin dashboard
- Database models for content

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Docker (optional)
- Git

### 📦 Installation

#### With Virtual Environment
```bash
git clone https://github.com/Khensanintulo911/consolidation-task.git
cd consolidation-task

python -m venv venv
source venv/bin/activate  # Linux/MacOS
.\venv\Scripts\activate   # Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver