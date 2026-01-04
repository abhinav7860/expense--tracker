-Expense Tracker (Django)
 This is a web-based Expense Tracker application developed using Django.  
 The application allows users to register, log in, and manage their personal expenses securely.  
 Each user can add, edit, delete, and view only their own expenses.

- Features
 User registration, login, and logout
 Authentication using Django’s built-in User model
 Each user can access only their own expense data
 Add, update, and delete expenses
 Expense categorization
 Total expense calculation
 Admin panel for managing users and expenses
 Runs locally using Django development server

-Technologies Used
 Python 3
 Django
 HTML and CSS
 SQLite database
 Git and GitHub

-Project Structure
expensetracker/
├── expenses/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── templates/
│ └── static/
├── expensetracker/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
└── manage.py

-How to Run the Server
 Step 1: Clone the Repository:
 git clone https://github.com/abhinav7860/expense--tracker.git
 cd expensetracker

 Step 2: Create and Activate Virtual Environment
 python -m venv myenv
 myenv\Scripts\activate

 Step 3: Install Dependencies
 pip install django

 Step 4: Apply Migrations
 python manage.py makemigrations
 python manage.py migrate

 Step 5: Run the Development Server
 python manage.py runserver
 Open the application in the browser:
 http://127.0.0.1:8000/


-How to Create a Superuser
 A superuser is required to access the Django admin panel.

 Step 1: Create Superuser
 python manage.py createsuperuser

 Step 2: Enter Required Details
 Username
 Email (optional)
 Password

 Step 3: Access Admin Panel
 Run the server and open:
 http://127.0.0.1:8000/admin/
 Log in using the superuser credentials.

-Notes
 The project runs locally using python manage.py runserver
 Hosting the project online is optional
 SQLite is used as the default database

-Author
 Abhinav Sabu
 B.Tech Computer Science
 Expense Tracker Project
