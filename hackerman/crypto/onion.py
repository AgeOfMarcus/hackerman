from cryptography.hazmat.primitives import serialization
from hackerman.crypto import rsa
from hackerman.hashing import sha1
from typing import Tuple
import base64

def generate() -> Tuple[str, rsa.rsa.RSAPrivateKey]:
    """
    Generates a new RSA key and its corresponding onion address.

    :return: A tuple containing the onion address and the private key.
    """
    rsa_key = rsa.generate_key(size=1024)
    public_key = rsa_key.public_key()

    public_bytes = public_key.public_bytes(
        encoding = serialization.Encoding.DER,
        format = serialization.PublicFormat.PKCS1
    )
    digest = sha1(public_bytes, hex=False) # hex=False returns bytes
    half_digest = digest[:10]
    return base64.b32encode(half_digest).decode("utf-8").lower() + '.onion', rsa_key

def exportKey(rsa_key: rsa.rsa.RSAPrivateKey) -> str:
    """
    Exports the given RSA key to a PEM string.

    :param rsa_key: The RSA key to export.
    :return: The PEM string.
    """
    return rsa_key.private_bytes(
        encoding = serialization.Encoding.PEM,
        format = serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm = serialization.NoEncryption()
    ).decode("utf-8")