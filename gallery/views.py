from gallery.models import Category, Image
from django.shortcuts import render

# Create your views here.
def images_all(request):
    store = Image.all_images()
    binamin = Category.all_categories()
    return render(request,'all-images/mixed.html', {"store":store},)

def details(request):
    pass

def search(request):
    q = request.GET.get('q',None)
    items = ''
    if q is None or q is "":
        display = Image.objects.all()
    elif q is not None:
        display = Image.objects.filter(name__icontains = q)
    return render(request,'all-images/search.html',{'display':display})
    
    
    # TRY 2
    # display = Image.objects.all()
    # if 'q' in request.GET:
    #     q = request.GET['q']
    #     display = Image.objects.filter(name__icontains = q)
        
    #     return render(request,'all-images/search.html',{'display':display} )
    
    # TRY 3
    
    # results = []
    # if request.method == "GET":
    #     display = request.GET.get('search')
    #     print(display)
    #     results = Image.objects.filter(name__icontains = display)
    # return render(request,'search.html',{"display":display},{"results":results})