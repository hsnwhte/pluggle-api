import uuid

from pluggle.enums import ContentFormat, PluggleIOType
from pydantic import BaseModel
from pydantic.fields import computed_field

from pluggle_api.settings import OUTPUTS_DIR


class InputFormData(BaseModel):
    strategy: str
    source_url: str | None
    source_filepath: str | None
    target_format: ContentFormat

    @computed_field
    @property
    def source_type(self) -> PluggleIOType:
        if self.source_filepath:
            return PluggleIOType.FILE
        elif self.source_url:
            return PluggleIOType.API
        else:
            raise ValueError

    @computed_field
    @property
    def source_address(self) -> str:
        if self.source_type == PluggleIOType.FILE and self.source_filepath:
            return self.source_filepath
        elif self.source_type == PluggleIOType.API and self.source_url:
            return self.source_url
        else:
            raise ValueError

    @computed_field
    @property
    def target_address(self) -> str:
        filename = f"{uuid.uuid7()}.{self.target_format.value}"
        return str(OUTPUTS_DIR / filename)
