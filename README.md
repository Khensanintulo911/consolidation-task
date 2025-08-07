# Django Poll App – Math Voting Platform

This project is a Django-based web application that allows users to vote on math-related questions and view poll results instantly. It was built as part of the "Introduction to Software Engineering" course.

## 🎯 Purpose

The goal of this project is to practice working with Django views, templates, models, and routing. It showcases the full flow of a poll system — from listing questions, capturing votes, and displaying results — using a dynamic backend and responsive frontend.

---

## 🚀 Features

- View a list of available poll questions
- Vote on a selected question
- Get immediate feedback via a results page
- Friendly error messages for missing input
- Clean and responsive Bootstrap-based layout

---

## 🧱 Project Structure

```bash
mysite/
│
├── polls/
│   ├── migrations/
│   ├── templates/
│   │   └── polls/
│   │       ├── base.html        # Shared layout for all templates
│   │       ├── index.html       # Homepage with question list
│   │       ├── detail.html      # Question detail + voting form
│   │       ├── results.html     # Voting results
│   ├── models.py                # Question & Choice models
│   ├── views.py                 # Application logic
│   ├── urls.py                  # App routing
│
├── manage.py
├── db.sqlite3
└── README.md
