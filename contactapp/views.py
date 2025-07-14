
from django.shortcuts import render, redirect

from .forms import ContactForm
from .models import ContactMessage

def contact_index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thankyou_page')

        
    else:
        form = ContactForm()
    return render(request, 'contact_templates/contact_index.html', {'form': form})

def thankyou_page(request):
    submissions = ContactMessage.objects.all().order_by('-created_at')
    return render(request, 'contact_templates/thankyou_page.html', {'submissions': submissions})