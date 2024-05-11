
qnt_processos = int(input("Informe a quantidade de processos: "))
lista_processos = []
processo = {}




#Função que adiciona os dados dos processos em um dicionário e esse deicionario é adicionado a uma lista.
for c in range(qnt_processos):
    print(f"Informe os dados do processo {c+1}: ")
    processo = {"T_chegada" : int(input("Tempo de Chegada")), "T_exec": int(input("Tempo de Execução")), "Deadline": int(input("Deadline")),}
    lista_processos.append(processo.copy())
    processo.clear()




#Função que faz o programa rodar como um todo.
def execucao(lista):
       
        n = 0
        while n != 5:
            lista_ordenada_tempo_chegada = sorted(lista_processos, key=lambda dicionario: dicionario['T_chegada'])
            escolha = int(input("\033[0;32mEscolha qual algoritmo quer executar:\033[m  \n 1 - FIFO \n 2 - SJF \n 3 - Round Robin \n 4 - EDF \n 5 - Exit \n "))

           
            if 5 >= escolha and escolha >= 1:
                match escolha:
                    case 1:
                        print("FIFO. Vamos lá!")
                        fifo(lista_ordenada_tempo_chegada)
                     
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


#Função do FIFO      
def fifo(lista):
    turnaround = 0
    tempo_atual = 0 #Tempo decorrido do sistema
    
    for k, v in enumerate(lista):
        espera = max(0, tempo_atual - v['T_chegada']) #Calcula o tempo de espera do processo
        print(f"Tempo médio Processo {k+1}: {espera + v['T_exec']}")
        v['T_medio'] = espera + v['T_exec'] 
        tempo_atual += v['T_exec'] #Incrementa o tempo atual com o tempo de execução do processo.
        turnaround += v['T_medio']

    turnaround = turnaround / len(lista_processos)
    turnaround = round(turnaround, 2)
    processo = {"T_medio": turnaround}
    lista.append(processo.copy())
    processo.clear()

    print("Lista por ordem de execução: ")
    for k, v in enumerate(lista):
        if k == len(lista) - 1:
            print(f"Turnaround: {v['T_medio']:.2f}")
        else:
            print(f"Processo {k+1} -- > {v['T_medio']}")
    lista.clear()
  

#Função do SJF

execucao(lista_processos)




   









     

    






    
    
    








   








