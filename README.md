# Flask User Authentication System

## Overview

This Flask application provides user authentication functionalities, including login, registration, and password hashing. It uses SQLAlchemy for database interactions and bcrypt for securely hashing passwords.

## Features

- **User Registration:** Allows users to create an account with a name, email, and password.
- **User Login:** Authenticates users using hashed passwords.
- **Welcome Page:** Displays a welcome message with the user's name.
- **Logout:** Clears the session to log out the user.

## Code Description

### 1. `app.py`

- **Initialization:** Sets up Flask, SQLAlchemy, and bcrypt.
- **Database Model:** Defines `LoginDetails` model for user information.
- **Routes:**
  - `/`: Handles login requests.
  - `/register`: Handles user registration.
  - `/welcome`: Displays a welcome page.
  - `/logout`: Logs out the user.

### 2. Database Initialization

The `init_db()` function creates the database and tables if they do not already exist.

## Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy
- bcrypt
- SQLite

## Installation

1. Clone this repository:

    ```bash
    git clone <https://github.com/ash1009/Flask-User-Authentication-System/tree/main>
    cd <Flask User Authentication System>
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Initialize the database:

    ```bash
    python app.py
    ```

## Usage

1. Start the Flask application:

    ```bash
    python app.py
    ```

2. Access the application in your web browser at [http://localhost:5000](http://localhost:5000).

3. Register, log in, and use the available features.

## Credits

This project uses SQLite for the database and bcrypt for password hashing.
