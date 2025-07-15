

from pydantic import BaseModel

class AdvertisingInput(BaseModel):
    TV: float
    radio: float
    newspaper: float
    
# Pydantic ensures that any JSON request sent to your API is properly formatted, with the right data types.