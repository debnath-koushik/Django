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


