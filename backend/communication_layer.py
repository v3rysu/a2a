# communication/communicator.py

import httpx

from security.jwt_service import JWTService
from registry.agent_registry import AgentRegistry


class AgentCommunicator:

    def __init__(
        self,
        registry: AgentRegistry,
        jwt_service: JWTService
    ):
        self.registry = registry
        self.jwt_service = jwt_service

    async def invoke(
        self,
        sender: str,
        receiver: str,
        capability: str,
        payload: dict
    ):

        token = self.jwt_service.create_token(
            sender
        )

        headers = {
            "Authorization":
                f"Bearer {token}"
        }

        agent_url = self.registry.get_url(
            receiver
        )

        async with httpx.AsyncClient() as client:

            response = await client.post(
                f"{agent_url}/{capability}",
                json=payload,
                headers=headers
            )

            response.raise_for_status()

            return response.json()