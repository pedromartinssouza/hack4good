from app.models import Localization

def assignMonitoring(pLat, pLongit):

    querySet = Localization.objects.filter(lat = pLat, longit = pLongit)

    querySet.update(monitoring = True)
    return list(querySet.values())