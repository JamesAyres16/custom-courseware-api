""" contains project base model """
from pydantic import BaseModel, ConfigDict

class SchemaBaseModel(BaseModel):
    """ default module configuration """
    model_config = ConfigDict(extra='forbid', frozen=True)
