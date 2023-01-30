from django.shortcuts import render
from .forms import Upload
from django.http import HttpResponse



def home(request):
    form = Upload()
    return render(request, 'home.html', {'form':form})


def processa_form(request):
    Upload(request.POST,request.FILES)
    upload_data = request.FILES['file']
    data = upload_data.read()
    to_string = data.decode()
    array_dados = to_string.split("\n")
    for dados in array_dados:
        tipo = dados[0:1]
        data = dados[1:9]
        valor = dados[9:19]
        cpf = dados[19:30]
        cartao = dados[30:42]
        hora_transacao = dados[42:48]
        dono_loja = dados[48:62]
        nome_loja = dados[62:81]

        print(
            f"Tipo: {tipo} | Data: {data} | Valor: {valor} | Cpf: {cpf} | Cartao: {cartao} | Hora: {hora_transacao} | Dono: {dono_loja} | Loja: {nome_loja}"
        )
 
    return HttpResponse("test")
