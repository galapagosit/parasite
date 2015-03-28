from django.http import JsonResponse
from api import GeoDataApi

# Create your views here.


def checkin(request):

    GeoDataApi.add_geolog(request.POST['lat'], request.POST['lng'])

    logs = GeoDataApi.get_nearset_logs(
        request.POST['lat'],
        request.POST['lng']
    )

    return JsonResponse({'nearest_players': logs})
