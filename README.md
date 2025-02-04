
<div align="center">

# 🎬 Vault7 / Movie Library

<br>

(The idea of this project is to to build a user friendly interface with an extensive movie/series library   database.)

<br>

A Django-powered Movie Library where users can browse, like, and manage their favorite movies and series. The project includes a seamless **like/unlike system with AJAX**, ensuring real-time updates without page reloads.

users can look for specific contents with search and filtering functionality.

Get recommendation feature based on user's data (Movie saved on 'watched' or 'liked') or rela.


<br>
<br>


## 🚀 Features

<br>

### 🎥 Movie & Series Management

View the latest **movies** and **series** <br>
Detailed movie and series pages

### ❤️ Like / Unlike System

**AJAX-powered Like/Unlike** (No page reload!) <br>
View all **liked content** on a dedicated page in the user’s profile

### 🔐 Authentication

**User registration & login** <br>
Secure authentication with Django’s built-in system

### 📃 User Dashboard

View **all liked content** <br>
Remove likes in real-time using AJAX

<br>
<br>



## 🛠️ Tech Stack

<br>

|         Technology              |         Purpose         |
| ------------------------------- | ----------------------- |
| **Python (Django)**             | Backend framework       |
| **JavaScript (AJAX, jQuery)**   | Frontend interactivity  |
| **Bootstrap**                   | Styling & UI Components |
| **PostgreSQL**                  | Database                |
| **Django Messages / AJAX**      | Pop-up notifications    |
| **Pillow module**               | image rendering         |


<br>
<br>



## ⚙️ Installation & Setup

<br>

### 1️⃣ Clone the Repository

<div align="left">

```sh
 git clone https://github.com/yourusername/movie-library.git
 cd movie-library
```

</div>

### 2️⃣ Create a Virtual Environment

<div align="left">

```sh
 python -m venv venv
 source venv/bin/activate  # On Windows: venv\Scripts\activate
```

</div>

### 3️⃣ Install Dependencies

<div align="left">

```sh
 pip install -r requirements.txt
```

</div>

### 4️⃣ Apply Migrations

<div align="left">

```sh
 python manage.py migrate
```

</div>

### 5️⃣ Create a Superuser (Optional, for Admin Panel)

<div align="left">

```sh
 python manage.py createsuperuser
```

</div>

### 6️⃣ Run the Development Server
<div align="left">

```sh
 python manage.py runserver
```

</div>

🚀 Open [**http://127.0.0.1:8000/**](http://127.0.0.1:8000/) in your browser.

<br>
<br>

---

## 🛠 Usage Guide

<br>

### 💖 Liking / Unliking Movies & Series

browse through the catalogue of available movies and series <br>
Click the **Like Button** on any movie or series. <br>
View all liked content on the **Liked Content** page.

<br>
<br>

### 🛠 Managing Liked Content

Visit your profile and to the Liked section to see everything you've liked. <br>
Unlike any content from this page, and it **removes instantly** (AJAX ✅).


<br>
<br>

### 📜 Messages & Alerts

Success and error messages appear **instantly**. <br>
Messages disappear **automatically** after a few seconds.

<br>
<br>



## 📌 Future Improvements

<br>

Implement **API** to extend catalogues content. <br>

🎭 search functionality (querying the database with **filtering options**) <br>
**Available on:** Get 3rd party platforms where contents are available for watching (eg: netflix, hbo...) <br>
⭐ Add a **watchlist** feature <br> 
**Recomendation**** features <br>
📊 Implement **like analytics** for top-rated movies

<br>
<br>




## 🤝 Contributing

<br>

Want to contribute? Fork the repo and submit a PR!

<div align="left">

```sh
git checkout -b feature-branch
```

</div>


<br>
<br>

## 📜 License

<br>
<br>

This project is **open-source** under the MIT License.

</div>