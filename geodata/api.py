from django.contrib.gis.geos import Point
from django.db import connection
from models import GeoDataLog


def _dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


class GeoDataApi(object):
    @classmethod
    def add_geolog(cls, lat, lng):
        point = Point(float(lat), float(lng))
        GeoDataLog.objects.create(latlng=point)

    @classmethod
    def get_nearset_logs(cls, lat, lng, latlng_range=0.2, length_limit_km=1, limit=20):
        lat = float(lat)
        lng = float(lng)

        sql = """
SELECT
    id AS id,
    GLength(
        GeomFromText(
            CONCAT(
                'LineString({lat} {lng},',
                X(latlng),
                ' ',
                Y(latlng),
                ')'
            )
        )
    ) AS length_km,
    X(latlng) AS lat,
    Y(latlng) AS lng
FROM geodata_geodatalog
WHERE
    MBRContains(
        GeomFromText(
            Concat(
                'LineString(',
                {lat} + {latlng_range},
                ' ',
                {lng} + {latlng_range},
                ',',
                {lat} - {latlng_range},
                ' ',
                {lng} - {latlng_range},
                ')'
            )
        ),
        latlng
    )
HAVING
    length_km < {length_limit_km}
ORDER BY length_km
LIMIT {limit}
""".format(
            lat=lat,
            lng=lng,
            latlng_range=latlng_range,
            length_limit_km=length_limit_km,
            limit=limit
        )

        cursor = connection.cursor()
        cursor.execute(sql)
        return _dictfetchall(cursor)
