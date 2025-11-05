import uuid

from pydantic import BaseModel, Field, ConfigDict, AliasGenerator
from pydantic.alias_generators import to_camel

student_dict = {
    'id': str(uuid.uuid4()),
    'name': 'Benito',
    'averageScore': 3.5,
    'department': 'ПОАС'
}


class Student(BaseModel):
    id: uuid.UUID
    name: str
    averageScore: float
    department: str


print(Student(**student_dict))


class AliasedStudent(BaseModel):
    id: uuid.UUID = Field(alias='id')
    name: str = Field(alias='name')
    average_score: float = Field(alias='averageScore')
    department: str = Field(alias='department')

print(AliasedStudent(**student_dict))


class AliasesConfigureByConfigDictStudent(BaseModel):
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
    average_score: float
    department: str

print(AliasesConfigureByConfigDictStudent(**student_dict))
print(AliasesConfigureByConfigDictStudent(**student_dict).model_dump(by_alias=True))



