from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from django.contrib import messages

from . import config
from .forms import ContactForm


User = get_user_model()


class IndexView(TemplateView):

    template_name = 'index.html'


def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    elif request.method == 'POST':
        messages.error(request, config.MESSAGE_INVALID_FORM)
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)


index = IndexView.as_view()




