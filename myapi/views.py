from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PersonSerializer
from .models import Person


@api_view(['GET', 'POST'])
def people(request):
    if request.method == 'GET':
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(age=Person.calculate_age(str(request.data.get("iin"))))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def people_detail(request, iin):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Person.objects.get(iin=iin)
    except Person.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        serializer = PersonSerializer(snippet)
        return JsonResponse(serializer.data)
