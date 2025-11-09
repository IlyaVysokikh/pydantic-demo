import datetime
import uuid
from datetime import timedelta
from enum import StrEnum
from typing import Annotated

from pydantic import (
    BaseModel,
    ConfigDict,
    AliasGenerator,
    confloat,
    field_validator, AfterValidator,
)
from pydantic.alias_generators import to_camel

class Department(StrEnum):
    POAS = 'ПОАС'


student_dict = {
    'id': str(uuid.uuid4()),
    'name': 'Benito',
    'averageScore': 3.5,
    'department': 'ПОАС',
    'dateBirth': '2000-01-01',
    'phone': '+7900000000'
}

student_with_invalid_phone_format = {
    "id": str(uuid.uuid4()),
    "name": "Benito",
    "averageScore": 3.5,
    "department": "ПОАС",
    "dateBirth": "2000-01-01",
    "phone": "8900000000",
}



def validate_phone(v: str) -> str:
    if not v.startswith('+7'):
        raise ValueError('Phone should be starts with +7')

    return v


Phone = Annotated[str, AfterValidator(validate_phone)]



class Student(BaseModel):
    model_config = ConfigDict(
        validate_by_name=True,
        validate_by_alias=True,
        alias_generator=AliasGenerator(
            validation_alias=to_camel,
            serialization_alias=to_camel,
        )
    )

    id: uuid.UUID
    name: str
    average_score: confloat(ge=2, le=5)
    department: Department
    date_birth: datetime.date
    phone: Phone


    @field_validator('date_birth')
    def ensure_18_or_over(cls, value):
        eighteen_years_ago = datetime.datetime.now() - timedelta(days=365*18)

        eighteen_years_ago = eighteen_years_ago.date()

        if value > eighteen_years_ago:
            raise ValueError('Too young')

        return value

# print(Student(**student_dict))
print(Student(**student_with_invalid_phone_format))