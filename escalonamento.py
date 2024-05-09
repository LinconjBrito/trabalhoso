
qnt_processos = int(input("Informe a quantidade de processos: "))
lista_processos = []
processo = {}

for c in range(qnt_processos):
    print(f"Informe os dados do processo {c+1}: ")
    processo = {"T_chegada" : int(input("Tempo de Chegada")), "T_exec": int(input("Tempo de Execução")), "Deadline": int(input("Deadline")),}
    lista_processos.append(processo.copy())
    processo.clear()


def execucao():
        n = 0
        while n != 5:
            escolha = int(input("\033[0;32mEscolha qual algoritmo quer executar:\033[m  \n 1 - FIFO \n 2 - SJF \n 3 - Round Robin \n 4 - EDF \n 5 - Exit \n "))
            if 5 >= escolha and escolha >= 1:
                match escolha:
                    case 1:
                        print("FIFO. Vamos lá!")
                     
                    case 2:
                        print("SJF. Vamos lá!")

                    case 3:
                        print("Round Robin. Vamos lá!")

                    case 4:
                        print("EDF. Vamos lá!")
            
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
        print(f"Tempo médio Processo {k+1}: {espera + v['T_exec']}")
        v['T_medio'] = espera + v['T_exec'] 
        tempo_atual += v['T_exec'] #Incrementa o tempo atual com o tempo de execução do processo.
        turnaround += v['T_medio']

    turnaround = turnaround / len(lista_processos)
    turnaround = round(turnaround, 2)
    processo = {"T_medio": turnaround}
    lista_ordenada_tempo_chegada.append(processo.copy())
    processo.clear()

    print("Lista por ordem de execução: ")
    for k, v in enumerate(lista_ordenada_tempo_chegada):
        if k == len(lista_ordenada_tempo_chegada) - 1:
            print(f"Turnaround: {v['T_medio']:.2f}")
        else:
            print(f"{k+1} -- > {v['T_medio']}")

fifo()








     

    






    
    
    








   








