# MyShop - Django Web Application

A Django-based e-commerce web application built as a BCT college project.

## Features

- Product listing page with cards
- Product detail page
- About Us page
- Contact page with Feedback Form
- Bootstrap 5 responsive UI
- Django Admin panel

## Tech Stack

- Python
- Django
- Bootstrap 5
- HTML & CSS
- SQLite Database
- Font Awesome Icons

## Pages

| Page | URL | Description |
|------|-----|-------------|
| Home | `/` | Hero banner with features |
| Products | `/newApp/` | All products listing |
| Product Detail | `/newApp/product/<id>/` | Single product details |
| About | `/newApp/about/` | About Us page |
| Contact | `/newApp/contact/` | Contact & Feedback form |
| Admin | `/admin/` | Django admin panel |

## Extra Feature

**Feedback Form** — Users can submit their name, email, subject and message through the Contact page. All feedback is saved to the database and visible in the Django Admin panel.

## How to Run

**Step 1 — Clone the repository**
```
git clone https://github.com/NehaTanti-afk/MyShop-BCT-Project.git
```

**Step 2 — Go to project folder**
```
cd MyShop-BCT-Project/myWebsite
```

**Step 3 — Install Django**
```
pip install django pillow
```

**Step 4 — Run migrations**
```
python manage.py migrate
```

**Step 5 — Create admin user**
```
python manage.py createsuperuser
```

**Step 6 — Run the server**
```
python manage.py runserver
```

**Step 7 — Open in browser**
```
http://127.0.0.1:8000/newApp/
```

## Project Structure

```
MyShop-BCT-Project/
│
└── myWebsite/
    ├── manage.py
    ├── myWebsite/          # Project settings
    │   ├── settings.py
    │   ├── urls.py
    │   └── views.py
    ├── newApp/             # Main app
    │   ├── models.py       # Product, Feedback models
    │   ├── views.py        # Page logic
    │   ├── urls.py         # URL routes
    │   ├── admin.py        # Admin panel
    │   └── templates/      # HTML pages
    ├── static/
    │   └── style.css       # Custom styles
    └── templates/
        ├── index.html      # Home page
        └── website/
            └── layout.html # Base template
```

## Student Info

- **Name:** Neha Tanti
- **GitHub:** [NehaTanti-afk](https://github.com/NehaTanti-afk)
- **Project:** BCT Django Assignment
