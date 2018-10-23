from drone_squadron.model.base_model import BaseModel
from drone_squadron.validation.drone_validation import SquadCanAffordPurchase
from drone_squadron.validation.field import Field
from drone_squadron.validation.validations import IsRequired, IsString, MinLength, MaxLength


class DroneModel(BaseModel):

    def __init__(self, name, squad, cost):
        super().__init__()
        self.name = Field(name) \
            .add(IsRequired("Must enter a name")) \
            .add(IsString("Must be a valid string")) \
            .add(MinLength(3, "Must have at 3 letters")) \
            .add(MaxLength(80, "Must not exceed 40 letters"))
        self.purchase = Field((squad, cost)) \
            .add(SquadCanAffordPurchase())

    def validate(self):
        self.check_field('name', self.name.validate())
        self.check_field('message', self.purchase.validate())
        return self.is_valid()
