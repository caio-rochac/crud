opcao = 0
alunos = []

while opcao != -1:
    print("---------- CRUD aluno ----------")
    print("Controle de Alunos")
    print("1 - Listar Alunos")
    print("2 - Cadastrar Alunos")
    print("3 - Consultar Aluno (chave: CPF)")
    print("4 - Editar Aluno (chave: CPF)")
    print("5 - Remover Aluno (chave: CPF)")
    print("6 - Listar Nomes dos Alunos Aprovados")
    print("7 - Listar Quantidade de Alunos por Situação")
    print("8 - Mostrar Média de Notas da Turma")
    print("9 - Apresentar o Nome e Nota do Aluno com Maior Nota")
    print("10 - Apresentar o Nome e Nota do Aluno com Menor Nota")
    print("-1 - Encerrar programa")

    opcao = int(input("digite a opção: "))

    if opcao == 1:
        if len(alunos) == 0:
            print("Não há alunos cadastrados!")
        else:
            
