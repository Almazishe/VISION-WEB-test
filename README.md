# VISION-WEB-test

# Administration panel
#### email: admin@me.com
#### pass: admin

### API
 - [POST] : http://127.0.0.1:8000/auth/users/ (Регистрация)
     body: {
        "email": "test@me.com",
        "password": "test_password_123",
        "re_password": "test_password_123",
     }
 - [POST] http://127.0.0.1:8000/auth/users/activation/ (Активация аккаунта)
    body {
        "uid": <uid_from_email>,
        "token": <token_from_email>
    }
 - [POST] http://127.0.0.1:8000/auth/jwt/create/ (Создание токенов (success&refresh))
    body {
        "email": <user_email>,
        "password": <user_password>
    }
 -  [GET] http://127.0.0.1:8000/auth/users/ (Лист юзеров)
    headers {
        "Authorization": "JWT <your_success_token>"
    }
