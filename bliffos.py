import json
import datetime
import random
print("                                                                                BliffOS")
print("""Attenzione! Questa è la versione 0.9 di BliffOS,
       in cui potresti riscontrare dei problemi.
       Grazie per l'attenzione.""")
while True:
    command=input("Scrivi qua un comando:")
    if command == "help":
        print("""
    help: Ti aiuta a usare BliffOS con una lista di comandi che puoi usare.
    shutdown: Spegne BliffOS.
    math: Ti chiede due numeri e il segno operativo per sommarli, sottrarli, moltiplicarli e dividerli.
    date: Mostra data e ora in quel momento.
    psr: Ti fa giocare a morra cinese: 1 significa carta, 2
    significa forbice e 3 significa pietra.
    blifftext: """)
    
    elif command == "shutdown":
        print("Grazie per aver usato BliffOS!")
        exit(0)
    elif command == "math":
        first_number=input("a=")
        first_number=int(first_number)
        second_number=input("b=")
        second_number=int(second_number)
        operation=input("op=")
        if operation == "+":
            print(first_number+second_number)
        elif operation == "-":
            print(first_number-second_number)
        elif operation == "*":
            print(first_number*second_number)
        elif operation == "/":
            print(first_number/second_number)
    elif command == "information":
        print("""                                                           BliffOS, 2025-2026, all right reserved.
        Creator: Giuliano Zambuto, 8 year.
        Assistant: Daniele Zambuto, 43 year.""")
    elif command == "date":
        print(datetime.datetime.now())
    elif command == "psr":
        cpu=random.randint(1, 3)
        you=input("1 = carta, 2 = forbice, 3 = pietra. Fai la tua scelta! ")
        you=int(you)
        if you > 3 or you < 1:
            print("Scelta non valida!")
        else:
            print("cpu: "+str(cpu))
            print("you: "+str(you))
            if cpu == you:
                print("Pareggio!")
            elif cpu == 1 and you == 3:
                print("Hai perso!")
            elif cpu == 2 and you == 1:
                print("Hai perso!")
            elif cpu == 3 and you == 2:
                print("Hai perso!")
            else:
                print("Hai vinto!")
                
    elif command == "blifftext":
            print("""Opzioni:
     1.Crea
     2.Carica""")
            text_menu=input("Inserisci: ")
            if text_menu == "1":
                text_content=input("")
                file_name=input("Inserire nome del file: ")
                file_content={
                    "content": text_content
                }
                with open(file_name, "w") as file:
                   json.dump(file_content, file)
            if text_menu == "2":
                file_to_load=input("Inserire nome del file da caricare: ")
                with open(file_to_load, "r") as file:
                    file_content=json.load(file)
                    print(file_content.get("content"))
    
    elif command == "number":
        cpu_choice=random.randint(0,9)
        response=input("Indovina il mio numero! ")
        if response == cpu_choice:
            print("Hai indovinato il mio numero!")
        else:
            print("Hai sbagliato! Riprova! Il mio numero era "+str(cpu_choice)+".")
        
    elif command == " ":
            print("MI-RE-DO-RE-RE#-MI-DO-RE-RE-DO-SI-DO-DO#-RE-SI-DO-MI-RE-DO-RE-RE#-MI-LA-SOL-FA#-SOL-SOL#-LA-SI-DO-DO-DO-DO-SOL-DO")
            print("""I Looney Tunes sono stati creati nel 1930, hanno cavalcato il mercato nel 1935 e nel 1937
             e nel 1940 sono diventati iconici con Bugs Bunny.""")

    else:
        print("Errore di Sintassi: Questo comando non esiste.")
    