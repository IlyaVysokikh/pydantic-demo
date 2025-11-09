from pydantic import BaseModel, ConfigDict

class MutableGeoPoint(BaseModel):
    lat: float
    lon: float
    
# point = MutableGeoPoint(lat=1234.5, lon=12414.4)
# print(point)
# point.lat = None
# print(point)


class ImmutableGeoPoint(BaseModel):
    model_config = ConfigDict(frozen=True)
    
    lat: float
    lon: float
    name: list[str]
    
immutable_geo_point = ImmutableGeoPoint(lat=1234.5, lon=12414.4, name=[])
immutable_geo_point.name.append('Kurgan')


class FlexibleGeoPoint(BaseModel, extra='allow'):
    lat: float
    lon: float


flexible_geo_point_data = {
    'lat': 123.4,
    'lon': 123.4,
    'name': 'Kurgan'
}

flexible_geo_point = FlexibleGeoPoint(**flexible_geo_point_data)
# print(flexible_geo_point.name)


class StrictGeoPoint(BaseModel, extra='forbid'):
    lat: float
    lon: float
    
# strict_geo_point = StrictGeoPoint(**flexible_geo_point_data)


class IgnoreExtraGeoPoint(BaseModel, extra='ignore'):
    lat: float
    lon: float
    
ignore_extra = IgnoreExtraGeoPoint(**flexible_geo_point_data)

print(ignore_extra.name)