from django.views.generic import TemplateView




class Homepage(TemplateView):
    template_name = 'home/index.html'


class Testpage (TemplateView):
    template_name ='home/test.html'

class ThanksPage(TemplateView):
    template_name ='home/thanks.html'