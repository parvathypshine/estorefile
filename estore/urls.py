
from django.contrib import admin
from django.urls import path
# from api.views import ProductsView,morning,AddView,SubView
from api.views import CubeView,NumCheck,Fact,WordCountView,ProductsView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cube',CubeView.as_view()),
    path('num',NumCheck.as_view()),
    path('fact',Fact.as_view()),
    path('wordcount',WordCountView.as_view()),
    path('products', ProductsView.as_view())

    # path('products',ProductsView.as_view()),
    # path('morning',morning.as_view()),
    # path('add',AddView.as_view()),
    # path('sub',SubView.as_view())

]
