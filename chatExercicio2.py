import time
import os

# Estrutura inicial de lista de tarefas
tarefas = []

        
# Função para adicionar nova tarefa
def adicionar_tarefa(nome, descricao, status):
    tarefas.append({"nome": nome, "descricao": descricao, "status": status})
    print("Tarefa adicionada com sucesso!\n")
    
# Função para remover tarefa
def remover_tarefa(posicao):
    tarefas.pop(posicao)
    print("Tarefa removida com sucesso!\n")

# Função para atualizar tarefa
def atualizar_tarefa(posicao):
    nome= input("Digite o nome da tarefa: ")
    descricao=input("Digite a descrição: ")
    status=input("Digite o status: ")
    tarefas[posicao] = {"nome": nome, "descricao": descricao, "status": status}
    print("Tarefa alterada com sucesso!\n")


while True:

    # Tentar entradas validas
    try:
        # Menu de opções 
        print("\n1 - Listar tarefas")
        print("2 - Adicionar tarefa na lista")
        print("3 - Remover tarefa da lista")
        print("4 - Atualizar tarefa")
        print("5 - Sair")
        escolha = int(input("\nEscolha uma opção: "))

        if escolha==1:
            # Exibir todas as tarefas
            if tarefas:
                for i, tarefa in enumerate(tarefas):
                    print(f"\nTarefa [{i}] Nome: {tarefa['nome']}, Descrição: {tarefa['descricao']}, Status: {tarefa['status']}")
                
            else:
                print("Sem tarefas na lista.\n")
                
        # Escolha de funções
        elif escolha==2: 
            # Entrada de dados na função
            nome= input("Digite o nome da tarefa: ")
            descricao=input("Digite a descrição: ")
            status=input("Digite o status: ")
            adicionar_tarefa(nome, descricao, status)
        
        elif escolha==3:
            # Exclusão de dados na função
            if tarefas:
                posicao = int(input("Escolha o número da tarefa a ser removida: "))
                if 0 <= posicao < len(tarefas):
                    remover_tarefa(posicao)
                else:
                    print("Número da tarefa inválido.\n")
            else:
                print("Sem tarefas para remover.\n")
        
        elif escolha==4:
            # Atualizar dados na função
            if tarefas:
                posicao = int(input("Escolha o número da tarefa a ser atualizada: "))
                if 0 <= posicao < len(tarefas):
                    atualizar_tarefa(posicao)
                else:
                    print("Número da tarefa inválido.\n")
            else:
                print("Sem tarefas para atualizar.\n")

        elif escolha==5:
            # Animação de saindo
            for i in range(1, 11):
                os.system('cls')
                progresso = '*' * i + '-' * (10 - i)
                print(f"Saindo [{progresso}]")
                time.sleep(1)

            os.system('cls')
            print("Saindo [**********]")
            print("SISTEMA FINALIZADO!")
            # Saida
            break

        else: 
            print("Opção inválida.")

    # Exceção para entradas invalidas
    except ValueError:  
        print("Opção inválida.")