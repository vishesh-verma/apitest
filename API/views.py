from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from API.models import ideator
from API.serializers import ideatorSerializer


@csrf_exempt

def apilist(request):

    if request.method == 'GET':
        api= ideator.objects.all()
        serializer=ideatorSerializer(api,many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data= JSONParser().parse(request)
        serializer =ideatorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def apidetails(request ,pk):
    try:
        api=ideator.objects.get(pk=pk)
    except api.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ideatorSerializer(api)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data= JSONParser().parse(request)
        serializer =ideatorSerializer(api,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        api.delete()
        return HttpResponse(status=204)
