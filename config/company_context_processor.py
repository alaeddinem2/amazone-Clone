from .models import company

def get_company_data(request):
    data = company.objects.last()
    return {'company_data': data}