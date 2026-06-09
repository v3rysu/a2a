# registry.py

class AgentRegistry:

    def __init__(self):

        self.agents = {
            "market-agent":
                "http://localhost:8000",

            "procurement-agent":
                "http://localhost:8001"
        }

    def get_url(self, agent_name):

        return self.agents[agent_name]