**Master Documentation**

# Vektor Data

Vektor Data is a Retrieval-Augmented Generation (RAG) application designed to help businesses easily interact with their reviews using a vector database and Large Language Models (LLMs). This project leverages advanced AI techniques to provide insightful analysis and interactions with business reviews, enhancing customer feedback management and decision-making processes.

## Features

- **Vector Database Integration**: Efficiently stores and retrieves business reviews using vector representations.
- **LLM Interaction**: Utilizes Azure OpenAI to generate and infer valuable insights from business reviews.
- **User-Friendly Interface**: Developed with React for a seamless and intuitive user experience.
- **Scalable Backend**: Powered by Flask and Python, ensuring high performance and flexibility.
- **Secure Data Management**: MongoDB is used for secure and efficient data storage.

## Tech Stack

- **Frontend**: React
- **Backend**: Python, Flask
- **Database**: MongoDB
- **AI Integration**: Azure OpenAI
- **Hosting & Deployment**: ....

### Prerequisites

- React.js
- Python 3.x
- MongoDB
- Azure OpenAI API Key

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/vektor-data.git
   cd vektor-data

## Dependencies

Below is a table documenting the main dependencies used in this project and their purposes:

| Dependency          | Version  | Purpose                                                                                  |
|---------------------|----------|------------------------------------------------------------------------------------------|
| `apify_client`      | 1.7.1    | Client for interacting with the Apify platform, used for web scraping and automation tasks. |
| `apify_shared`      | 1.1.2    | Shared utilities and functions for Apify client usage.                                    |
| `Cerberus`          | 1.3.5    | A lightweight and extensible data validation library for Python.                          |
| `certifi`           | 2024.7.4 | Provides Mozilla's CA Bundle, which is used for SSL verification in HTTP clients.         |
| `dnspython`         | 2.6.1    | A DNS toolkit for Python, used for performing DNS queries and managing DNS records.       |
| `Flask`             | 3.0.3    | A micro web framework for Python, used to build the backend of the application.           |
| `httpcore`          | 1.0.5    | A low-level HTTP library, used as the base transport layer for HTTP clients like httpx.   |
| `httpx`             | 0.27.0   | An HTTP client for Python, providing a synchronous and asynchronous API for making HTTP requests. |
| `itsdangerous`      | 2.2.0    | Used to securely sign data, ensuring that it hasn’t been tampered with.                   |
| `MarkupSafe`        | 2.1.5    | Provides a way to handle strings with safe and unsafe content, used by Jinja2 and Flask.  |
| `PyJWT`             | 2.9.0    | A Python library for encoding and decoding JSON Web Tokens (JWT), used for user authentication. |
| `pymongo`           | 4.8.0    | A Python driver for MongoDB, used to interact with the MongoDB database.                  |
| `python-dotenv`     | 1.0.1    | Loads environment variables from a `.env` file, making it easier to manage configuration. |
| `pytz`              | 2024.1   | Provides accurate and cross-platform timezone calculations, essential for datetime handling. |
| `typing_extensions` | 4.12.2   | Provides backport of new type hinting features for older Python versions.                 |
| `Werkzeug`          | 3.0.3    | A comprehensive WSGI web application library, used by Flask for request and response handling. |

## Routes

| **Route**  | **Method** | **Description**                                                                 | **Required Fields**                                                                                                                               | **Responses**                                                                                                                                              |
|------------|------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `/signup`  | `POST`     | Used to sign up a new user. It creates a new user account in the system.         | - `first_name`: The user's first name <br> - `last_name`: The user's last name <br> - `email`: Official email <br> - `country`: The user's country <br> - `phone_number`: The user's phone number <br> - `password`: The user's password | - `201 Created`: User created successfully. <br> - `400 Bad Request`: Missing fields, unofficial email, or email already registered.                      |
| `/login`   | `POST`     | Used to log in a user. It authenticates the user and returns a JWT for session management. | - `email`: The user's email address <br> - `password`: The user's password                                                                       | - `200 OK`: Login successful, returns JWT. <br> - `400 Bad Request`: Missing email or password. <br> - `401 Unauthorized`: Invalid credentials.            |




