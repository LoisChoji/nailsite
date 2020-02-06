from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Allpolishes
from django.template import loader

# Create your views here.
def nails(request):
    np = Allpolishes.objects.all()
    template = loader.get_template('NailPolishes/nails.html')
    # the context is a dictionary mapping template variable name
    context ={
        'np':np,
    }
    #nb: we almost always render request in django
    return HttpResponse(template.render(context, request))

def detail(request, nail_id): 
    #an exception for when someone requests for a polish    
   polish = get_object_or_404(Allpolishes, pk=nail_id)
   return render(request, 'NailPolishes/detail.html', {'polish': polish})

def yourchoice(request, nail_id):
    polish = get_object_or_404(Allpolishes, pk = nail_id)
    try:
        selected_nailtype = polish.polishdetails_set.get(pk = request.POST['choice'])
    except (KeyError, Allpolishes.DoesNotExist):
        return render(request, 'Allpolishes/detail.html',{

            'polish': polish,
            'error_message':"please select a valid option",
        })
    else:
        selected_nailtype.your_choice = True
        selected_nailtype.save()
        return render(request, 'NailPolishes/detail.html', {'polish':polish})



















