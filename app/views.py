from django.http import JsonResponse
from .models import drink
from .serializers import DrinkSerializer
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def drink_list(request): # this is GET method

    # get all Drinks 
    # serialize them
    # return json

    if request.method == 'GET':

        all_drinks = drink.objects.all()
        serializer = DrinkSerializer(all_drinks, many=True)

        return Response({"drinks": serializer.data})
    
    if request.method == 'POST':

        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Drink created successfully!'}, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def drink_detail(request, id):
    try :
        drink_id = drink.objects.get(pk=id)
    except drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = DrinkSerializer(drink_id)

        return Response({"drink": serializer.data})
    
    elif request.method == 'PUT':

        serializer = DrinkSerializer(drink_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Drink updated successfully!'}, status=status.HTTP_200_OK)
        
    elif request.method == 'DELETE':

        serializer = DrinkSerializer(drink_id)
        serializer.delete()
        return Response({'message': 'Drink deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)