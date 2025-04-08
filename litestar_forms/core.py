from typing import Annotated, Any

from litestar.enums import RequestEncodingType
from litestar.params import Body
from pydantic import BaseModel, ValidationError, ConfigDict, field_validator


_FormData = dict[str, Any]
FormData = Annotated[_FormData, Body(media_type=RequestEncodingType.URL_ENCODED)]


class PydanticErrorItem(BaseModel):
    model_config = ConfigDict(
        extra="ignore"
    )
    type: str
    loc: str
    input: Any

    @field_validator("loc", mode="before")
    @classmethod
    def loc_field(cls, v: list[str]) -> str:
        return str(v[0])



class Form:
    __model__: type[BaseModel]

    def __init__(self, raw_data: _FormData) -> None:
        self.raw_data = raw_data
        self.errors: list[PydanticErrorItem] = []
        self.model_instance: type[BaseModel] | None = None
        try:
            self.model_instance = self.__model__.model_validate(raw_data)
        except ValidationError as e:
            self.errors.extend(PydanticErrorItem.model_validate(d) for d in e.errors())

    def is_valid(self) -> bool:
        return bool(self.model_instance)




