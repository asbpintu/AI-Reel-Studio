from app.security.jwt import create_access_token, decode_token


def test_jwt():

    token = create_access_token(
        {
            "sub": "admin@test.com",
            "role": "Admin",
        }
    )

    print(token)

    payload = decode_token(token)

    print(payload)


if __name__ == "__main__":
    test_jwt()  