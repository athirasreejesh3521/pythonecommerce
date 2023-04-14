from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from . import views


app_name='shop'
urlpatterns = [

    path('', views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/', views.allProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail,name='prodCatDetail'),
]

if settings.DEBUG:
     urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
     urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)