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
            for i in range(len(alunos)):
                print(alunos[i][1])
				
	if opcao == 2:
		alunos.append(["", "", 0, 0, 0, ""])
		alunos[-1][0] = input("Digite o CPF: ")
		alunos[-1][1] = input("Digite o nome: ")
		alunos[-1][2] = int(input("Digite a primeira nota: "))
		alunos[-1][3] = int(input("Digite a segunda nota: "))
		alunos[-1][4] = (alunos[-1][2] + alunos[-1][3]) / 2
		if alunos[-1][4] >= 7:
			alunos[-1][5] = "A"
		elif alunos[-1][4] < 7 and alunos[-1][4] >= 4:
			alunos[-1][5] = "F"
		else:
			alunos[-1][5] = "R"
	
	if opcao == 3:
		if len(alunos) > 0:
			cpf = input("Consultar CPF: ")
			contagem = len(alunos)

			for i in range(alunos):
				if cpf == alunos[i][0]:

					contagem -= 1

			if contagem == len(alunos):
				print("CPF não encontrado!")
		else:
			print("Não há alunos cadastrados!")
