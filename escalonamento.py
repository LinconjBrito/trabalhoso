

qnt_processos = int(input("Informe a quantidade de processos: "))
lista_processos = []
processo = {}

for c in range(qnt_processos):
    print(f"Informe os dados do processo {c+1}: ")
    processo = {"T_chegada" : float(input("Tempo de Chegada: ")), "T_exec": float(input("Tempo de Execução: ")), "Deadline": float(input("Deadline: ")), "T_medio": 0}
    lista_processos.append(processo.copy())
    processo.clear()

quantum = float(input("Qual o quantum do Sitema?"))
sobrecarga = float(input("Qual a sobrecarga do sistema?"))



def execucao():
        n = 0
        while n != 5:
            escolha = int(input("\033[0;32mEscolha qual algoritmo quer executar:\033[m  \n 1 - FIFO \n 2 - SJF \n 3 - Round Robin \n 4 - EDF \n 5 - Exit \n "))
            if 5 >= escolha and escolha >= 1:
                match escolha:
                    case 1:
                        print("\033[0;32mFIFO. Vamos lá!\033[m")
                        fifo()
                     
                    case 2:
                        print("SJF. Vamos lá!")
                        sjf()

                    case 3:
                        print("Round Robin. Vamos lá!")
                        round_r()

                    case 4:
                        print("EDF. Vamos lá!")
                        edf()
            
                    case 5: 
                        print("Saindo...")
                n = escolha
            else: 
                print("\033[0;31mPor favor! Escolha um valor entre 1 e 5!\033[m")
     
       
def fifo():
    turnaround = 0
    tempo_atual = 0 #Tempo decorrido do sistema
    lista_ordenada_tempo_chegada = sorted(lista_processos, key=lambda dicionario: dicionario['T_chegada'])
    for k, v in enumerate(lista_ordenada_tempo_chegada):
        espera = max(0, tempo_atual - v['T_chegada']) #Calcula o tempo de espera do processo
        v['T_medio'] = espera + v['T_exec'] 
        if k > 0:
            tempo_atual += v['T_exec'] #Incrementa o tempo atual com o tempo de execução do processo.
        else:
            tempo_atual += v["T_chegada"] + v['T_exec'] #Incrementa o tempo atual com o tempo de execução do processo.

        turnaround += v['T_medio']


    turnaround = turnaround / len(lista_processos)

    print(f"Turnaround medio de: {float(turnaround)}")
    


    # processo = {"T_medio": turnaround}
    # lista_ordenada_tempo_chegada.append(processo.copy())
    # processo.clear()

    # print("Lista por ordem de execução: ")
    # for k, v in enumerate(lista_ordenada_tempo_chegada):
    #     if k == len(lista_ordenada_tempo_chegada) - 1:
    #         print(f"Turnaround: {v['T_medio']:.2f}")
    #     else:
    #         print(f"{k+1} -- > {v['T_medio']}")


def sjf():
    # Inicialização de variáveis
    tempo_atual = 0
    lista_final = []
    turnaround = 0

    # Lista de processos ordenados por tempo de chegada
    lista_processos2 = sorted(lista_processos, key=lambda dicionario: dicionario["T_chegada"])
 
    # Enquanto houver processos na lista de processos
    while lista_processos2:
        # Filtra processos que já chegaram
        processos_disponiveis = [p for p in lista_processos2 if p["T_chegada"] <= tempo_atual]
        
        if processos_disponiveis:
            # Seleciona o processo com o menor tempo de execução
            proximo_processo = min(processos_disponiveis, key=lambda p: p["T_exec"])
            lista_processos2.remove(proximo_processo)
            
            # Calcula o tempo de espera e o tempo médio
            espera = max(0, tempo_atual - proximo_processo["T_chegada"])
            proximo_processo["T_medio"] = espera + proximo_processo["T_exec"]
            turnaround += proximo_processo["T_medio"]
            
            # Atualiza o tempo atual
            tempo_atual += proximo_processo["T_exec"]
            lista_final.append(proximo_processo)
        else:
            # Se não há processos disponíveis, avança o tempo
            tempo_atual = lista_processos2[0]["T_chegada"]

    turnaround = turnaround/qnt_processos
    print(f"Turnaround medio de: {float(turnaround)}")
    

def round_r():


    lista_tempo_chegada = [] 
    lista_tempo_execucao = []

    for k, v in enumerate(lista_processos):
        lista_tempo_chegada.append(v['T_chegada'])
        lista_tempo_execucao.append(v['T_exec'])


    tempo = turnaround = 0
    
    tempo_cpu = [0]*qnt_processos  
    lista_processamento = [0]*qnt_processos  
    lista_circular = [] 
    
    def verificaFila():
        for x in range(0,qnt_processos):
            if lista_tempo_chegada[x] <= tempo and lista_processamento[x] == 0:
                lista_processamento[x] = 1 
                lista_circular.append(x)  
            pass
    verificaFila()

    for p in lista_circular:
        resta_executar = lista_tempo_execucao[p]-tempo_cpu[p]  
        if resta_executar > quantum:
            tempo+= quantum
            verificaFila()
            tempo_cpu[p]+=quantum
            tempo+= sobrecarga
            verificaFila()
            lista_circular.append(p)
        elif resta_executar == quantum and resta_executar > 0 : 
            tempo+=quantum
            verificaFila()
            tempo_cpu[p]+=quantum
            turnaround+=tempo-lista_tempo_chegada[p]
        elif resta_executar < quantum:
            tempo+= resta_executar
            verificaFila()
            tempo_cpu[p]+=resta_executar
            turnaround+=tempo-lista_tempo_chegada[p]
    
    print(f"Turnaround medio de: {float(turnaround/qnt_processos)}") 


def edf():
      
    lista_tempo_chegada = [] 
    lista_tempo_execucao = []
    lista_deadlines = []

    for k, v in enumerate(lista_processos):
        lista_tempo_chegada.append(v['T_chegada'])
        lista_tempo_execucao.append(v['T_exec'])
        lista_deadlines.append(v['Deadline'])

    tempo = turnaround = 0
    
    tempo_cpu = [0]*qnt_processos  
    lista_processamento = [0]*qnt_processos  

    def verificaFila():
        for x in range(0,qnt_processos):
            if lista_tempo_chegada[x] <= tempo and lista_processamento[x] == 0:
                lista_processamento[x] = 1
            pass
    verificaFila()
    def firstKill():
        deadline_proxima = 1000
        escolhido = -1
        for x in range(0,qnt_processos):
            if lista_processamento[x] == 1 and lista_deadlines[x] < deadline_proxima and tempo_cpu[x] < lista_tempo_execucao[x]:
                deadline_proxima = lista_deadlines[x]
                escolhido = x
            pass
        return escolhido

    while firstKill() != -1:
        p = firstKill()
        resta_executar = lista_tempo_execucao[p]-tempo_cpu[p] 
        if resta_executar > quantum:
            tempo+=quantum
            verificaFila()
            tempo_cpu[p]+=quantum 
            tempo+=sobrecarga
            verificaFila()
        elif resta_executar == quantum and resta_executar > 0: 
            tempo+=quantum
            verificaFila() 
            tempo_cpu[p]+=quantum 
            turnaround+=tempo-lista_tempo_chegada[p] 
        elif resta_executar < quantum:
            tempo+= resta_executar
            verificaFila()
            tempo_cpu[p]+=resta_executar
            turnaround+=tempo-lista_tempo_chegada[p]

    print(f"Turnaround medio de: {float(turnaround/qnt_processos)}")  


execucao()
