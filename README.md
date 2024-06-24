# Sticky-Note-App
 
MyNotes Application
Overview

MyNotes is a web application built with Django that allows users to create, view, edit, and delete sticky notes (post-it notes). Users can sign up, log in, and manage their personal notes within the application.

Features

User Authentication: Users can sign up, log in, and log out securely.
Note Management: Create, view, edit, and delete notes.
Responsive Design: The application is designed to be responsive and works well on different devices.
Database: Uses MariaDB as the relational database for storing notes and user information.


Installation
To run the MyNotes application locally, follow these steps:

Clone the repository

python -m venv venv
Activate the virtual environment:

On Windows:
venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Set up the database:
python manage.py makemigrations
python manage.py migrate

Run the development server:
python manage.py runserver
Access the application:

Open a web browser and go to http://127.0.0.1:8000 to view the application.


Usage
Sign Up: Create a new account using the "Sign Up" link.
Log In: Log in with your credentials using the "Log In" link.
Create a Note: Once logged in, you can create a new note using the "Create a Note!" link.
View Notes: View all your notes using the "Take a look at your current Notes" link.
Edit Note: Click on a note to view its details and edit it.
Delete Note: Delete a note by clicking on the delete button while viewing a note.
Log Out: Log out from your account using the "Log Out" button in the navigation bar.
