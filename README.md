# Django

Learning the Django Web Framework

---

## 🚀 Creating a Django Project

To start a new Django project, use the following command:

```bash
django-admin startproject project_name
```

This will create a new folder structure for your Django project, including the necessary configuration files.

---

## ⚙️ Django Server Interfaces: WSGI vs ASGI

Django supports two types of server interfaces:

### 1. **WSGI (Web Server Gateway Interface)** – Traditional (Synchronous)

* **Default in Django**
* Designed to handle standard **HTTP/HTTPS** requests
* **Stateless protocol**: Each request is independent of the others
* Common use cases:

  * E-commerce websites
  * Blogs
  * News sites
* In your `settings.py`, WSGI is set by default:

  ```python
  WSGI_APPLICATION = 'project_name.wsgi.application'
  ```

---

### 2. **ASGI (Asynchronous Server Gateway Interface)** – Real-Time (Asynchronous)

* Designed to handle **real-time communication** and **websockets**
* Supports both **stateful and stateless protocols**
* **Stateful protocol**: Maintains a connection between client and server
* Use cases:

  * Chat applications
  * Video/audio calls
  * Live document editing (e.g., Google Docs)
* To enable ASGI, add the following in your `settings.py`:

  ```python
  ASGI_APPLICATION = 'project_name.asgi.application'
  ```

---

## 📖 Stateless vs Stateful Protocols

| Protocol Type | Description                                                                | Examples                                                 |
| ------------- | -------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Stateless** | Each request is independent; the server doesn’t remember previous requests | HTTP, HTTPS                                              |
| **Stateful**  | Maintains a continuous connection with the client                          | WebSocket, Chat apps, video calls, collaborative editors |

---

## 📝 Summary

* **WSGI** is great for traditional web applications (like blogs, stores).
* **ASGI** is needed for real-time features (like chat or notifications).
* Django supports both — you choose based on your app’s needs.

---

## 🧩 Django Apps

In Django, **apps** are like **independent sub-modules** of your main project.
They help you break your project into smaller, manageable parts — each with its own responsibility.

---

### 🧠 What is a Django App?

* A **Django app** is a Python package that contains a specific functionality or feature of your overall project.
* Each app can have its own:

  * `models.py` – for database models
  * `views.py` – for handling logic and responses
  * `templates/` – for HTML templates
  * `urls.py` – for routing (URL handling)

---

### 📦 Why Use Django Apps?

* To **organize** your project better
* To **reuse** functionality
* To **separate concerns** (each app has its own job)
* To easily plug in **third-party apps** or create your own

---

### 🛍️ Example: E-commerce Project

Imagine you're building an **e-commerce website**. You might break it down into these apps:

| App Name    | Responsibility                   |
| ----------- | -------------------------------- |
| `accounts`  | Handles user registration/login  |
| `products`  | Manages product listings         |
| `orders`    | Handles customer orders          |
| `payments`  | Integrates with payment gateways |
| `logistics` | Manages shipping and tracking    |

Each of these is a **Django app** — a self-contained module of your project.

> ⚠️ **Important:**
> Do **not** create an app named `admin` — Django already has a built-in `admin` app.
> Creating your own `admin` app **can cause conflicts** and break admin-related functionality.

---

### 🛠️ Create a New App

To create a new Django app, use the following command:

```bash
python manage.py startapp app_name
```

> Replace `app_name` with your desired name (e.g., `accounts`, `blog`, etc.)

---

### 🔌 Add App to Project

Once created, add your app to the `INSTALLED_APPS` list in your `settings.py` file:

```python
INSTALLED_APPS = [
    'app_name',
    ...
]
```

This tells Django to recognize and use the app as part of your project.

---

### 🌍 Third-Party Django Apps

You can also use ready-made apps developed by others. Just install them with `pip`:

```bash
pip install django-someapp
```

Then add it to `INSTALLED_APPS`, and you're good to go!

---


