import base64
import hashlib
import hmac

from flask import current_app


def __generate_password_digest(password: str) -> bytes:
    return hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode("utf-8"),
        salt=current_app.config["PWD_HASH_SALT"],
        iterations=current_app.config["PWD_HASH_ITERATIONS"],
    )


def generate_password_hash(password: str) -> str:
    return base64.b64encode(__generate_password_digest(password)).decode('utf-8')


def compare_passwords(password_hash, other_password):
    """

    :param password_hash: - Password from DB
    :param other_password: - Password from user input
    :return:
    """
    return password_hash == generate_password_hash(other_password)


def generate_token(email, password, password_hash):
    ...


def update_token(refresh_token):
    ...
