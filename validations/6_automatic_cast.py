from pydantic import BaseModel

class GeoPoint(BaseModel):
    lat: float
    lon: float
    
point = {
    "lat": "12.345",
    "lon": "12.345"
}
geo_point = GeoPoint(**point)

print(type(geo_point.lat))
