from typing import Optional
from pydantic import BaseModel as SchemaBaseModel

class CursoSchema(SchemaBaseModel):
  id: Optional[int] = None
  titulo: str
  aulas: int
  horas: int

  class Config:
    from_attributes = True
