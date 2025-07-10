from django.shortcuts import render, redirect
#from skills.models import Skills
#from user_authentication.models import UserProfile
#from ratings.models import Rating


# Create your views here.
def browse(request):
    sort = request.GET.get('sort', 'username')
    order = request.GET.get('order', 'asc').lower()

    if sort not in ['username', 'email', 'webpage']:
        sort = 'username'
    if order not in ['asc', 'desc']:
        order = 'asc'

    sort_key = sort if order == 'asc' else f'-{sort}'
    users = UserProfile.objects.select_related('webpage').order_by(sort_key)

    print("Requested sort:", sort, "order:", order)
    return render(request, 'user_list.html', {
        'users': users,
        'current_sort': sort,
        'current_order': order
    })
