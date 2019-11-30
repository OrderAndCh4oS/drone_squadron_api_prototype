from drone_squadron.validation_model.base_validation_model import BaseValidationModel
from drone_squadron.validation.field import Field
from drone_squadron.validation.validations import IsRequired, IsString, MinLength, MaxLength, MinValue, MaxValue


class SquadronValidationModel(BaseValidationModel):

    def __init__(self, name, scrap):
        super().__init__()
        self.name = Field(name) \
            .add(IsRequired("Must enter a name")) \
            .add(IsString("Must be a valid string")) \
            .add(MinLength(3, "Must have at 3 letters")) \
            .add(MaxLength(80, "Must not exceed 80 letters"))

        self.scrap = Field(scrap) \
            .add(MinValue(0, "Not enough scrap")) \
            .add(MaxValue(100000, "Reached scrap storage limit"))

    def validate(self):
        self.check_field('name', self.name.validate())
        self.check_field('scrap', self.scrap.validate())
        return self.is_valid()
