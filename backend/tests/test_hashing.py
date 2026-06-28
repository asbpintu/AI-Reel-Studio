from app.security.hashing import hash_password, verify_password




def test_hashing():
    pwd = hash_password("Password@123")

    print(pwd)

    print(verify_password("Password@123", pwd))

    print(verify_password("WrongPassword", pwd))

if __name__ == "__main__":
    test_hashing()
