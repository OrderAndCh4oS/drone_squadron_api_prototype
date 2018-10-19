from drone_squadron.model.base_model import BaseModel
from drone_squadron.validation.field import Field
from drone_squadron.validation.validations import IsRequired, IsString, MinLength, MaxLength
from validation.drone_validation import SquadCanAffordPurchase


class DroneModel(BaseModel):

    def __init__(self, name, squad_and_cost):
        super().__init__()
        self.name = Field(name) \
            .add(IsRequired("Must enter a name")) \
            .add(IsString("Must be a valid string")) \
            .add(MinLength(3, "Must have at 3 letters")) \
            .add(MaxLength(80, "Must not exceed 40 letters"))
        self.purchase = Field(squad_and_cost) \
            .add(SquadCanAffordPurchase(squad_and_cost))

    def validate(self):
        self.check_field('name', self.name.validate())
        self.check_field('message', self.purchase.validate())
        return self.is_valid()
