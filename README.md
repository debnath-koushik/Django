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

Sure! Here's the updated section with the command to **run the Django development server**, including how to **choose a custom port**, explained in a beginner-friendly way for your `README.md`.

---

## 🚀 Running the Django Development Server

Once you’ve created your Django project and set it up, you can start the development server using the following command:

```bash
python manage.py runserver
```

By default, this runs the server at:

```
http://127.0.0.1:8000/
```

---

### 🌐 Choosing a Custom Port

If port `8000` is already in use or you prefer to use another port (e.g., `5000`, `8080`, etc.), you can specify it like this:

```bash
python manage.py runserver 5000
```

This will run your server at:

```
http://127.0.0.1:5000/
```

You can even specify a different IP and port (useful for testing on local networks):

```bash
python manage.py runserver 0.0.0.0:8000
```

This makes your server accessible to **other devices on the same network** (e.g., mobile or another PC).

---

### ✅ Summary

| Command                                   | Description                             |
| ----------------------------------------- | --------------------------------------- |
| `python manage.py runserver`              | Start server on default port `8000`     |
| `python manage.py runserver 5000`         | Start server on custom port `5000`      |
| `python manage.py runserver 0.0.0.0:8000` | Make server accessible on local network |

> ⚠️ **Note:** The development server is only for development and testing. For production, use a proper web server like **Gunicorn** or **Daphne** with **WSGI** or **ASGI**.

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

## 🖼️ Returning HTML Content

You can return HTML directly in `HttpResponse`:

```python
def home(request):
    return HttpResponse("<h1>Welcome to My Django Site</h1><p>This is the home page.</p>")
```

> ⚠️ This works for small responses, but for larger HTML pages, it’s better to use **templates**.

---

### 📑 Returning HTML Using Templates

Instead of hardcoding HTML in your views, use Django’s **template system**:

```python
# views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```

```html
<!-- templates/home.html -->
<h1>Welcome to My Django Site</h1>
<p>This is the home page.</p>
```

This approach keeps your HTML and Python code separate (cleaner & easier to maintain).

---

### 📬 Returning JSON Response (for APIs)

If you want to send JSON (often used in APIs or AJAX requests):

```python
from django.http import JsonResponse

def get_data(request):
    data = {
        "name": "Alice",
        "age": 25,
        "city": "New York"
    }
    return JsonResponse(data)
```

Browser output:

```json
{"name": "Alice", "age": 25, "city": "New York"}
```

---

### ✅ Summary Table

| Response Type      | Function/Method | Example Use Case      |
| ------------------ | --------------- | --------------------- |
| Plain text / HTML  | `HttpResponse`  | Simple messages/pages |
| HTML from template | `render()`      | Web pages             |
| JSON               | `JsonResponse`  | APIs, AJAX responses  |

---

> 💡 **Tip:** Always return an HTTP response object — Django won’t understand plain strings or numbers without wrapping them.

---

## 🔗 Mapping Views to URLs

For a view to work, it needs to be connected to a **URL pattern**.

---

### 1️⃣ Mapping from the Main Project’s `urls.py`

If you created `hello_world` in your **main project folder** (`views.py` inside the folder with `settings.py`):

```python
# project_name/urls.py
from django.contrib import admin
from django.urls import path
from . import views  # Import views from main project

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello_world),  # Map URL to view
]
```

Now visiting:

```
http://127.0.0.1:8000/hello/
```

will show:

```
Hello, World!
```

---

### 2️⃣ Mapping from an App’s `urls.py`

If the view is inside an **app** (e.g., `blog/views.py`):

**`blog/views.py`**

```python
from django.http import HttpResponse

def blog_home(request):
    return HttpResponse("Welcome to the Blog!")
```

**`blog/urls.py`** (create this file inside the app if it doesn’t exist):

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),  # Empty string = root of blog/
]
```
or,

```python
from django.urls import path
from myproject.views import method1, method2  # add app name in the place of myproject

