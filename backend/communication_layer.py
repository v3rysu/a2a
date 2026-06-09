# communication/communicator.py

import httpx

from security.jwt_service import JWTService
from registry.agent_registry import AgentRegistry
from security.authorization_service import AuthorizationService


class AgentCommunicator:

    def __init__(
        self,
        registry: AgentRegistry,
        jwt_service: JWTService,
        authorization_service: AuthorizationService
    ):
        self.registry = registry
        self.jwt_service = jwt_service
        self.authorization_service = authorization_service

    async def invoke(
        self,
        sender: str,
        receiver: str,
        capability: str,
        payload: dict
    ):

        # Authorization
        if not self.authorization_service.is_allowed(
            sender,
            receiver
        ):
            raise PermissionError(
                f"{sender} cannot call {receiver}"
            )

        # Authentication
        token = self.jwt_service.create_token(
            sender
        )

        headers = {
            "Authorization": f"Bearer {token}"
        }

        # Discovery
        agent_url = self.registry.get_url(
            receiver
        )

        # Communication
        async with httpx.AsyncClient() as client:

            response = await client.post(
                f"{agent_url}/{capability}",
                json=payload,
                headers=headers
            )

            response.raise_for_status()

            return response.json()