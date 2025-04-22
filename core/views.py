from django.http import JsonResponse
from .models import ProductionData, Product,User

def production_logs_json(request):
    logs = ProductionData.objects.all().values(
        'id',
        'date',
        'line__line_name',
        'shift__shift_name',
        'product__product_name',
        'total_production',
        'total_energy_consumed',
        'created_by__username',
        'created_at'
    )

    return JsonResponse(list(logs), safe=False)

def get_single_log(request, log_id):
    try:
        log = ProductionData.objects.get(id=log_id)
        data = {
            'id': log.id,
            'date': log.date,
            'line': log.line.line_name,
            'shift': log.shift.shift_name,
            'product': log.product.product_name,
            'total_production': log.total_production,
            'total_energy_consumed': log.total_energy_consumed,
            'created_by': log.created_by.username if log.created_by else None,
            'created_at': log.created_at
        }
        return JsonResponse(data, safe=False)
    except ProductionData.DoesNotExist:
        return JsonResponse({'error': 'Log not found'}, status=404)

def get_all_products(request):
    products = Product.objects.all().values()
    return JsonResponse(list(products), safe=False)

def get_all_users(request):
    users = []

    for user in User.objects.all():
        user_permissions = user.user_permissions.all().values_list('codename', flat=True)

        users.append({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'is_staff': user.is_staff,
            'is_active': user.is_active,
            'date_joined': user.date_joined,
            'permissions': list(user_permissions),
        })

    return JsonResponse(list(users), safe=False)