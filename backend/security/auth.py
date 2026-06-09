# security/auth.py

from fastapi import Header, HTTPException

from jwt_service import JWTService


def authenticate(
    authorization: str = Header(...)
):

    if not authorization.startswith(
        "Bearer "
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid header"
        )

    token = authorization.replace(
        "Bearer ",
        ""
    )

    try:

        return JWTService.verify_token(
            token
        )

    except Exception:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )