def beräkna_pensionsår():
    pensionsålder = 65
    
    while True:
        try:
            ålder = input("Vänligen ange din ålder: ")
            ålder = int(ålder)

        except ValueError:
            print("Error ! du måste ange ett positivt heltal.")
            continue

        else:
            if ålder < 0:
                print("Vänligen ange en giltig, positiv ålder.")
                continue
                
            år_kvar = pensionsålder - ålder
            
            if år_kvar > 0:
                print("Det är", år_kvar, "år kvar tills du når pensionen.")
            elif år_kvar == 0:
                print("Grattis! Du har redan nått pensionsåldern.")
            else:
                år_passerat = (år_kvar)
                print(" Grattis, Du har redan passerat pensionsåldern.")
            
            break
            
        finally:
            print("program avslutad klart.")

beräkna_pensionsår()

