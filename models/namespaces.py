import warnings

from pydantic import BaseModel, ConfigDict

warnings.filterwarnings('error')  # Raise warnings as errors

try:

    class Model(BaseModel):
        model_prefixed_field: str
        also_protect_field: str

        model_config = ConfigDict(
            protected_namespaces=('protect_me_', 'also_protect_')
        )

except UserWarning as e:
    print(e)