Django Rest API for Articles using Token Authentication
This Django Rest API allows users to perform CRUD operations on Articles. It utilizes Token Authentication for authorization.

Prerequisites
Python 3
Django 4
Django Rest Framework
Setup
Clone this repository to your local machine.
Navigate to the root directory of the project in your terminal.
Create a virtual environment: python3 -m venv venv
Activate the virtual environment: source venv/bin/activate or venv\Scripts\activate if on windows
Install the dependencies: pip install -r requirements.txt
Run the migrations: python manage.py migrate
Start the server: python manage.py runserver
Usage
Authentication
All CRUD operations except for Login and Register require token authentication.

Register: /api/auth/signup/

To create a new user account, send a POST request to this endpoint with a JSON payload containing username, email, and password.

Example:

POST /api/auth/signup/
Content-Type: application/json

{
    "email": "@example.com",
    "username": "user",
    "password": "password"
}
Login: /api/auth/login/

To obtain a token, send a POST request to this endpoint with a JSON payload containing username and password.

Example:

POST /api/auth/login/
Content-Type: application/json

{
    "username": "testuser",
    "password": "testpassword"
}
The response will include a token in the auth_token field.

Example:

{
    "auth_token": "9f144b962fc4a139042f5f5d5d5b8d875d53a87a"
}
Logout: /api/auth/logout/

To log out, send a POST request to this endpoint with an Authorization header containing the token.

Example:

POST /api/auth/logout/
Authorization: Token 9f144b962fc4a139042f5f5d5d5b8d875d53a87a
Articles
List Articles: /api/articles/

To retrieve a list of articles, send a GET request to this endpoint with an Authorization header containing the token.

Example:


GET /api/articles/
Authorization: Token 9f144b962fc4a139042f5f5d5d5b8d875d53a87a
Create Article: /api/articles/

To create a new article, send a POST request to this endpoint with a JSON payload containing title and content, and an Authorization header containing the token.

Example:


POST /api/articles/
Authorization: Token 9f144b962fc4a139042f5f5d5d5b8d875d53a87a
Content-Type: application/json

{
    "title": "Test Article",
    "content": "This is a test article."
}
Retrieve Article: /api/articles/<id>/

To retrieve a specific article, send a GET request to this endpoint with an Authorization header containing the token.

Example:

GET /api/articles/1/
Authorization: Token 9f144b962fc4a139042f5f5d5d5b8d875d53a87a



This project has a a react frontend i will be attaching 


