
from django.shortcuts import render, redirect

from .forms import ContactForm
from .models import ContactMessage




SUBMISSIONS = []

def contact_index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)


        if form.is_valid():
           
            SUBMISSIONS.append(form.cleaned_data)
            return redirect('contactapp:thankyou_page')
    else:
        form = ContactForm()
    return render(request, 'contact_templates/contact_index.html', {'form': form})



def thankyou_page(request):
    return render(request, 'contact_templates/thankyou_page.html', {'submissions': SUBMISSIONS})
