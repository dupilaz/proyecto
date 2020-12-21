from django.shortcuts import render
from django.utils import timezone
from .models import consulta
from .forms import PostForm
from django.shortcuts import redirect


# Create your views here.
def principal(request):
    return render(request, 'ventas/principal.html', {})


def formulario(request):
    form = PostForm()
    return render(request, 'ventas/formulario.html', {'form': form})
def loguin(request):
    return render(request, 'ventas/loguin.html', {})    
        

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'ventas/formulario.html', {'form': form})  


def login(request):
    if request.method == "POST":
        if request.POST['password'] == "123" and request.POST['username']=="oscar":
            request.session['member_id'] = "oscar"
            return redirect('/', user=request.session.get('member_id'))
        else:
            return redirect('/ventas/loguin')
    else:
        form = PostForm()
    return render(request, 'ventas/loguin.html', {'form': form})  

def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")           