import Console
from Banco import criar_tabela
import Banco
import Calculadora

def adicionar_aluno():
    nome = str(input("Nome: "))
    email = str(input("E-mail: "))
    campus = str(input("Campus: "))
    matricula =  Console.safe_number(seta="Matrícula: ")
    endereco = str(input("Endereço: "))
    periodo = Console.safe_number(seta="Período: ")
    Banco.incluir_aluno((nome,matricula,email,endereco,campus,periodo))

def atualizar_notas():
    ida = Calculadora.safe_number(seta="Id: ")
    av1 = Calculadora.safe_float(seta="av1: ")
    av2 = Calculadora.safe_float(seta="av2: ")
    av3 = Calculadora.safe_float(seta="av3: ")
    avd = Calculadora.safe_float(seta="avd: ")
    avds = Calculadora.safe_float(seta="avds: ")
    Banco.atualizar_notas(ida,(av1,av2,av3,avd,avds))

def atualizar_alunos():
    ida = Calculadora.safe_number(seta="Id: ")
    nome = str(input("Nome: "))
    email = str(input("E-mail: "))
    campus = str(input("Campus: "))
    matricula =  Console.safe_number(seta="Matrícula: ")
    endereco = str(input("Endereço: "))
    periodo = Console.safe_number(seta="Período: ")
    Banco.atualizar_aluno(ida,(nome,email,endereco,campus,matricula,periodo))

def consultar_todos():
    alunos = Banco.pegar_alunos()
    for aluno in alunos:
        print(string_aluno(aluno))

def string_aluno(aluno):
    if aluno == None:
        return "Não existe um aluno com esse id"
    media = "{:.2f}".format(Calculadora.get_media((aluno[7],aluno[8],aluno[9],aluno[10],aluno[11])))
    return f'''
    ID: {aluno[0]}
    Nome: {aluno[1]}
    Email: {aluno[2]}
    Endereço: {aluno[3]}
    Campus: {aluno[4]}
    Matricula: {aluno[5]}
    Periodo: {aluno[6]}
    Média: {media}\n'''

def exibir_aluno():
    ida = Console.safe_number(seta="Id: ")
    aluno = Banco.pegar_aluno(ida)
    print(string_aluno(aluno))

def deletar_aluno():
    ida = Console.safe_number(seta="Id: ")
    Banco.deletar_aluno(ida)