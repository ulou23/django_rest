from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import Context
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from sendurls.models import Urlinput
from sendurls.serializers import UrlinputSerializer

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.http import Http404

from rest_framework.renderers import TemplateHTMLRenderer

class UrlinputList(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name='url_list.html'


    def get(self,request):
        request=Urlinput.objects.all()
        return Response({'list':request})

    def post(self,request,format=None):
        serializer=UrlinputSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UrlDetail(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name='url_list.html'############

    def get_object(self, pk):
        try:
            return Urlinput.objects.get(pk=id)
        except Urlinput.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        urlinput = self.get_object(pk)
        serializer = UrlinputSerializer(urlinput)
        return Response({'serializer':serializer, 'urlinput':urlinput})

    def put(self, request, pk, format=None):
        urlinput = self.get_object(pk)
        serializer = UrlinputSerializer(urlinput, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer':serializer,'urlinput':urlinput})
        serializer.save()
        return render('url_list.html')


    def delete(self, request, pk, format=None):
        urlinput = self.get_object(pk)
        urlinput.delete()
        return redirect('url-list')




#@csrf_exempt  # wszyscy dostep , nie maja csrf tokenu
#@api_view(['GET','POST'])
#def url_list(request):
#
#    if request.method == 'GET':
#        urlinputs = Urlinput.objects.all()
#        serializer = UrlinputSerializer(urlinputs, many=True)
#        #return JsonResponse(serializer.data, safe=False)
#        return Response(serializer.data)
#
#    elif request.method == 'POST':
#        data = JSONParser().parse(request)
#        serializer = UrlinputSerializer(data=data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data,status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#@api_view(['GET','PUT','DELETE'])
#def url_detail(request, pk):
#
#    try:
#        urlinput = Urlinput.objects.get(pk=pk)
#    except Urlinput.DoesNotExist:
#        #return HttpResponse(status=404)
#        return Response(status=status.HTTP_404_NOT_FOUND)
#
#    if request.method == 'GET':
#        serializer = UrlinputSerializer(urlinput)
#        return Response(serializer.data)
#
#    elif request.method == 'PUT':
#        data = JSONParser().parse(request)
#        serializer = UrlinputSerializer(urlinput, data=data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#    elif request.method == 'DELETE':
#        urlinput.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)
#


import json
from django.urls import resolve
from django.views.generic.base import View
