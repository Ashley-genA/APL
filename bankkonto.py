class Konto:
    
    def __init__(self, startsaldo=0):
        
        self.__saldo__ = startsaldo
        print(f"Ett nytt konto har skapats. Startsaldo: {self._saldo} kr.")

    def sätt_in(self, belopp):
        
        if belopp > 0:
            self.__saldo__+= belopp
            print(f"\n Insättning lyckades! {belopp} kr har satts in.")
            self.visa_saldo()
        else:
            print("\nFel: Du kan bara sätta in ett positivt belopp**")

    def ta_ut(self, belopp):
        
        if belopp > 0 and self.__saldo__>= belopp:
            self.__saldo__ -= belopp
            print(f"\n Uttag lyckades! {belopp} kr har tagits ut.")
            self.visa_saldo()
        elif belopp > 0 and self.__saldo__ < belopp:
            print(f"\n Fel: Otillräckligt saldo. Ditt saldo är {self.__saldo__} kr.")
        else:
            print("\nFel: Du kan bara ta ut ett positivt belopp.")

    def visa_saldo(self):
        
        print(f"\n🏦 Ditt aktuella saldo är: {self.__saldo__} kr.")

def meny():
    mitt_konto = Konto(startsaldo=1000)
    
    while True:
        print("\n" + "="*30)
        print("          BANKOMATEN")
        print("="*30)
        print("1: Sätt in pengar")
        print("2: Ta ut pengar")
        print("3: Visa saldo")
        print("4: Avsluta")
        print("-" * 30)

        val = input("Välj ett alternativ (1-4): ")

        if val == '1':
            try:
                belopp = float(input("Ange belopp att sätta in: "))
                mitt_konto.satt_in(belopp)
            except ValueError:
                print("\nOgiltig inmatning. Ange ett nummer.")

        elif val == '2':
            try:
                belopp = float(input("Ange belopp att ta ut: "))
                mitt_konto.ta_ut(belopp)
            except ValueError:
                print("\nOgiltig inmatning. Ange ett nummer.")

        elif val == '3':
            mitt_konto.visa_saldo()

        elif val == '4':
            print("\nTack för att du använde bankomaten. Välkommen åter!")
            break

        else:
            print("\nOgiltigt val. Försök igen med 1, 2, 3 eller 4.")

# Kör programmet genom att kalla på meny-funktionen
if __name__ == "__main__":
    meny()