# procurement_agent.py

from fastapi import Depends

from auth import authenticate


@app.post("/recommend_purchase")
async def recommend_purchase(
    data: dict,
    claims=Depends(authenticate)
):

    sender = claims["sender"]

    return procurement_agent.recommend_purchase(
        data["shortage"]
    )