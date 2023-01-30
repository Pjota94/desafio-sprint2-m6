data = "3201903010000014200096206760174753****3153153453JOÃO MACEDO   BAR DO JOÃO"


class Campo:
    def __init__(self, inicio, final):
        self.inicio = inicio
        self.final = final

    def __set_name__(self, owner, nome):
        self.nome = nome

    def __get__(self, instance, owner):
        if not instance:
            return self
        return instance.dados_brutos[self.inicio : self.final]


class Base:
    def __init__(self, dados):
        self.dados_brutos = dados

    def __repr__(self):
        campos = []
        for name, obj in self.__class__.__dict__.items():
            if isinstance(obj, Campo):
                campos.append((name, getattr(self, name)))
        return "\n".join(f"{campo}:{conteudo}" for campo, conteudo in campos)


class CNAB_LINHA1(Base):
    tipo = Campo(0, 1)
    data = Campo(1, 9)
    valor = Campo(9, 19)
    cpf = Campo(19, 30)
    cartao = Campo(30, 42)
    hora_transacao = Campo(42, 48)
    nome_dono_loja = (48, 62)
    nome_loja = (62, 81)


result = print(CNAB_LINHA1(data))
