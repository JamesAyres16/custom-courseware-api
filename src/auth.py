""" authentication utilities """
from typing import Annotated

from fastapi.security import OAuth2AuthorizationCodeBearer
from fastapi import HTTPException, Depends

from sqlalchemy.orm.session import Session
import jwt

from .database import default_db_manager
from .schemas.user import User
from .config import config


openid_url = "{}/realms/{}/protocol/openid-connect".format(
    config.KEYCLOAK_URL, config.KEYCLOAK_REALM
)
oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=f"{openid_url}/auth",
    tokenUrl=f"{openid_url}/token",
    refreshUrl=f"{openid_url}/token"
)
jwks_client = jwt.PyJWKClient(f"{openid_url}/certs")



def user(
    token: Annotated[str, Depends(oauth2_scheme)],
    session: Annotated[Session, Depends(default_db_manager.get_session)]
) -> User:
    """ gets user from JWT """
    exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        signing_key = jwks_client.get_signing_key_from_jwt(token)
        payload: dict = jwt.decode(
            token, signing_key, algorithms=["RS256"], require=["exp"]
        )
        print(payload)
    except jwt.InvalidTokenError as e:
        raise exception from e

    user_id = subject.lstrip("user:")
    user = session.get(User, user_id)
    if not user:
        raise exception
    return user
