from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
class ProductsView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({'msg':'inside product get'})

class morning(APIView):
    def get(self,request,*args,**kwargs):

        return Response({'msg':'good morning'})