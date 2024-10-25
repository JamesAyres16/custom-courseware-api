""" Module Contains Contains for Form Errors """
from ..schema_base import SchemaBaseModel


class FieldError(SchemaBaseModel):
    """ Field Error Container """
    name: str
    input: str
    error: str

class FormError(SchemaBaseModel):
    """ Form Error Container """
    fields: list[FieldError]
