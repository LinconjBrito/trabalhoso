Qnt_Processos = int(input("Informe a quantidade de processos: "))

Lista_Dados_Processos = [[] for f in range(Qnt_Processos)]

i = 0
count_processos = 1
while i < Qnt_Processos:
    print(("Informe os seguintes dados do processo ") + (str(count_processos)) + (":"))
    Tempo_De_Chegada = int(input("Tempo de chegada: "))
    Lista_Dados_Processos[i].append(Tempo_De_Chegada)
    Tempo_De_Execucao = int(input("Tempo de execução: "))
    Lista_Dados_Processos[i].append(Tempo_De_Execucao)
    Deadline = int(input("Deadline: "))
    Lista_Dados_Processos[i].append(Deadline)

    i+=1
    count_processos +=1

print("Informe os seguintes dados do sistema:")
Quantum_Do_Sistema = int(input("Quantum do sistema: "))
Sobrecarda_Do_Sistema = int(input("Sobrecarga do sistema: "))




