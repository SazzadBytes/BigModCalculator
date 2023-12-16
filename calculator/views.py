from django.shortcuts import render

# Create your views here.

def index(request):
    answer={}
    ans=0
    try:
        if request.method=='POST':
            Base=int(request.POST.get('base'))
            Ex=int(request.POST.get('ex'))
            Div=int(request.POST.get('div'))
            ans=pow(Base, Ex ,Div)
            answer={
                'ans':ans,
                'base':Base,
                'ex':Ex,
                'div':Div
            }

            
 
    except:
        pass

    return render(request,'index.html',answer)

