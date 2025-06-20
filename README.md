How to run the code:

S1. Create virtual environment:
python3 -m venv venv

S2. Activate it:
source venv/bin/activate

S3. Install requirements:
npm install requirements

S4. Run the server:
uvicorn main:app –reload

S5. Test GET request:
URL: http://127.0.0.1:8000/
→ Response: { “message”: “Working fine” }

S6. Register user (POST):
URL: http://127.0.0.1:8000/auth/register
Body (raw JSON):
{
“username”: “your_username”,
“password”: “your_password”
}
→ Response: { “message”: “User created successfully” }

S7. Login user (POST):
URL: http://127.0.0.1:8000/auth/login
Headers:
- Content-Type: application/x-www-form-urlencoded
Body (x-www-form-urlencoded):
- username = your_username
- password = your_password
→ Response:
{
“access_token”: “<JWT_TOKEN>”,
“token_type”: “bearer”
}