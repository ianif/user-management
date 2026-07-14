import getpass
import os
from collections import Counter

from utils import generate_report, hash_password, load_data

ADMIN_PASSWORD_HASH = os.environ.get("ADMIN_PASSWORD_HASH", hash_password("password123"))


def authenticate(user, password):
    """Authenticate a user by comparing hashed passwords."""
    return user == "admin" and hash_password(password) == ADMIN_PASSWORD_HASH


def process_users(users):
    """Return each user's name along with how many times it occurs."""
    counts = Counter(users)
    return [{"name": user, "count": counts[user]} for user in users]


def main():
    users = ["alice", "bob", "alice", "john"]

    print("User Report")
    print(generate_report(users))

    password = getpass.getpass("Password: ")

    if authenticate("admin", password):
        print("Login successful")
    else:
        print("Login failed")

    data = load_data("users.txt")
    print(data)


if __name__ == "__main__":
    main()
