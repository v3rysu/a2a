# security/jwt_service.py

import jwt

from datetime import datetime, timedelta
from security.keystore import KeyStore


class JWTService:

    def __init__(self):
        self.keystore = KeyStore()

    def create_token(self, sender: str):

        private_key = self.keystore.get_private_key(
            sender
        )

        payload = {
            "sender": sender,
            "exp": datetime.utcnow() + timedelta(minutes=30)
        }

        return jwt.encode(
            payload,
            private_key,
            algorithm="RS256"
        )

    def verify_token(self, token: str):

        unverified_payload = jwt.decode(
            token,
            options={"verify_signature": False}
        )

        sender = unverified_payload["sender"]

        public_key = self.keystore.get_public_key(
            sender
        )

        return jwt.decode(
            token,
            public_key,
            algorithms=["RS256"]
        )