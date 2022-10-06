from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import BookSerializer,ReviewSerializer,UserSerializer,CartSerializer
from api.models import Books,Reviews,Cart
from rest_framework.viewsets import ViewSet,ModelViewSet

from django.contrib.auth.models import User
from rest_framework import authentication,permissions
from rest_framework.decorators import action
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
        txt=request.data.get("text")
        words=(txt.split(" "))
        wc={}
        for w in words:
            if w in wc:
                wc[w]+=1
            else:
                wc[w]=1
        return Response(data=wc)

class ProductsView(APIView):
    # def post(self, request, *args, **kwargs):
    #     bname=request.data.get('name')
    #     bauthor = request.data.get('author')
    #     bprice= request.data.get('price')
    #     bpublisher= request.data.get('publisher')
    #     Books.objects.create(name=bname,author=bauthor,price=bprice,publisher=bpublisher)
    #     return Response(data="created")

    def get(self, request, *args, **kwargs):
        qs=Books.objects.all()
        serializer=BookSerializer(qs,many=True)
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            Books.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        #     print(serializer.validated_data)
        # else:
        #     return Response(data=serializer.errors)
        # return Response(data="created")


    # Books.objects.data(**serializer.validated_data)
    #         return Response(data=serializer.data)
    #     else:
    #         return Response(data=serializer.errors)

class ProductDetailsView(APIView):
    def get(self, request, *args, **kwargs):
        id=kwargs.get("id")
        book=Books.objects.get(id=id)
        serializer=BookSerializer(book,many=False)
        return Response(data=serializer.data)

    def delete(self, request, *args, **kwargs):
            id=kwargs.get("id")
            Books.objects.get(id=id).delete()
            return Response(data="deleted")
    def put(self, request, *args, **kwargs):
        id=kwargs.get('id')
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            Books.objects.filter(id=id).update(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class ReviewView(APIView):
    def get(self, request, *args, **kwargs):
        reviews=Reviews.objects.all()
        serializer=ReviewSerializer(reviews,many=True)
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer=ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class ReviewDetailsView(APIView):
    def get(self,request, *args, **kwargs):
        id=kwargs.get("pk")
        qs=Reviews.objects.get(id=id)
        serializer=ReviewSerializer(qs,many=False)
        return Response(data=serializer.data)

    def put(self,request, *args, **kwargs):
        id=kwargs.get("pk")
        object=Reviews.objects.get(id=id)
        serializer=ReviewSerializer(instance=object,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def delete(self,request, *args, **kwargs):
        id=kwargs.get("pk")
        Reviews.objects.get(id=id).delete()
        return Response(data="deleted")

class ProductsViewsetView(ViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]



    def list(self,request,*args,**kwargs):
        qs=Books.objects.all()
        serializer=BookSerializer(qs,many=True)
        return Response(data=serializer.data)
    def create(self,request,*args,**kwargs):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        book=Books.objects.get(id=id)
        serializer=BookSerializer(book,many=False)
        return Response(data=serializer.data)
    def update(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        book=Books.objects.get(id=id)
        serializer=BookSerializer(instance=book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Books.objects.get(id=id).delete()
        return Response(data="deleted")
    @action(methods=['POST'],detail=True)
    def add_review(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        book=Books.objects.get(id=id)
        user=request.user
        Reviews.objects.create(book=book,user=user,comment=request.data.get('comment'),rating=request.data.get('rating'))
        return Response(data="created")

    @action(methods=['GET'],detail=True)
    def get_review(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        book=Books.objects.get(id=id)
        reviews=book.reviews_set.all()
        serializer=ReviewSerializer(reviews,many=True)
        return Response(data=serializer.data)

    @action(methods=["POST"],detail=True)
    def addto_cart(self,request,*args,**kwargs):
        id = kwargs.get('pk')
        book = Books.objects.get(id=id)
        Cart.objects.create(book=book,user=request.user,status=request.data.get('options'))
        return Response(data="created")

    # @action(methods=['GET'],detail=True)
    # def cart_list(self,request,*args,**kwargs):
    #     cart=Cart.objects.all()
    #     cart_list=cart.books_set.all()
    #     serializer=CartSerializer(cart_list,many=True)
    #     return Response(data=serializer.data)


    # @action(methods=['POST'],detail=True)
    # def add_cart(self,request,*args,**kwargs):
    #     id=kwargs.get('pk')
    #     book=Books.objects.get(id=id)
    #     return Response(data='added to cart')
    #

class ProductModelviewsetview(ModelViewSet):
    serializer_class = BookSerializer

    queryset=Books.objects.all()

class ReviewModelViewsetView(ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Reviews.objects.all()

    def list(self, request, *args, **kwargs):
        all_reviews=Reviews.objects.all()

        if "user" in request:
            all_reviews=all_reviews.filter(user=request.query_params.get('user'))
            serializer = ReviewSerializer(all_reviews, many=True)
            return Response(data=serializer.data)
# check reviewmodelview#

class UserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


