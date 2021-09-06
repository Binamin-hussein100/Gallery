from django.db.models import query
from gallery.models import Category, Image
from django.shortcuts import render
from django.db.models import Q

# Create your views here.
def images_all(request):
    store = Image.all_images()
    binamin = Category.objects.all()
    return render(request,'all-images/mixed.html', {"store":store,"binamin":binamin})

def details(request,pk):
    eachImage = Image.objects.get(id=pk)
    return render(request,'all-images/each.html',{"eachImage":eachImage})
def search(request):
    
    if request.method == "GET":
            query = request.GET.get('q')
            if query:
                display = Image.objects.filter(Q(name__icontains = query)|Q(category__pic_type__icontains = query)|Q(location__location__icontains = query))
                return render(request,'all-images/search.html', {"display":display})
            else:
                print("no data found")
                return render(request,'all-images/search.html',{})
    
    # q = request.GET.get('q',None)
    # items = ''
    # if q is None or q is "":
    #     display = Image.objects.all()
    # elif q is not None:
    #     display = Image.objects.filter(name__icontains = q)
    # return render(request,'all-images/search.html',{'display':display})
    
    
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