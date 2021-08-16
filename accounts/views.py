from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView



class RegisterView(CreateView):
    template_name = "form.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('index')