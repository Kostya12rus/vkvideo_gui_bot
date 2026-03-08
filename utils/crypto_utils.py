import base64
import pickle
import zlib
from os import urandom
from typing import Any

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

SALT_SIZE = 16  # размер соли в байтах


def _get_key(password: str, salt: bytes) -> bytes:
    """ Генерирует ключ на основе пароля и соли. """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))


def _encrypt_bytes(data: bytes, password: str) -> bytes:
    """ Шифрует байтовые данные, добавляя соль в начало результата.

    Args:
        data (bytes): Данные для шифрования.
        password (str): Пароль для генерации ключа.

    Returns:
        bytes: Соль (16 байт) + зашифрованные данные.
    """
    salt = urandom(SALT_SIZE)
    return salt + Fernet(_get_key(password, salt)).encrypt(data)


def _decrypt_bytes(token: bytes, password: str) -> bytes:
    """ Расшифровывает байтовые данные с учетом префикса-соли.

    Args:
        token (bytes): Соль (16 байт) + зашифрованные данные.
        password (str): Пароль, использованный для шифрования.

    Returns:
        bytes: Расшифрованные данные.
    """
    salt, encrypted = token[:SALT_SIZE], token[SALT_SIZE:]
    return Fernet(_get_key(password, salt)).decrypt(encrypted)


def encrypt_text(obj: Any, password: str = "") -> str:
    """ Шифрует строку и возвращает байтовое представление.

    Args:
        obj: Объект для шифрования.
        password (str): Пароль для шифрования.

    Returns:
        str: Зашифрованные данные.
    """
    return base64.b64encode(_encrypt_bytes(zlib.compress(pickle.dumps(obj)), password)).decode()


def decrypt_text(obj_text: str, password: str = "") -> Any:
    """ Расшифровывает байты и возвращает строку.

    Args:
        obj_text (str): Зашифрованные данные.
        password (str): Пароль для расшифровки.

    Returns:
        Any: Расшифрованная данные.
    """
    return pickle.loads(zlib.decompress(_decrypt_bytes(base64.b64decode(obj_text.encode()), password)))
