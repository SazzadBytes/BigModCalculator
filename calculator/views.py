from django.shortcuts import render
from decimal import Decimal

# Create your views here.

def index(request):
    answer = {}
    ans = 0
    try:
        if request.method == 'POST':
            base_str = request.POST.get('base')
            ex_str = request.POST.get('ex')
            div_str = request.POST.get('div')

            try:
                base = Decimal(base_str)
                ex = Decimal(ex_str)
                div = Decimal(div_str)
                ans = pow(base, ex, div)  
            except InvalidOperation:
                answer = {'error': 'Invalid input values'}
                return render(request, 'index.html', answer)

            answer = {
                'ans': ans,
                'base': base,
                'ex': ex,
                'div': div
            }

    except Exception as e:
        answer = {'error': f'An error occurred: {e}'}

    return render(request, 'index.html', answer)
