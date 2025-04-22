from django.shortcuts import render
from core.models import ProductionData
from django.db.models import Sum, Count
from datetime import date, timedelta
from django.utils.timezone import now
import json

def home_view(request):
        production_data = ProductionData.objects.select_related('line', 'shift', 'product').all()
        context = {
            'production_data': production_data,
        }
        return render(request, 'home.html', context)

def dashboard_view(request):
    selected_date_str = request.GET.get('date')
    
    if selected_date_str:
        selected_date = date.fromisoformat(selected_date_str)
    else:
        selected_date = date.today()
        
    current_month = selected_date.month
    current_year = selected_date.year

    energy_today = ProductionData.objects.filter(date=selected_date).aggregate(total=Sum('total_energy_consumed'))['total'] or 0
    energy_month = ProductionData.objects.filter(date__month=current_month, date__year=current_year).aggregate(total=Sum('total_energy_consumed'))['total'] or 0
    products_per_month = ProductionData.objects.filter(date__month=current_month, date__year=current_year).aggregate(total=Sum('total_production'))['total'] or 0

    # Production per line
    line_data = ProductionData.objects.filter(date=selected_date)\
        .values('line__line_name')\
        .annotate(total=Sum('total_production'))

    line_labels = [item['line__line_name'] for item in line_data]
    line_totals = [item['total'] for item in line_data]

    # Production per shift
    shift_data = ProductionData.objects.filter(date=selected_date)\
        .values('shift__shift_name')\
        .annotate(total=Sum('total_production'))

    shift_labels = [item['shift__shift_name'] for item in shift_data]
    shift_totals = [item['total'] for item in shift_data]
    
    
    product_data = ProductionData.objects.filter(date=selected_date)\
        .values('product__product_name')\
        .annotate(total=Sum('total_production'))
    
    
    product_labels = [item['product__product_name'] for item in product_data]
    product_totals = [item['total'] for item in product_data]

    context = {
        'energy_today': energy_today,
        'energy_month': energy_month,
        'line_labels': json.dumps(line_labels),
        'line_totals': line_totals,
        'shift_labels': json.dumps(shift_labels),
        'shift_totals': shift_totals,
        'product_labels': json.dumps(product_labels),
        'product_totals': product_totals,
        'selected_date': selected_date.strftime('%d-%m-%Y'),
        'current_month': selected_date.strftime('%B %Y'),
        'products_per_month': products_per_month,
        'total_production_today': ProductionData.objects.filter(date=selected_date).aggregate(total=Sum('total_production'))['total'] or 0,
    }
    print(context)
    return render(request, 'dashboard.html', context)


