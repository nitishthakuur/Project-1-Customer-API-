# FastAPI Customer Management API

A RESTful Customer Management API built with Python, FastAPI, Pydantic, and SQLite.

## Features

- Create customers
- Retrieve all customers
- Retrieve a customer by ID
- Update customer details
- Delete customers
- Request validation using Pydantic
- SQLite database integration
- Dependency injection for database connections
- Proper HTTP status codes and error handling

## Tech Stack

- Python
- FastAPI
- Pydantic
- SQLite
- Uvicorn

## Project Structure

```text
fastapi-customer-api/
│
├── main.py
├── customerapi.py
├── databasefastapi.py
├── README.md
└── .gitignore

## Installation

### 1. Clone the repository

```bash
git clone <https://github.com/nitishthakuur/Project-1-Customer-API->
cd <your-project-folder>

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

Replace `<https://github.com/nitishthakuur/Project-1-Customer-API->` with your actual GitHub repository URL.

---

# Running the API

Add:

```markdown
## Running the API

Start the FastAPI development server using Uvicorn:

```bash
uvicorn main:app --reload

# API will run at:

http://127.0.0.1:8000

# Interactive API Documentation

http://127.0.0.1:8000/docs


---

# API Endpoints

This is an important section for an interviewer.

Add:

```markdown
## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/customer/` | Create a new customer |
| GET | `/customer/` | Retrieve all customers |
| GET | `/customer/{id}` | Retrieve a customer by ID |
| PUT | `/customer/{id}` | Update customer details |
| DELETE | `/customer/{id}` | Delete a customer |

# Example Request

## Example Request

### Create Customer

**POST** `/customer/`

```json
{
    "phone_number": "9876543210",
    "name": "Rahul",
    "password": "example123"
}

# Example Response

{
    "message": "Employee added successfully"
}


One thing: your current API response actually says **"Employee added successfully"**, even though this is a customer API. That's something I'd recommend fixing in the code before finalizing the README. Otherwise an interviewer could notice the inconsistency.

---

# Validation

Add:

```markdown
## Validation

The API uses Pydantic for request validation.

- Phone numbers must contain exactly 10 digits.
- Password length must be between 6 and 10 characters.
- Invalid customer IDs return `404 Not Found`.
- Invalid request data returns `422 Unprocessable Content`.


## Database

This project uses SQLite as its database.

The database connection is provided to the API endpoints using FastAPI dependency injection.

The SQLite database file is excluded from Git using `.gitignore`.

## Technologies Used

- Python
- FastAPI
- Pydantic
- SQLite
- Uvicorn

## Future Improvements

- Implement secure password hashing
- Add authentication and authorization
- Add automated tests
- Improve database architecture
- Add pagination
- Deploy the API



