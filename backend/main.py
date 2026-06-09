market_agent = MarketAgent()

communicator = AgentCommunicationLayer(
    {
        "procurement-agent":
            "http://localhost:8001"
    }
)


shortage = market_agent.analyze_inventory(
    inventory=30,
    demand=50
)

result = await communicator.invoke(
    target_agent="procurement-agent",
    capability="recommend_purchase",
    payload={
        "shortage": shortage
    }
)