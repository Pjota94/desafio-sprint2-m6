from django.shortcuts import render
from cnab.models import FormData
from .forms import Upload

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
        
        data_tratada = f"{data[0:4]}/{data[4:6]}/{data[6:8]}"
        hora_tratada = f"{hora_transacao[0:2]}:{hora_transacao[2:4]}:{hora_transacao[4:6]}"
        valor_tratado = int(valor)/100

        data = {
                "tipo": tipo,
                "data" : data_tratada,
                "valor" : valor_tratado,
                "cpf" : cpf,
                "cartao" : cartao,
                "hora_transacao" : hora_tratada,
                "dono_loja" : dono_loja,
                "nome_loja" : nome_loja
                }
        
        FormData.objects.create(**data)

    lista = FormData.objects.all()

    context = {
        "lista" : lista
    }

        
    return render(request, 'tabela.html',context)



