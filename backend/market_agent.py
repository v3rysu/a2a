class MarketAgent:

    def analyze_inventory(
        self,
        inventory: int,
        demand: int
    ):

        return max(0, demand - inventory)