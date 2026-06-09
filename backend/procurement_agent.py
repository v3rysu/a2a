class ProcurementAgent:

    def recommend_purchase(self, shortage: int):

        return {
            "recommendation": f"Purchase {shortage} laptops",
            "estimated_cost": shortage * 1500
        }