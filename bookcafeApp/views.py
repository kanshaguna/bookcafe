from django.shortcuts import render
from bookcafeApp.forms import EnquiryForm
from bookcafeApp.models import Enquiry
from bookcafeApp.models import Menu

# Create your views here.

def home(request):
    menu = Menu.objects.all()

    form = EnquiryForm()
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
        return submitEnquiry(request)
    return render(request, 'bookcafeApp/index.html', {'menu': menu,'form': form})


def submitEnquiry(request):
    return render(request, 'bookcafeApp/submitEnquiry.html')