from .models import Location

def locations(_request):
  locations = Location.objects.all()
  return {'locations': locations}