urlpatterns = [
    path('', method1, name='method1'),  
]
```

**`project_name/urls.py`** (main URL configuration):

```python
from django.contrib import admin
from django.urls import path, include  # include lets you link to app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),  # Include blog app's URLs
]
```

Now visiting:

```
http://127.0.0.1:8000/blog/
```

will show:

```
Welcome to the Blog!
```

---

### 📌 Quick Recap

| Location     | File to Edit                                       | Example Code                        |
| ------------ | -------------------------------------------------- | ----------------------------------- |
| Main Project | `project_name/urls.py`                             | `path('hello/', views.hello_world)` |
| App          | `app_name/urls.py` + `include()` in main `urls.py` | `path('', views.my_view)`           |

---

Here’s a simplified, README-friendly version of your Django HTTP Response & URL explanation:

---

# Returning HTTP Responses & Understanding URLs

## 1. Returning a Simple HTTP Response

You can return text directly from a Django view using **`HttpResponse`**.

**Example – `views.py`:**

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi.. from Django Server")
```

---

## 2. Adding HTML Content to Responses

You can send HTML directly in the response.

**Example – `views.py`:**

```python
from django.http import HttpResponse

def about(request):
    html_content = """
    <h1>Hii.. from Django Server | This is the <b>About Page</b></h1>
    <p>This about page can be used to see the about section.</p>
    """
    return HttpResponse(html_content)
```

---

## 3. Understanding URLs in Django

URLs map user requests to views using the `urls.py` file.

**Example – `urls.py`:**

```python
from django.urls import path
from home.views import index, about

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
]
```

* `/` → calls `index` view
* `/about/` → calls `about` view

---

## 4. Returning an HTML Page (Template)

Instead of writing HTML in Python, you can create HTML files and render them.

**Steps:**

1. **Create a `templates` folder** inside your app (`home/templates/`).
2. **Add an HTML file** (e.g., `index.html`):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Django Server</title>
</head>
<body>
    <h1>This HTML page is returned by Django.</h1>
    <p>Django is really nice.</p>
</body>
</html>
```

3. **Update the view** to use `render`:

```python
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
```

4. **Map the URL** in `urls.py`.

---

## 5. Example URL Mappings

| URL Path    | View Function | HTML Page    |
| ----------- | ------------- | ------------ |
| `/`         | index         | index.html   |
| `/about/`   | about         | about.html   |
| `/contact/` | contact       | contact.html |

---

## 6. Run the Server

```bash
python manage.py runserver
```

* Visit **`http://127.0.0.1:8000/`** → Shows index page.
* Visit **`http://127.0.0.1:8000/about/`** → Shows about page.
* Visit **`http://127.0.0.1:8000/contact/`** → Shows contact page.

---

Here’s a cleaned-up, README-friendly version of your notes on **URL namespaces** and **linking pages** in Django:

---

# Linking Pages, Namespaces, and Request Parameters

## 1. Linking Pages in Templates

You can create navigation between pages using the HTML `<a>` tag.

**Example – `index.html`:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django Server</title>
</head>
<body>
    <h1>This HTML page is returned by Django. :)</h1>
    <p>Django is really nice.</p>
    <p>
        <a href="/contact">Contact</a> |
        <a href="/about">About</a>
    </p>
</body>
</html>
```

Do the same for **about.html** and **contact.html**, adding links back to **Home** or other pages.

---

## 2. Changing URL Paths

In `urls.py`, you can change the actual path without changing the template code.

```python
from django.urls import path
from .views import index, about, contact

urlpatterns = [
    path('', index, name='index'),
    path('about-xyz-company/', about, name='about'),
    path('contact/', contact, name='contact'),
]
```

Here:

* `/about-xyz-company/` is the actual path
* `name='about'` is the **namespace** (used for template links)

---

## 3. Using Namespaces with `{% url %}`

Instead of hardcoding URLs, use Django’s **`{% url %}`** tag.
This way, even if you change the actual path later, the links will still work.

**Example – `index.html` with dynamic URLs:**

```html
<p>
    <a href="{% url 'contact' %}">Contact</a> |
    <a href="{% url 'about' %}">About</a>
