import uuid

from pydantic import BaseModel, ConfigDict, AliasGenerator, confloat
from pydantic.alias_generators import to_camel

student_dict = {
    'id': str(uuid.uuid4()),
    'name': 'Benito',
    'averageScore': 3.5,
    'department': 'ПОАС'
}

student_with_invalid_avg_score_dict = {
    'id': str(uuid.uuid4()),
    'name': 'Benito',
    'averageScore': 5.2, # or less than 2.0
    'department': 'ПОАС'
}


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
    department: str

print(Student(**student_dict))
print(Student(**student_with_invalid_avg_score_dict))
