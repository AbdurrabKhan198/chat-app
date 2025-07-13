from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request, 'chat/index.html')



def user(request):
    return render(request, 'chat/user.html')

def chat(request):
    username = request.GET.get('username')

    if username:
        request.session['username'] = username
    else:
        username = request.session.get('username')

    if not username:
        return redirect('user')

    return render(request, 'chat/chat.html', {'username': username})