import math
from django.views.generic import TemplateView
from django.http import JsonResponse


class CalculatorView(TemplateView):
    template_name = 'mainapp/calculator.html'

    def post(self, request):
        n = int(request.POST.get('n'))
        # x = int(request.POST.get('x'))
        x = request.POST.get('x')
        if x is not None:
            x = int(x)

        calculator_type = request.POST.get('calculator_type')

        if calculator_type == 'gini':
            gini = 1 - (x / n) ** 2 - ((n - x) / n) ** 2
            result = {'result': gini}
        elif calculator_type == 'entropy':
            entropy = (x / n) * math.log10(n / x) + ((n - x) / n) * math.log10(n / (n - x))
            result = {'result': entropy}
        elif calculator_type == 'bientropy':
            n = n*0.1
            bientropy = n * math.log2(1/n) + (1-n) * math.log2(1/(1-n))
            result = {'result': bientropy}
        else:
            result = {'error': 'Invalid calculator type'}

        return JsonResponse(result)
