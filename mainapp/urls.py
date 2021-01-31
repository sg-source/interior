from django.urls import path
import mainapp.views as mainapp
app_name = 'mainapp'
urlpatterns = [
    path('', mainapp.product, name='index'),
    path('category/<int:pk>/', mainapp.product, name='category'),
    path('category/<int:pk>/<int:page>/', mainapp.product, name='page'),
    path('product-details/<int:pk>/', mainapp.product_details, name='product-details')

    # path('all', mainapp.product, name='products_all'),
    # path('home', mainapp.product, name='products_home'),
    # path('office', mainapp.product, name='products_office'),
    # path('furniture', mainapp.product, name='products_furniture'),
    # path('modern', mainapp.product, name='products_modern'),
    # path('classic', mainapp.product, name='products_classic')
]
