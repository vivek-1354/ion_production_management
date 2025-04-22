from django.urls import path
from .views import production_logs_json, get_single_log, get_all_products, get_all_users

urlpatterns = [
    path('api/production-data/', production_logs_json, name='production_logs_json'),
    path('api/production-data/<int:log_id>', get_single_log, name='production_logs_json'),
    path('api/products', get_all_products, name='production_logs_json'),
    path('api/users', get_all_users, name='production_logs_json')
]
