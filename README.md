# Travel Booking App  

![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg?logo=python&logoColor=white)  
![Django](https://img.shields.io/badge/django-4.0%2B-green.svg?logo=django&logoColor=white)  
![Bootstrap](https://img.shields.io/badge/UI-Bootstrap-purple.svg?logo=bootstrap)  
![License: MIT](https://img.shields.io/badge/License-MIT-orange.svg)  
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)  


---

##  Overview  

The **Travel Booking App** is a Django-based web application that allows users to:  
-  Browse and filter available travel options (by type, source, destination, and date).  
-  Register and log in to manage bookings.  
-  Book travel tickets with dynamic seat availability and total price calculation.  
-  Cancel confirmed bookings with automatic seat restoration.  
-  View personal booking history in a clean dashboard.  

This project is built with **Django 4.x**, **Bootstrap**, and **SQLite (default)**, but it can be scaled to **PostgreSQL or MySQL** for production.  

---

##  Features  

✅ User authentication (Register, Login, Logout)  
✅ Search travel options (filter by type, source, destination, date)  
✅ Book seats with live seat availability check  
✅ Calculate total booking cost dynamically  
✅ Manage & cancel bookings (with seat restoration)  
✅ Flash messages for success/error feedback  
✅ Responsive UI with Bootstrap  

---

##  Tech Stack  

- **Backend**: Django (Python 3.9+)  
- **Frontend**: Django Templates + Bootstrap 5  
- **Database**: SQLite (default) / PostgreSQL / MySQL  
- **Authentication**: Django Auth System  
- **Styling**: Bootstrap + Custom CSS  

---

##  Project Structure  

```
TravelBookingApp/
│── core/
│   ├── migrations/
│   ├── templates/core/
│   │   ├── travel_list.html
│   │   ├── register.html
│   │   ├── booking_form.html
│   │   ├── my_bookings.html
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│── TravelBookingApp/
│   ├── settings.py
│   ├── urls.py
│── manage.py
```

---

##  Installation  

1. **Clone the Repository**  

```bash
git clone https://github.com/yourusername/Travel-Booking-App.git
cd Travel-Booking-App
```

2. **Create & Activate Virtual Environment**  

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

3. **Install Dependencies**  

```bash
pip install -r requirements.txt
```

4. **Apply Migrations & Run Server**  

```bash
python manage.py migrate
python manage.py runserver
```

5. Open in browser → `http://127.0.0.1:8000/`  

---

##  Usage  

- Register/Login  
- Search for travel options  
- Book available seats  
- View and cancel bookings  

---

---

##  Contributing  

1. Fork the repo  
2. Create a new branch (`feature/awesome-feature`)  
3. Commit your changes  
4. Push to your branch  
5. Open a Pull Request  

---

##  Author  

Developed by **Bharath Kumar Mattapally**  
