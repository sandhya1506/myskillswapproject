from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .forms import AddSkillsForm, RequestSkillsForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    #return HttpResponse("<h1>It works</h1>")
   return render(request, 'index.html')

# def skillboard(request):
#     skills = AddSkills.objects.all()
#     return render(request, 'skills/skillboard.html', {'skills': skills})
# RequestSkills.objects.all()  #has to be DB object from models

def skillboard(request):
    addskills = AddSkillsForm() 
    getskills = RequestSkillsForm()
    return render(request, 'skills/skillboard.html', {'addskills': addskills, 'getskills':getskills})

#@login_required
def addSkills(request):
    if request.method == 'POST':
        print('INSIDE ADD POST.')
        added=AddSkillsForm(request.POST) #creates instance of ModelForm
        if added.is_valid():
            #added.save(commit=False) #create filled in instance of Model, do not commit
           # added.user=request.user  #add user to the form - is the connections CORRECT?? XX
            added.save()             #commit to DB
            return redirect('skills:skillboard')
        else:
            return redirect('skills:skillboard')
    else: #GET
        return redirect('skills:skillboard')
      
#@login_required
def reqSkills(request):
    if request.method == 'POST':
        print('INSIDE REQ POST.')
        req=RequestSkillsForm(request.POST) #creates instance of ModelForm
        print('PAST FORM REQ.')
        if req.is_valid():
            print('ITS VALID')
            req.save(commit=False) #create filled in instance of Model, do not commit
            #req.user=request.user  #add user to the form
            req.save()             #commit to DB
            return redirect('skills:skillboard')
        else:
            print('REQ NOT VALID.')
            return redirect('skills:skillboard')
    else: #GET
        return redirect('skills:skillboard')
        