</p>
```

**Benefits:**

* Avoids broken links if URL patterns change
* Makes code easier to maintain

---

## 4. Running & Testing

```bash
python manage.py runserver
```

* Visit **`http://127.0.0.1:8000/`** → Home page
* Click **Contact** → Goes to `/contact/`
* Click **About** → Goes to `/about-xyz-company/` (but link still works because of namespace)

---

## 5. Flow Diagram

```
User clicks link → Django URL namespace matches → View function runs → HTML page rendered → Response sent to browser
```

---

Here’s your **README-friendly** version for **Creating Dynamic URLs in Django**:

---

# Creating Dynamic URLs

Dynamic URLs allow you to pass **variables** in the URL and use them inside your views.

---

## 1. Creating a View for Dynamic URLs

Example: A view that accepts an `id` from the URL.

**`views.py`**

```python
from django.shortcuts import render

def dynamic_url(request, id):
    print(f"This is the value we got: {id}")
    return render(request, "dynamic_url.html")
```

---

## 2. Template for Dynamic URL

Create a template to display the dynamic data.

**`templates/dynamic_url.html`**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django | Dynamic URL</title>
</head>
<body>
    <h1>This HTML page is returned by Django.</h1>
    <p>Dynamic URL Example</p>
    <p>
        <a href="{% url 'index' %}">Home</a> |
        <a href="{% url 'about' %}">About</a>
    </p>
</body>
</html>
```

---

## 3. Defining URL Patterns

Use **angle brackets `< >`** in `urls.py` to capture variables.

**`urls.py`**

```python
from django.urls import path
from .views import index, dynamic_url

urlpatterns = [
    path('<id>/', dynamic_url, name='dynamic_url'),
]
```

---

## 4. Passing Data from View to Template

Use the `context` parameter in `render()` to send data.

**`views.py`**

```python
def dynamic_url(request, id):
    return render(request, "dynamic_url.html", context={"id": id, "name": "Deepika"})
```

**Updated Template**

```html
<p>{{ name }}</p>
<p>Dynamic URL ID: {{ id }}</p>
```

---

## 5. Running the Example

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/2345908
```

You’ll see:

```
Deepika
Dynamic URL ID: 2345908
```

---

## 6. Restricting Dynamic URL Data Types

Django **path converters** let you enforce data types.

| Converter | Description                                        | Example URL       |
| --------- | -------------------------------------------------- | ----------------- |
| `<int>`   | Matches integers only                              | `/123/`           |
| `<str>`   | Matches any string (no slashes)                    | `/example/`       |
| `<slug>`  | Matches letters, numbers, hyphens, and underscores | `/example-slug/`  |
| `<uuid>`  | Matches a valid UUID                               | `/550e8400-e29b/` |
| `<path>`  | Matches strings including slashes                  | `/example/path/`  |

**Example – Restricting to Integer & String**

```python
urlpatterns = [
    path('<int:id>/<str:name>/', dynamic_url, name='dynamic_url'),
]
```

---

Here’s a **concise, README-friendly** summary comparing **Class-Based Views (CBVs)** and **Function-Based Views (FBVs)** in Django:

---

# Django – Class-Based Views (CBVs) vs Function-Based Views (FBVs)

Django lets you handle requests in **two main ways**:

* **Function-Based Views (FBVs)** – simple functions
* **Class-Based Views (CBVs)** – object-oriented classes

---

## 1. Class-Based Views (CBVs)

CBVs use Python **classes** to structure view logic. They inherit from Django’s built-in base view classes.

**Example – `views.py`:**

```python
from django.views import View
from django.shortcuts import render

class HomeView(View):
    template_name = "index.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)
```

**Example – `urls.py`:**

```python
from django.urls import path
from .views import HomeView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
]
```

**Pros:**

* Organized, reusable code
* Supports **OOP concepts** like inheritance
* Built-in **generic views** (ListView, DetailView, CreateView, etc.)
* Great for **CRUD operations**

**Cons:**

* More complex for beginners
* Implicit code flow (hidden behind mixins)
* Decorators need extra work

---

## 2. Function-Based Views (FBVs)

