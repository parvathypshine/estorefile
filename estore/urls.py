
from django.contrib import admin
from django.urls import path
from api.views import ProductsView,morning
urlpatterns = [
    path('admin/', admin.site.urls),
    path('products',ProductsView.as_view()),
    path('morning',morning.as_view())

]
