import random


valore_carte_utente = None
valore_carte_pc = None
probabilita_banco = None

#valori booleani

def game():
    while True:
   
        print("--BLACK JACK--")
        # mano dell'utente: calore
        valore_carte_utente = random.randint(1, 13) + random.randint(1,8)

        n_carte_utente = 2
        print("Tue carte: ", valore_carte_utente)

        #chiamare carta
        while valore_carte_utente < 21:
            scelta_carta_utente = int(input("[1]Stai \n[2]chiama carta"))
            if (scelta_carta_utente == 2):
                valore_carte_utente += random.randint(1,13)
                print(valore_carte_utente)
                if valore_carte_utente >= 21:
                    print("Sballato, il banco vince")
                    return
            elif  (scelta_carta_utente == 1):
                print("Valore delle tue carte", valore_carte_utente)
                break
                

        #Scelta delle carte del pc

        valore_carte_pc = random.randint(1,13) + random.randint(1,8)

        while valore_carte_pc > 21:
            #segno biricchino
            if valore_carte_pc > 5:
                valore_carte_pc = valore_carte_pc + random.randint(1,13)
                

            elif valore_carte_pc < 6 and valore_carte_pc > 12:
                probabilita_banco = random.randint (1,3)
                if probabilita_banco > 1:
                    valore_carte_pc = valore_carte_pc + random.randint(1,13)
                    break
                else:
                    print("valore carte del pc: ", valore_carte_pc)

            elif valore_carte_pc < 13 and valore_carte_pc > 19:
                probabilita_banco = random.randint (1,10)
                if probabilita_banco > 6:
                    valore_carte_pc = valore_carte_pc + random.randint(1,13)
                    break
                else:
                    print("valore carte del pc: ", valore_carte_pc)

            elif valore_carte_pc > 20:
                probabilita_banco = random.randint (1,20)
                if probabilita_banco < 20:
                    valore_carte_pc = valore_carte_pc + random.randint(1,13)
                    break
                else:
                    print("valore carte del pc: ", valore_carte_pc)

            #if biricchino
            if valore_carte_pc > 21:
                print("Il banco ha sballato con punteggio di", valore_carte_pc)
                return

        if valore_carte_utente > valore_carte_pc:
            print("Hai vinto! \n tuo punteggio: ", valore_carte_utente, "\n punteggio pc: ", valore_carte_pc)
        elif valore_carte_pc > valore_carte_utente:
            print("Hai perso! \n tuo punteggio: ", valore_carte_utente, "\n punteggio pc: ", valore_carte_pc)
        elif valore_carte_pc == valore_carte_utente:
            print("Parita' con punteggio di ", valore_carte_utente)

        scelta_chiusura = int(input("[1]Chiudi gioco [2]Continua a giocare"))
        if scelta_chiusura == 1:
            print("Grazie per aver giocato")
            return



game()








