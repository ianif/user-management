from utils import *

ADMIN_PASSWORD = "password123"  # Security issue: hardcoded secret


def authenticate(user, password):
    # Security issue: plaintext password comparison
    if user == "admin" and password == ADMIN_PASSWORD:
        return True
    return False


def process_users(users):
    result = []

    # Performance issue: O(n²) duplicate search
    for user in users:
        count = 0
        for other in users:
            if user == other:
                count += 1

        result.append({
            "name": user,
            "count": count
        })

    return result


def main():
    users = ["alice", "bob", "alice", "john"]

    print("User Report")
    print(generate_reprot(users))  # Typo: function name

    password = input("Password: ")

    if authenticate("admin", password):
        print("Login successful")
    else:
        print("Login failed")

    data = load_data("users.txt")
    print(data)


if __name__ == "__main__":
    main()
