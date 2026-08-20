from pluggle.enums import PluggleIOType
from pluggle.models.dto import InputArgs

from pluggle_api.schemas.input import InputFormData


def build_input_args(form: InputFormData) -> InputArgs:

    return InputArgs(
        source_type=form.source_type,
        source_address=form.source_address,
        source_table=None,
        transform_strategy_name=form.strategy,
        target_type=PluggleIOType.FILE,
        target_address=form.target_address,
        target_table=None,
        target_format=form.target_format,
    )
