import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

from pydantic import BaseModel, ConfigDict, Field, constr

Base = declarative_base()


class StudentOrm(Base):
    __tablename__ = 'students'
    
    id = sa.Column('id', sa.Integer, primary_key=True)
    name = sa.Column('name', sa.String(20))
    
    
class StudentModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: constr(max_length=20)



# Reserved names
class MyModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    metadata: dict[str, str] = Field(alias='metadata_')


class SQLModel(Base):
    __tablename__ = 'my_table'
    id = sa.Column('id', sa.Integer, primary_key=True)
    # 'metadata' is reserved by SQLAlchemy
    metadata_ = sa.Column('metadata', sa.JSON)


sql_model = SQLModel(metadata_={'key': 'val'}, id=1)

pydantic_model = MyModel.model_validate(sql_model)

print(pydantic_model.model_dump())
#> {'metadata': {'key': 'val'}}
print(pydantic_model.model_dump(by_alias=True))
#> {'metadata_': {'key': 'val'}}