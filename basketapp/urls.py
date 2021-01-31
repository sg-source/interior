from django.urls import path
import basketapp.views as basketapp
app_name = 'basketapp'
urlpatterns = [
    path( '', basketapp.basket, name='view'),
    path( 'add/<int:pk>', basketapp.basket_add, name='add'),
    path( 'remove/<int:pk>', basketapp.basket_remove, name='remove'),
    path('edit/<int:pk>/<int:quantity>/', basketapp.basket_edit, name='edit')


    # path('all', mainapp.product, name='products_all'),
    # path('home', mainapp.product, name='products_home'),
    # path('office', mainapp.product, name='products_office'),
    # path('furniture', mainapp.product, name='products_furniture'),
    # path('modern', mainapp.product, name='products_modern'),
    # path('classic', mainapp.product, name='products_classic')
]
