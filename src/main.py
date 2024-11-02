""" Custom Courseware API entrypoint """
from fastapi import FastAPI
from .schemas.api_info import ApiInfo


app = FastAPI(
    title="Custom Courseware API",
    version="0.0.1",
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
