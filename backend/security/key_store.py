# security/keystore.py

from pathlib import Path


class KeyStore:

    def __init__(self, key_directory: str = "keys"):
        self.key_directory = Path(key_directory)

    def get_private_key(self, agent_name: str) -> str:

        key_file = (
            self.key_directory /
            f"{agent_name}_private.pem"
        )

        return key_file.read_text()

    def get_public_key(self, agent_name: str) -> str:

        key_file = (
            self.key_directory /
            f"{agent_name}_public.pem"
        )

        return key_file.read_text()