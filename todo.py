import json
import os

ARQUIVO_TAREFAS = "tarefas.json"

def carregar_tarefas():
    if not os.path.exists(ARQUIVO_TAREFAS):
        return []
    with open(ARQUIVO_TAREFAS, "r") as f:
        return json.load(f)

def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, "w") as f:
        json.dump(tarefas, f, indent=4)

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    for i, tarefa in enumerate(tarefas, 1):
        status = "✔" if tarefa["feita"] else "✘"
        print(f"{i}. [{status}] {tarefa['descricao']}")

def adicionar_tarefa(tarefas):
    desc = input("Descrição da nova tarefa: ").strip()
    if desc:
        tarefas.append({"descricao": desc, "feita": False})
        salvar_tarefas(tarefas)
        print("Tarefa adicionada!")
    else:
        print("Descrição vazia. Tarefa não adicionada.")

def marcar_tarefa_feita(tarefas):
    listar_tarefas(tarefas)
    try:
        escolha = int(input("Número da tarefa feita: "))
        if 1 <= escolha <= len(tarefas):
            tarefas[escolha - 1]["feita"] = True
            salvar_tarefas(tarefas)
            print("Tarefa marcada como feita!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        escolha = int(input("Número da tarefa para remover: "))
        if 1 <= escolha <= len(tarefas):
            tarefa_removida = tarefas.pop(escolha - 1)
            salvar_tarefas(tarefas)
            print(f"Tarefa '{tarefa_removida['descricao']}' removida!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def menu():
    tarefas = carregar_tarefas()
    while True:
        print("\n--- To-Do List ---")
        print("1. Listar tarefas")
        print("2. Adicionar tarefa")
        print("3. Marcar tarefa como feita")
        print("4. Remover tarefa")
        print("5. Sair")
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            listar_tarefas(tarefas)
        elif escolha == "2":
            adicionar_tarefa(tarefas)
        elif escolha == "3":
            marcar_tarefa_feita(tarefas)
        elif escolha == "4":
            remover_tarefa(tarefas)
        elif escolha == "5":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()

