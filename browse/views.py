from django.shortcuts import render, get_object_or_404
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

def skill_view(request, username=None, skill_name=None):
    user = get_object_or_404(UserProfile, username)
    profile = user.userprofile
    skills = profile.skills.all()

    if skill_name:
        skill = get_object_or_404(skills, name=skill_name)
        return render(request, 'browse/skill_detail.html', {
            'user': user,
            'skill': skill,
        })
    else:
        return render(request, 'browse/skills_by_user.html',{
            'user': user,
            'skills': skills,
        })
    
def reverse_skill_view(request, skill_name=None, username=None):
    skill = get_object_or_404(Skill, name=skill_name)
    users = UserProfile.objects.filter(userprofile_skills=skill)

    if username:
        user = get_object_or_404(users, username=username)
        return render(request, 'browse/skill_detail.html', {
            'user': user,
            'skills': skill,
        })
    else:
        return render(request, 'browse/user_by_skill.html', {
            'skill': skill,
            'users': users,
        })