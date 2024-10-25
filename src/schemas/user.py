from .schema_base import SchemaBaseModel

class User(SchemaBaseModel):
    """ Available User Information """
    username: str
    email: str
    first_name: str
    last_name: str
