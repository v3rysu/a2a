# security/authorization_service.py

class AuthorizationService:

    PERMISSIONS = {

        "market-agent": [
            "procurement-agent"
        ],

        "procurement-agent": [
            "finance-agent"
        ],

        "finance-agent": []
    }

    def is_allowed(
        self,
        sender: str,
        receiver: str
    ):

        allowed = self.PERMISSIONS.get(
            sender,
            []
        )

        return receiver in allowed