from django.shortcuts import render
def index(request):
    return render(request,'index.html')
from gubkaform.forclas import Mayforma
def final(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        voz = request.POST.get('voz')
        yzuk = request.POST.get('yzuk')
        email = request.POST.get('email')
        povar = request.POST.get('povar')
        ket = request.POST.get('ket')
        mult = request.POST.get('mult')
        img = request.FILES.get('img').read()
        print('все ввели')
        file = open('gubkaform/static/updar/{0}.jpg'.format(name),'wb')
        file.write(img)
        print('записали')
        fpath = 'updar/{0}.jpg'.format(name)
        data = {'k1': name,'k2':voz,'k3':yzuk,'k4':email,'k5':povar,'k6':ket,'k7':mult,'k8':fpath}
        print('готово к отправке')
        return render(request,'rezult.html',context=data)
    else:
        gubkaform = Mayforma()
    data = {'form': gubkaform}
    return render(request,'sety.html',context=data)

