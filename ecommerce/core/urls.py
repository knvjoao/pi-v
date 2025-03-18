from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from carts.views import CartDetailView
from . import views


urlpatterns = [
    path('', lambda req: redirect('/produtos/'), name="home"),
    path('admin/', admin.site.urls),
    path('produtos/', include('produtos.urls')),
    path('clientes/', include('clientes.urls')),
    path('carrinho/<int:pk>/', CartDetailView.as_view()),
    path('para-sua-empresa/', views.para_sua_empresa, name='para_sua_empresa'),
    path('baixe-o-app/', views.baixe_o_app, name='baixe_o_app'),
    path('receba-hoje/', views.receba_hoje, name='receba_hoje'),
    path('cartao-de-credito/', views.cartao_de_credito, name='cartao_de_credito'),
    path('marcas-proprias/', views.marcas_proprias, name='marcas_proprias'),
    path('produtos-internacionais/', views.produtos_internacionais, name='produtos_internacionais'),
    path('venda-na-ecommerce/', views.venda_na_ecommerce, name='venda_na_ecommerce'),
    path('oferta/', views.oferta, name='oferta'),
    path('buscar/', views.buscar, name='buscar')
]

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, 
                    document_root=settings.MEDIA_ROOT)
