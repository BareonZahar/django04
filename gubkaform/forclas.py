from django import forms


class Mayforma(forms.Form):
    name = forms.CharField(label='Ваше имя')
    vozrast = (('ребенок','1-11 лет'),('подросток','12-16 лет '),('юноша','17-21 год'),('взрослый','21- год'))
    voz = forms.TypedChoiceField(choices=vozrast,label='Ваш возраст')
    yzu = (('русском','Ru'),('английском','En'),('французком','Fr'),('немецком','De'))
    yzuk = forms.TypedChoiceField(choices=yzu,label='Ваш родной язык')
    email = forms.EmailField(label='Ваш email',help_text='fir@dir.ru')
    povar = forms.BooleanField(label='Вы умеете готовить')
    keti = (('незнаю','Незнаю'),('да','Да'),('нет','Нет'))
    ket = forms.TypedChoiceField(choices=keti,label='Живете с котом')
    mul = (('незнаю','незнаю'),('очень','очень'),('терпимо','терпимо'),('нелюблю','нелюблю'))
    mult = forms.TypedChoiceField(choices=mul,label='Любите мультфильмы')
    img = forms.ImageField(label='Ты панда')


