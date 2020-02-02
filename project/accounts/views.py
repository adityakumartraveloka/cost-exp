from django.shortcuts import render
# Create your views here.
from django.http import JsonResponse
from .models import ProductDomainIndex
from .serializers import ProductDomainIndexSerializer

def ProductDomainInfo(request):
    qeueryset = ProductDomainIndex.objects.all()
    # print(qeueryset)
    serializer = ProductDomainIndexSerializer(qeueryset, many=True)
    return JsonResponse(serializer.data, safe=False)
