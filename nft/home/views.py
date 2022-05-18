from django.shortcuts import redirect, render
from .forms import NFTForm

# Create your views here.

def nft_create(request):
    form=NFTForm()

    if request.method=='POST':
        form=NFTForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()

        msg='Account created'
        return redirect('/index')


    return render(request,'create.html',{'form':form})