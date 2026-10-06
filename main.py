import random

numero_segreto = random.randint(1, 20)

indovinato = False

for tentativo in range(1, 6):  # Il ciclo for - 5 tentativi
    print("Tentativo {tentativo}: Indovina il numero da 1 a 20:")
    scelta = int(input())

    if scelta == numero_segreto:  # Operatore ==
        print("Bravo! Hai indovinato! Il numero era {numero_segreto}")
        indovinato = True
        break  
    elif scelta < numero_segreto:  # Operatore <
        print("Il numero segreto è maggiore.")
    else:  
        print("Il numero segreto è minore.")

if not indovinato:
    print("Non ci sono più tentativi disponibili. Il numero segreto era {numero_segreto}.")
    numero_segreto = 16
