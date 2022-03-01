import cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def generate_key(size=4096) -> rsa.RSAPrivateKey:
    """
    Generates a new private key.

    :param size: The size of the key. Defaults to 4096.
    :return: The private key.
    """
    return rsa.generate_private_key(
        public_exponent=65537,
        key_size=size,
        backend=default_backend()
    )

def export_private_key(rsa_key: rsa.RSAPrivateKey) -> str:
    """
    Exports the given RSA key to a PEM string.

    :param rsa_key: The RSA key to export.
    :return: The PEM string.
    """
    return rsa_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    ).decode("utf-8")

def export_public_key(rsa_key: rsa.RSAPublicKey) -> str:
    """
    Exports the given RSA key to a PEM string.

    :param rsa_key: The RSA key to export.
    :return: The PEM string.
    """
    return rsa_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.PKCS1
    ).decode("utf-8")

def encrypt(rsa_key: rsa.RSAPublicKey, data: bytes) -> bytes:
    """
    Encrypts data with given RSA key.

    :param rsa_key: The RSA key to use.
    :param data: The data to encrypt.
    :return: The encrypted data.
    """
    return rsa_key.encrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None
        )
    )

def decrypt(rsa_key: rsa.RSAPrivateKey, data: bytes) -> bytes:
    """
    Decrypts data with given RSA key.

    :param rsa_key: The RSA key to use.
    :param data: The data to decrypt.
    :return: The decrypted data.
    """
    return rsa_key.decrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None
        )
    )