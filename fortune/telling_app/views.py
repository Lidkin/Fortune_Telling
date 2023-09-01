from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

import random

class GetRandomquote(APIview):
    def pick_random_object(tytle):
        return random.randrange(1, Quots.objects.get(tytle=tytle).count() + 1)

    def get(self, request, tytle:str):
        pk = Books.objects.get(tytle=tytle)
        try:
            item = Quote.objects.get(pk=pk)
            serializer = RentalSerializer(item, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist as e:    
            return Response({"message":str(e)}, status=status.HTTP_404_NOT_FOUND)    
