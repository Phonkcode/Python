while True:
    print('')
    print("===== Menu =====")
    print("1. O que é print?")
    print("2. O que é input?")
    print("3. O que é int?")
    print("4. O que é str?")
    print("5. O que é range, para que serve?")
    print("6. O que é while, para que serve?")
    print("7. O que é if, elif e else para que serve?")
    print("8. O que é append()?")
    print("9. O que é len?")
    print("10. O que é sum?")
    print("11. O que é set?")
    print("12. O que é list?")
    print("13. O que é extend()?")
    print("14. O que é insert()?")
    print("15. O que é Remove()?")
    print("16. O que é pop()?")
    print("17. O que é index()?")
    print("18. O que é count()?")
    print("19. O que é sort()?")
    print("20. O que é reverse()?")
    print("21. O que é copy()?")
    print("22. O que é clear()?")
    print("23. O que é strip()?")
    print("0. Sair")

    escolha = input("Digite o número da opção desejada: ")
    print('')

    if escolha == '0':
        break

    elif escolha == '1':
        print("Em Python, print() é uma função embutida que permite exibir mensagens ou valores na saída do programa.")
        print("Ela é usada para mostrar informações na tela do console ou terminal durante a execução de um programa.")
        print(
            "A sintaxe básica do print() é a seguinte: print(valor1, valor2, ..., valorN)")
        print("Exemplo:")
        print('print("Olá, mundo!")')
        voltar_menu = input(
            "Digite 'm' para voltar ao menu ou 's' para sair: ")
        if voltar_menu.lower() == "m":
            continue
        else:
            break

    elif escolha == '2':
        print("Em Python, input() é uma função embutida que permite obter entrada do usuário.")
        print(
            "Ela pausa a execução do programa e espera que o usuário digite algum valor.")

        nome = input("Digite seu nome: ")
        print("Olá,", nome, "!")

        idade = input("Digite sua idade: ")
        print("Você tem", idade, "anos.")

        voltar_menu = input(
            "Digite 'm' para voltar ao menu ou 's' para sair: ")

        if voltar_menu.lower() == "m":
            continue
        else:
            print("Saindo...")
            break

    elif escolha == '3':
        print("Em Python, int() é uma função embutida que permite converter um valor em um número inteiro.")
        print("Ela é usada para garantir que um valor seja interpretado como um número inteiro.")

        valor = input("Digite um número inteiro: ")
        numero_inteiro = int(valor)

        print("O valor digitado como inteiro é:", numero_inteiro)

        voltar_menu = input(
            "Digite 'm' para voltar ao menu ou 's' para sair: ")

        if voltar_menu.lower() == "m":
            continue
        else:
            print("Saindo...")
            break

    elif escolha == '4':
        print(
            "Em Python, str() é uma função embutida que converte um valor em uma string.")
        print("Ela é usada para garantir que um valor seja interpretado como uma sequência de caracteres.")

        valor = input("Digite um valor: ")
        texto = str(valor)

        print("O valor digitado como string é:", texto)

        voltar_menu = input(
            "Digite 'm' para voltar ao menu ou 's' para sair: ")

        if voltar_menu.lower() == "m":
            continue
        else:
            print("Saindo...")
            break

    elif escolha == '5':
        print("Em Python, range() é uma função embutida que gera uma sequência de números.")
        print(
            "Ela é comumente usada em loops for para iterar sobre um intervalo de valores.")

        start = int(input("Digite o valor inicial: "))
        end = int(input("Digite o valor final: "))
        step = int(input("Digite o tamanho do passo: "))

        for num in range(start, end, step):
            print(num)

        voltar_menu = input(
            "Digite 'm' para voltar ao menu ou 's' para sair: ")

        if voltar_menu.lower() == "m":
            continue
        else:
            print("Saindo...")
            break

    elif escolha == '6':
        print("Em Python, while é uma estrutura de controle de fluxo que permite executar um bloco de código repetidamente")
        print("enquanto uma condição especificada for verdadeira.")

        contador = 0
        while contador < 5:
            print("Executando o loop while. Contador =", contador)
            contador += 1

        voltar_menu = input(
            "Digite 'm' para voltar ao menu ou 's' para sair: ")

        if voltar_menu.lower() == "m":
            continue
        else:
            print("Saindo...")
            break

    elif escolha == '7':
        print("Em Python, if, elif e else são estruturas de controle de fluxo que permitem executar blocos de código")
        print("com base em condições específicas.")

        nota = float(input("Digite sua nota: "))

        if nota >= 9.0:
            print("Excelente!")
        elif nota >= 7.0:
            print("Bom trabalho!")
        else:
            print("Estude mais!")

        voltar_menu = input(
            "Digite 'm' para voltar ao menu ou 's' para sair: ")

        if voltar_menu.lower() == "m":
            continue
        else:
            print("Saindo...")
            break

    elif escolha == '8':
        print("Em Python, append() é um método utilizado em listas para adicionar um elemento ao final da lista.")

        lista = [1, 2, 3]
        valor = int(input("Digite um número para adicionar à lista: "))
        lista.append(valor)
        print("Lista atualizada:", lista)

        voltar_menu = input(
            "Digite 'm' para voltar ao menu ou 's' para sair: ")

        if voltar_menu.lower() == "m":
            continue
        else:
            print("Saindo...")
            break

    elif escolha == '9':
        print("Em Python, len() é uma função embutida que retorna o tamanho (número de elementos) de uma sequência.")

        lista = [1, 2, 3, 4, 5]
        tamanho = len(lista)
        print("O tamanho da lista é:", tamanho)

        voltar_menu = input(
            "Digite 'm' para voltar ao menu ou 's' para sair: ")

        if voltar_menu.lower() == "m":
            continue
        else:
            print("Saindo...")
            break

    elif escolha == '10':
        print("Em Python, sum() é uma função embutida que retorna a soma dos elementos de uma sequência numérica.")

        lista = [1, 2, 3, 4, 5]
        soma = sum(lista)
        print("A soma dos elementos da lista é:", soma)

        voltar_menu = input(
            "Digite 'm' para voltar ao menu ou 's' para sair: ")

        if voltar_menu.lower() == "m":
            continue
        else:
            print("Saindo...")
            break

    elif escolha == '11':
        print("Em Python, set() é um tipo de dado utilizado para armazenar uma coleção de elementos únicos.")

        conjunto = set([1, 2, 3, 4, 4, 5, 5])
        print("Conjunto:", conjunto)

        voltar_menu = input(
            "Digite 'm' para voltar ao menu ou 's' para sair: ")

        if voltar_menu.lower() == "m":
            continue
        else:
            print("Saindo...")
            break

    elif escolha == '12':
        print("Em Python, list() é um tipo de dado utilizado para armazenar uma sequência de elementos.")

        lista = list("Python")
        print("Lista:", lista)

        voltar_menu = input(
            "Digite 'm' para voltar ao menu ou 's' para sair: ")

        if voltar_menu.lower() == "m":
            continue
        else:
            print("Saindo...")
            break

    elif escolha == '13':
        print("Em Python, extend() é um método utilizado em listas para adicionar múltiplos elementos a uma lista existente.")

        lista1 = [1, 2, 3]
        lista2 = [4, 5, 6]
        lista1.extend(lista2)
        print("Lista estendida:", lista1)

        voltar_menu = input(
            "Digite 'm' para voltar ao menu ou 's' para sair: ")

        if voltar_menu.lower() == "m":
            continue
        else:
            print("Saindo...")
            break

    elif escolha == '14':
        print("Em Python, insert() é um método utilizado em listas para inserir um elemento em uma posição específica.")

        lista = [1, 2, 3, 5]
        valor = int(input("Digite um número para inserir na lista: "))
        posicao = int(input("Digite a posição de inserção: "))
        lista.insert(posicao, valor)
        print("Lista atualizada:", lista)

        voltar_menu = input(
            "Digite 'm' para voltar ao menu ou 's' para sair: ")

        if voltar_menu.lower() == "m":
            continue
        else:
            print("Saindo...")
            break

    elif escolha == '15':
        print("Em Python, remove() é um método utilizado em listas para remover a primeira ocorrência de um elemento.")

        lista = [1, 2, 3, 4, 5, 3]
        valor = int(input("Digite um número para remover da lista: "))

        if valor in lista:
            lista.remove(valor)
            print("Lista atualizada:", lista)
        else:
            print("O valor não existe na lista.")

        voltar_menu = input(
            "Digite 'm' para voltar ao menu ou 's' para sair: ")

        if voltar_menu.lower() == "m":
            continue
        else:
            print("Saindo...")
            break

    elif escolha == '16':
        print("Em Python, pop() é um método utilizado em listas para remover e retornar o último elemento.")

        lista = [1, 2, 3, 4, 5]
        elemento_removido = lista.pop()
        print("Elemento removido:", elemento_removido)
        print("Lista atualizada:", lista)

        voltar_menu = input(
            "Digite 'm' para voltar ao menu ou 's' para sair: ")

        if voltar_menu.lower() == "m":
            continue
        else:
            print("Saindo...")
            break

    elif escolha == '17':
        print("Em Python, index() é um método utilizado em listas para encontrar o índice de um elemento.")

        lista = [1, 2, 3, 4, 5]
        valor = int(
            input("Digite um número para encontrar o índice na lista: "))

        if valor in lista:
            indice = lista.index(valor)
            print("O valor", valor, "está no índice", indice)
        else:
            print("O valor não existe na lista.")

        voltar_menu = input(
            "Digite 'm' para voltar ao menu ou 's' para sair: ")

        if voltar_menu.lower() == "m":
            continue
        else:
            print("Saindo...")
            break

    elif escolha == '18':
        print("Em Python, count() é um método utilizado em listas para contar o número de ocorrências de um elemento.")

        lista = [1, 2, 2, 3, 3, 3]
        valor = int(
            input("Digite um número para contar ocorrências na lista: "))
        ocorrencias = lista.count(valor)
        print("O número", valor, "aparece", ocorrencias, "vezes na lista.")

        voltar_menu = input(
            "Digite 'm' para voltar ao menu ou 's' para sair: ")

        if voltar_menu.lower() == "m":
            continue
        else:
            print("Saindo...")
            break

    elif escolha == '19':
        print("Em Python, sort() é um método utilizado em listas para ordenar os elementos em ordem crescente.")

        lista = [3, 1, 4, 2, 5]
        lista.sort()
        print("Lista ordenada:", lista)

        voltar_menu = input(
            "Digite 'm' para voltar ao menu ou 's' para sair: ")

        if voltar_menu.lower() == "m":
            continue
        else:
            print("Saindo...")
            break

    elif escolha == '20':
        print("Em Python, reverse() é um método utilizado em listas para inverter a ordem dos elementos.")

        lista = [1, 2, 3, 4, 5]
        lista.reverse()
        print("Lista invertida:", lista)

        voltar_menu = input(
            "Digite 'm' para voltar ao menu ou 's' para sair: ")

        if voltar_menu.lower() == "m":
            continue
        else:
            print("Saindo...")
            break

    elif escolha == '21':
        print("Em Python, copy() é um método utilizado em listas para criar uma cópia da lista.")

        lista = [1, 2, 3]
        copia = lista.copy()
        print("Cópia da lista:", copia)

        voltar_menu = input(
            "Digite 'm' para voltar ao menu ou 's' para sair: ")

        if voltar_menu.lower() == "m":
            continue
        else:
            print("Saindo...")
            break

    elif escolha == '22':
        print("Em Python, clear() é um método utilizado em listas para remover todos os elementos da lista.")

        lista = [1, 2, 3]
        lista.clear()
        print("Lista vazia:", lista)

        voltar_menu = input(
            "Digite 'm' para voltar ao menu ou 's' para sair: ")

        if voltar_menu.lower() == "m":
            continue
        else:
            print("Saindo...")
            break

    elif escolha == '23':
        print("Em Python, strip() é um método utilizado em strings para remover espaços em branco no início e no fim.")

        texto = "   Python   "
        texto_sem_espacos = texto.strip()
        print("Texto original:", texto)
        print("Texto sem espaços:", texto_sem_espacos)

        voltar_menu = input(
            "Digite 'm' para voltar ao menu ou 's' para sair: ")

        if voltar_menu.lower() == "m":
            continue
        else:
            print("Saindo...")
            break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
