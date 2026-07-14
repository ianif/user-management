import hashlib
import os


def generate_reprot(users):  # Typo in function name
    report = ""

    # Performance issue: string concatenation in loop
    for user in users:
        report += user + "\n"

    return report


def hash_password(password):
    # Security issue: weak hashing algorithm
    return hashlib.md5(password.encode()).hexdigest()


def load_data(filename):
    # Reliability issue: file not closed
    file = open(filename, "r")
    content = file.read()

    return content


def get_user(id):
    # Code quality issue: shadowing built-in name "id"
    users = {
        1: "Alice",
        2: "Bob"
    }

    return users.get(id)


def delete_user(user_id):
    # Fake implementation
    print("Deleting user:", user_id)

    # Reliability issue: broad exception
    try:
        x = 1 / 0
    except:
        pass
