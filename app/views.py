from django.http import JsonResponse
from .models import drink
from .serializers import DrinkSerializer

def drink_list(request): # this is GET method

    # get all Drinks 
    # serialize them
    # return json

    all_drinks = drink.objects.all()
    serializer = DrinkSerializer(all_drinks, many=True)

    return JsonResponse({"drinks": serializer.data})