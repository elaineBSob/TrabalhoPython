import Controlador
import Console

if __name__ == "__main__":
    Controlador.criar_tabela()
    while True:
        Console.cabecalho("Sistema Gerenciador")
        op = Console.opcoes(("Cadastrar Aluno","Consultar Aluno","Deletar Aluno","Atualizar Alunos","Atualizar notas","Consultar Todos","Sair"))
        if op == 1:
            Controlador.adicionar_aluno()
        elif op == 2:
            Controlador.exibir_aluno()
        elif op == 3:
            Controlador.deletar_aluno()
        elif op == 4:
            Controlador.atualizar_alunos()
        elif op == 5:
            Controlador.atualizar_notas()
        elif op == 6:
            Controlador.consultar_todos()
        elif op == 7:
            print("\n\n\n\n\n\n\n\n")
            print(Console.cabecalho(fecha=True,texto="GoodBye :)"))
            break