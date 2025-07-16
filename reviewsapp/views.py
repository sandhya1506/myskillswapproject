from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from .models import Review

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_list')  
    else:
        form = ReviewForm()
    return render(request, 'reviewsapp/add_review.html', {'form': form})

@login_required
def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'reviewsapp/review_list.html', {'reviews': reviews})
