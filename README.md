# User Authentication API

A simple FastAPI application with user registration, login, and JWT authentication.

## Features

- User registration with password hashing
- User login with JWT token generation
- Protected endpoints using JWT authentication
- SQLite database for user storage

## Endpoints

- `POST /auth/register` - Register a new user
- `POST /auth/login` - Login and get JWT token
- `GET /auth/me` - Get current user info (protected)

## Testing

1. Register a user:
```bash
curl -X POST "http://127.0.0.1:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass"}'
```

2. Login and get token:
```bash
curl -X POST "http://127.0.0.1:8000/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=testuser&password=testpass"
```

3. Access protected endpoint:
```bash
curl -X GET "http://127.0.0.1:8000/auth/me" \
  -H "Authorization: Bearer <your-token>"
```

## Run the application

```bash
uvicorn main:app --reload
```
