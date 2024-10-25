""" Custom Courseware API entrypoint """
from fastapi import FastAPI
import uvicorn

from .schemas.api_info import ApiInfo
from .config import config
from .routes import user, auth

# TODO: add alembic workflow
# TODO: validate tests
# TODO: add user cleanup
# TODO: add verificatoin cleanup
# TODO: create cleanup tests


app = FastAPI(
    title="Custom Courseware API",
    version="0.1.0",
    summary="REST API for interacting with Custom Courseware data"
)


@app.get('/', tags=["API Info"])
async def info() -> ApiInfo:
    """ Returns API info """
    return ApiInfo(
        title=app.title,
        version=app.version,
        summary=app.summary,
        spec=app.openapi_url,
        docs=app.docs_url
    )


if __name__ == '__main__':
    uvicorn.run(
        app,
        host=config.host,
        port=config.port,
        log_level=config.log_level,
        reload=config.reload
    )