FBVs are simple **functions** that take a `request` and return a `response`.

**Example – `views.py`:**

```python
from django.shortcuts import render

def dynamic_url(request, id, name):
    return render(request, "dynamic_url.html", context={"id": id, "name": name})
```

**Example – `urls.py`:**

```python
from django.urls import path
from .views import dynamic_url

urlpatterns = [
    path('<int:id>/<str:name>/', dynamic_url, name="dynamic_url"),
]
```

**Pros:**

* Simple and explicit
* Easier for beginners to understand
* Great for unique logic
* Easy to use with decorators

**Cons:**

* Can lead to **repetitive code**
* Manual handling of GET/POST with `if request.method == 'POST'`
* No OOP advantages

---

## 3. When to Use What?

* **Use CBVs** if your project is **CRUD-heavy** or benefits from **inheritance & reusability**.
* **Use FBVs** for **simple, unique, or highly customized** request handling.

---

Here’s your **README-friendly** introduction to Django Template Tags:

---

# Django – Introduction to Template Tags

**Template tags** in Django allow you to add dynamic behavior to HTML templates.
They are written as:

* **`{% ... %}`** → for logic and control flow
* **`{{ ... }}`** → for displaying variables

---

## 1. Why Use Template Tags?

* Embed Python-like logic directly in HTML (without writing Python code in templates).
* Make templates **dynamic** and **data-driven**.
* Keep **logic** in templates and **business code** in views.

---

## 2. Types of Template Tags

### **a) Displaying Variables**

```html
<p>Hello, {{ user.name }}!</p>
```

Displays the value of `user.name` passed from the view.

---

### **b) Conditional Logic**

```html
{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}!</p>
{% else %}
    <p>Please log in to access this page.</p>
{% endif %}
```

Executes code blocks conditionally.

---

### **c) Looping**

```html
<ul>
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
</ul>
```

Iterates over lists or querysets and displays items.

---

### **d) Including Other Templates**

```html
{% include 'header.html' %}
```

Reuses template parts (e.g., headers, footers) to keep code DRY.

---

### **e) Loading Custom Template Tags**

* You can create your own tags for custom logic.
* Example:

```python
# myapp/templatetags/custom_tags.py
from django import template
register = template.Library()

@register.simple_tag
def greet(name):
    return f"Hello, {name}!"
```

```html
{% load custom_tags %}
<p>{% greet "John" %}</p>
```

---

## 3. Quick Syntax Summary

| Purpose          | Syntax Example                          |
| ---------------- | --------------------------------------- |
| Show variable    | `{{ variable_name }}`                   |
| If condition     | `{% if condition %}...{% endif %}`      |
| For loop         | `{% for item in list %}...{% endfor %}` |
| Include file     | `{% include 'file.html' %}`             |
| Load custom tags | `{% load custom_tags %}`                |

---

Got it — you’re basically outlining a **full Django Template Language (DTL) guide** here.
If we tidy this up into a clean, structured explanation, it could look like this:

---

## **Django Template Language (DTL) – Complete Guide**

Django’s template language is a **lightweight, HTML-friendly syntax** for injecting dynamic data into web pages. It supports **variables, tags, filters, and template inheritance** — making it easy to separate presentation from logic.

---

### **1. Syntax Basics**

| Purpose   | Syntax                | Example                   |           |            |
| --------- | --------------------- | ------------------------- | --------- | ---------- |
| Variables | `{{ variable_name }}` | `{{ user.username }}`     |           |            |
| Tags      | `{% tag_name %}`      | `{% for item in items %}` |           |            |
| Filters   | \`{{ variable         | filter }}\`               | \`{{ name | upper }}\` |

---

### **2. Variables**

Variables are placeholders for dynamic data from your view.

**Example:**

```html
<title>{{ title }}</title>
<h1>Welcome, {{ user.username }}!</h1>
```

**Passing variables from view:**

```python
# views.py
from django.shortcuts import render

def my_view(request):
    context = {
        'title': 'Welcome to My Website',
        'user': request.user,
        'items': ['Item 1', 'Item 2', 'Item 3'],
        'date': '2024-03-18',
        'number': 123.456,
    }
    return render(request, 'my_template.html', context)
