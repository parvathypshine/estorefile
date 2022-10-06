
from django.contrib import admin
from django.urls import path
# from api.views import ProductsView,morning,AddView,SubView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter
from api.views import CubeView,NumCheck,Fact,WordCountView,ProductsView,ProductDetailsView,ReviewDetailsView,ReviewView,ProductsViewsetView,ProductModelviewsetview,ReviewModelViewsetView,UserView
router=DefaultRouter()
router.register("api/v1/products",ProductsViewsetView,basename="products")
router.register("api/v2/products",ProductModelviewsetview,basename="books")
router.register("api/v3/reviews",ReviewModelViewsetView,basename="review")
router.register("register",UserView,basename="user")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cube',CubeView.as_view()),
    path('num',NumCheck.as_view()),
    path('fact',Fact.as_view()),
    path('wordcount',WordCountView.as_view()),
    path('products', ProductsView.as_view()),
    path("products/<int:id>",ProductDetailsView.as_view()),
    path("review",ReviewView.as_view()),
    path("review/<int:id>",ReviewDetailsView.as_view()),
    path("reviews/<int:id>",ReviewDetailsView.as_view()),
    path("token/",ObtainAuthToken.as_view())

    # path('products',ProductsView.as_view()),
    # path('morning',morning.as_view()),
    # path('add',AddView.as_view()),
    # path('sub',SubView.as_view())

]+router.urls
