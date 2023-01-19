from django.views.generic import TemplateView


class CoquiHomeView(TemplateView):
    template_name = "index.html"
