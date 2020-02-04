from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from datetime import datetime


from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from .serializers import RegisterAccessRequestSerializer
from .models import RegisterAccessRequest
# Create your views here.


# class RegisterAccessResquestView(APIView):
#     def get(self, request):
#         queryset = RegisterAccessRequest.objects.all()
#         serializer = RegisterAccessRequestSerializer(queryset, many=True)
#         return Response(serializer.data)


# def registeraccessrequestview(request):
#     queryset = RegisterAccessRequest.objects.all()
#     print(queryset)
#     serializer = RegisterAccessRequestSerializer(queryset, many=True)

#     return JsonResponse(serializer.data,safe=False)

@api_view(['GET', 'POST'])
@csrf_exempt
def registeraccessrequest(request):

    sender_mail = 'scomrip@gmail.com'
    requester_mail = request.data['email']
    admin_mail = 'aditya.16bit1031@abes.ac.in'
    subject_requester = 'Thank You for Requesting'
    msg_requester = 'You have raised a request for product_domains'
    msg_admim = 'You have got a request from ' + request.data['email']
    subject_admin = 'You got a new request, check here' + 'http://localhost:8000/admin'

    if request.method == 'GET':
        queryset = RegisterAccessRequest.objects.all()
        serializer = RegisterAccessRequestSerializer(queryset, many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == 'POST':
        print('[request.data]',request.data)
        try:
            instance = RegisterAccessRequest.objects.get(email=request.data['email'])
            serializer = RegisterAccessRequestSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            else:
                return JsonResponse(serializer.errors, status=400)


        except RegisterAccessRequest.DoesNotExist:            
            serializer = RegisterAccessRequestSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                # send_mail(subject_requester,
                # msg_requester,
                # sender_mail,
                # [requester_mail],
                # fail_silently=False)

                # send_mail(subject_admin,
                # 'A new tickets',
                # sender_mail,
                # [admin_mail],
                # fail_silently=False
                # )
                msg = 'Request has been created'
                return JsonResponse(serializer.data, status=201)
            else:
                errors = serializer.errors
                return JsonResponse(errors, status=400)




@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def registeraccessrequestupdate(request, id):
    try:
        instance = RegisterAccessRequest.objects.get(id=id)
        print('[instance] views.py', instance)
    except RegisterAccessRequest.DoesNotExist:
        return JsonResponse({'err': 'Given request is not found'}, status=404)

    if request.method == 'GET':
        serializer = RegisterAccessRequestSerializer(instance)
        return JsonResponse(serializer.data)
    
    if request.method == 'PUT':
        serializer = RegisterAccessRequestSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        instance.delete()
        return HttpResponse(status=204)


# def approverequest(request, id):
#     try:
#         instance = RegisterAccessRequest.objects.get(id=id)
#     except RegisterAccessRequest.DoesNotExist:
#         return JsonResponse({ 'err': 'Request is not found'}, status=404)

#     if request.method == 'POST':