```

---

### **3. Tags (Logic Control)**

Tags allow **looping, conditionals, includes, and inheritance**.

**For loop:**

```django
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
```

**If/Else:**

```django
{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}!</p>
{% else %}
    <p>Please log in.</p>
{% endif %}
```

**Include:**

```django
{% include 'navbar.html' %}
```

**Inheritance:**

```django
<!-- base.html -->
<html>
<head>
    <title>{% block title %}Default Title{% endblock %}</title>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>

<!-- child.html -->
{% extends 'base.html' %}
{% block title %}Home Page{% endblock %}
{% block content %}
    <h1>This is the home page.</h1>
{% endblock %}
```

---

### **4. Filters (Data Formatting)**

Filters modify variable output.

**Examples:**

```django
{{ text|lower }}                   <!-- lowercase -->
{{ date|date:"D d M Y" }}           <!-- format date -->
{{ number|floatformat:2 }}          <!-- 2 decimal places -->
```

---

### **5. Custom Tags & Filters**

You can extend DTL with your own logic.

**Custom Tag Example:**

```python
# custom_tags.py
from django import template
register = template.Library()

@register.simple_tag
def multiply(a, b):
    return a * b
```

**Usage:**

```django
{% load custom_tags %}
{% multiply 2 3 %}  <!-- Outputs: 6 -->
```

---

### **6. Best Practices**

* **Keep Templates Simple** → Avoid complex logic.
* **Push Business Logic to Views** → Templates should handle only display.
* **Use Filters for Formatting** → Clean, reusable formatting.
* **Leverage Inheritance** → Create base layouts for consistency.

---

Alright, let’s break this down step-by-step so it’s crystal clear.

---

## **Template Inheritance in Django**

Django’s **template inheritance** is basically like making a "master HTML template" (base) and letting other HTML pages (children) fill in only the parts that are different.
Think of it like a cake mold — you always get the same shape (header, footer, layout), but you can change the flavor (page-specific content) without rebuilding the whole cake.

---

### **Key Concepts**

1. **Base Template (`base.html`)**

   * This contains the general layout: header, footer, navbar, CSS/JS imports, etc.
   * Uses `{% block %}` tags to mark places where child templates can insert their own content.

2. **Child Templates (e.g., `home.html`, `about.html`)**

   * They **extend** the base template with `{% extends "base.html" %}`.
   * Fill or override the `{% block %}` sections.

3. **Blocks**

   * Named placeholders inside templates.
   * Syntax:

     ```django
     {% block block_name %}
         Default or empty content
     {% endblock %}
     ```

4. **Context**

   * A dictionary passed from the view to the template via:

     ```python
     return render(request, 'template.html', context)
     ```
   * Variables in the context can be used in **both base and child templates** as `{{ variable_name }}`.

---

### **Example Flow**

#### **1. Base Template: `base.html`**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Django Server</title>
</head>
<body>
  <header>
      <h2>My Website</h2>
  </header>

  {% block start %}
  {% endblock %}

  <footer>
    &copy; 2024 My Page
  </footer>
</body> 
</html>
```

---

#### **2. Child Template: `home.html`**

```django
{% extends "base.html" %}

{% block start %}
    <h1>This HTML page is returned by Django.</h1>
    <p>Django is really nice.</p>
    <p>Home Page.</p>
    <p>{{ message }}</p>

    <p>
        <a href="{% url 'about' %}" target="_blank"> About </a> | 
        <a href="{% url 'contact' %}" target="_blank"> Contact </a>
    </p>
{% endblock %}
```

---

#### **3. View: `views.py`**

```python
from django.shortcuts import render

def home_page(request):
    context = {'message': 'Hello from the Home Page!'}
    return render(request, 'home.html', context)
```

---

## **The `{% include %}` Tag**

**Purpose:**
Instead of inheritance, `{% include %}` allows you to **drop in reusable chunks of HTML** into any template.
Think of it as "copy-paste at render time."

---

### **Example:**

#### **`image.html`**

