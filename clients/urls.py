from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('clients/', views.client, name='client_base'),
    path('client_info_list/', views.client_info_list, name='client_info_list'),
    path('add_client/', views.add_client, name='add_client'),

    path('addClientToDatabase/', views.addClientToDatabase, name='addClientToDatabase'),
    path('clients/<int:cid>/detail', views.client_detail, name='client_detail'),

    path('clients/update/<int:cid>/', views.update_client_detail, name='update_client_detail'),

    path('clients/client_add_project/<int:cid>/', views.client_add_project, name='client_add_project'),

    path('clients/client_add_bc/<int:cid>/', views.client_add_bc, name='client_add_bc'),
    path('clients/client_add_fc/<int:cid>/', views.client_add_fc, name='client_add_fc'),

    path('clients/bc_detail_update/<int:bc_id>/<int:cid>', views.bc_detail_update, name='bc_detail_update'),
    path('clients/fc_detail_update/<int:fc_id>/<int:cid>', views.fc_detail_update, name='fc_detail_update'),

    path('clients/delete_client/<int:cid>/', views.delete_client, name='delete_client'),
    path('clients/delete_client_bc/<int:bc_id>/<int:cid>/', views.delete_client_bc, name='delete_client_bc'),
    path('clients/delete_client_fc/<int:fc_id>/<int:cid>/', views.delete_client_fc, name='delete_client_fc'),

    path('clients/advanced_client/', views.advanced_client_form, name='advanced_client_form'),
    path('clients/search_client/', views.advanced_client_search, name='advanced_client_search'),
]
