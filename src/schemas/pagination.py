""" contains pagination schema """
from pydantic import Field

from .schema_base import SchemaBaseModel


class PaginationParams(SchemaBaseModel):
    """ params required for pagination """
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