```html
<div class="image-container">
    <img src="{{ image_url }}" alt="{{ image_alt_text }}">
    {% if description %}
        <p>{{ description }}</p>
    {% endif %}
</div>
```

---

#### **Using Include in `home.html`**

```django
{% extends "base.html" %}

{% block start %}
    {% include "image.html" with image_url="path/to/image.jpg" image_alt_text="My Image" description="A beautiful image" %}

    <h1>This HTML page is returned by Django.</h1>
    <p>Django is really nice.</p>
    <p>Home Page.</p>
    <p>{{ message }}</p>

    <p>
        <a href="{% url 'about' %}" target="_blank"> About </a> | 
        <a href="{% url 'contact' %}" target="_blank"> Contact </a>
    </p>
{% endblock %}
```

---

### **Difference: Inheritance vs Include**

| Feature     | Inheritance (`extends`)                            | Include (`include`)               |
| ----------- | -------------------------------------------------- | --------------------------------- |
| **Purpose** | Defines a **parent-child** relationship for layout | Inserts reusable template chunks  |
| **Scope**   | Whole page layout                                  | Small components/snippets         |
| **Blocks**  | Yes, child can override blocks                     | No blocks, just content insertion |
| **Usage**   | Base HTML → Child HTML                             | Navbar, footer, widgets, cards    |

---

It looks like you’ve compiled a guide that mixes **CSS styling methods** with an example of **Bootstrap integration into Django templates**.
Let me break this down into **clear, commented notes** so it’s easier to understand and reuse.

---

## **1. Adding CSS Directly in HTML Templates**

There are three main ways:

---

### **a) Inline Styles**

Directly add `style` attributes to HTML elements.

```html
<p style="color: red; font-size: 16px;">
    This is a paragraph with inline styles.
</p>
```

* **Pros:** Quick for small, one-off changes.
* **Cons:** Hard to maintain for large projects.

---

### **b) Embedded CSS in `<head>`**

Place `<style>` tags in the `<head>` section to define styles for multiple elements.

```html
<head>
    <style>
        p {
            color: blue;
            font-size: 14px;
        }
    </style>
</head>
```

* **Pros:** Centralized for the page.
* **Cons:** Only affects that single HTML file.

---

### **c) `<style>` Block Inside `<body>`**

Possible but **not recommended** except for very targeted styles.

```html
<div>
    <h1>Heading</h1>
    <style>
        h1 {
            color: green;
            font-size: 24px;
        }
    </style>
</div>
```

* **Use Case:** Styling dynamically generated sections without touching the main CSS.

---

## **2. Integrating Bootstrap into Django**

Bootstrap gives you a ready-made responsive design system.

---

### **a) Base Template (`base.html`)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <!-- Bootstrap CSS from CDN -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <!-- Example embedded CSS -->
    <style>
        p { color: aqua; }
    </style>

    {% block start %}{% endblock %}

    <!-- Example JavaScript -->
    <script>
        alert('Hello Django lovers hea');
    </script>

    <!-- Bootstrap JS from CDN -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

**Key points:**

* **`{% block start %}`** lets other templates inject content.
* Bootstrap **CSS** goes in `<head>`, **JS** at the end for faster loading.
* Inline `<style>` is allowed but for bigger projects, keep styles in a separate `.css` file.

---

### **b) Child Template Example**

```html
{% extends 'base.html' %}

{% block start %}
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
        <a class="navbar-brand" href="#">Django Bootstrap Demo</a>
    </div>
</nav>

<div class="container mt-5">
    <h1>Welcome to our Django Bootstrap Demo!</h1>
    <p>Django is powerful, and Bootstrap makes it beautiful.</p>
</div>
{% endblock %}
```

* Uses Bootstrap classes (`navbar`, `container`, etc.).
* Extends the base template so you don’t repeat boilerplate.

---

## **3. How the Alert Works**

When the page loads, the `<script>` in the base template runs:

```javascript
alert('Hello Django lovers hea');
```

* This pops up a message immediately after the DOM loads.
* Could be replaced with more interactive JavaScript.

---

