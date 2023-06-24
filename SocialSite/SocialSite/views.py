from django.views.generic import TemplateView


class TestPage(TemplateView):
    template_name = "myapp/test.html"


class ThanksPage(TemplateView):
    template_name = "myapp/thanks.html"


class HomePage(TemplateView):
    template_name = "myapp/index.html"
