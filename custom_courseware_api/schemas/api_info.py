""" contains API info schema """
from .schema_base import SchemaBaseModel

class ApiInfo(SchemaBaseModel):
    """ API info schema """
    title: str
    version: str
    summary: str
    spec: str
    docs: str
