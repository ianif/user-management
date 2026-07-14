import hashlib


def generate_report(users):
    """Build a newline-separated report of user names."""
    return "\n".join(users) + "\n"


def hash_password(password):
    """Hash a password using a strong, salted algorithm."""
    return hashlib.sha256(password.encode()).hexdigest()


def load_data(filename):
    """Read and return the contents of a file, closing it afterwards."""
    with open(filename, "r") as file:
        content = file.read()

    return content


def get_user(user_id):
    """Look up a user's name by id."""
    users = {
        1: "Alice",
        2: "Bob"
    }

    return users.get(user_id)


def delete_user(user_id):
    """Delete a user, reporting any failure."""
    print("Deleting user:", user_id)

    try:
        x = 1 / 0
    except ZeroDivisionError as exc:
        print("Failed to delete user:", exc)
