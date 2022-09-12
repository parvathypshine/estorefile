from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
# class ProductsView(APIView):
#     def get(self,request,*args,**kwargs):
#         return Response({'msg':'inside product get'})
#
# class morning(APIView):
#     def get(self,request,*args,**kwargs):
#
#         return Response({'msg':'good morning'})
#
# # class AddView(APIView): sep13
# #     def get(self, request, *args, **kwargs):
# #         num1=int(input('enter'))
# #         num2=int(input('enter'))
# #         res=num1+num2
# #         return Response({'result':res})
# class AddView(APIView):
#     def post(self,request,*args,**kwargs):
#         n1=request.data.get('num1')
#         n2=request.data.get("num2")
#         res=int(n1)+int(n2)
#         return Response({'msg':res})
#
# class SubView(APIView):
#     def post(self, request, *args, **kwargs):
#         n1=request.data.get('num1')
#         n2=request.data.get('num2')
#         res = int(n1)-int(n2)
#         return Response({'msg': res})
class CubeView(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get('num'))
        res=n**3
        return Response({'result':res})
class NumCheck(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get('num'))
        if n%2==0:

            return Response({'result':'even'})
        else:

            return Response({'result':"odd"})# Response data=res

class Fact(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get('num'))
        res=1
        for i in range(1,n+1):
            res=res*i
        return Response(data=res)
class WordCountView(APIView):
    def post(self,request,*args,**kwargs):
