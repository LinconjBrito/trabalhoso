# QUANTIDADE DE PROCESSOS;
qnt_processos = int(input("Informe a quantidade de processos: "))

# LISTA DE DICIONÁRIOS QUE CONTÉM OS DADOS DOS PROCESSOS;
lista_processos = [
    {"T_chegada": 0, "T_exec": 4, "Deadline": 7},
    {"T_chegada": 2, "T_exec": 2, "Deadline": 5},
    {"T_chegada": 4, "T_exec": 1, "Deadline": 8},
    {"T_chegada": 6, "T_exec": 3, "Deadline": 10}
]

# Inicialização de variáveis
tempo_atual = 0
lista_final = []
turnaround = 0

# Lista de processos ordenados por tempo de chegada
lista_processos = sorted(lista_processos, key=lambda dicionario: dicionario["T_chegada"])

# Enquanto houver processos na lista de processos
while lista_processos:
    # Filtra processos que já chegaram
    processos_disponiveis = [p for p in lista_processos if p["T_chegada"] <= tempo_atual]
    
    if processos_disponiveis:
        # Seleciona o processo com o menor tempo de execução
        proximo_processo = min(processos_disponiveis, key=lambda p: p["T_exec"])
        lista_processos.remove(proximo_processo)
        
        # Calcula o tempo de espera e o tempo médio
        espera = max(0, tempo_atual - proximo_processo["T_chegada"])
        proximo_processo["T_medio"] = espera + proximo_processo["T_exec"]
        turnaround += proximo_processo["T_medio"]
        
        # Atualiza o tempo atual
        tempo_atual += proximo_processo["T_exec"]
        lista_final.append(proximo_processo)
    else:
        # Se não há processos disponíveis, avança o tempo
        tempo_atual = lista_processos[0]["T_chegada"]

# Calcula o turnaround médio
turnaround_medio = turnaround / qnt_processos
lista_final.append({"T_medio": turnaround_medio})

# Imprime o resultado
for processo in lista_final:
    print(f"{processo}\n")
