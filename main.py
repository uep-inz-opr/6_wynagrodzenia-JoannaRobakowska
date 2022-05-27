class Pracownik:
    def __init__(self, imie, wyn):
        self.imie = str(imie)
        self.wyn = int(wyn)
    
    def __repr__(self):
        return f"{self.imie} {self.wyn}"
    
    def __wynagrodzenie_netto__(self):
       krok_1 = round(round(self.wyn * 0.0976,2) + round(self.wyn * 0.015,2) + round(self.wyn * 0.0245,2), 2)
       krok_2 = round(self.wyn-krok_1,2)
       krok_3 = round(krok_2*0.09, 2)
       krok_4 = round(krok_2*0.0775, 2)
       krok_5 = round(111.25, 2)
       krok_6 = round(self.wyn - krok_5 - krok_1, 2)
       krok_7 = round(krok_6, 0)
       krok_8 = round(((krok_7)*0.18)-46.33,2)
       krok_9 = round(krok_8-krok_4, 2)
       krok_10 = round(krok_9, 0)
       self.wynagrodzenienetto = round((self.wyn - krok_1 - krok_3 - krok_10), 2)
       return round(self.wynagrodzenienetto, 2)
    
    def __obliczanie_skladki__(self):
        self.skladki = round(self.wyn *0.0976, 2) + round(self.wyn*0.065, 2) + round(self.wyn*0.0193,2) + round(self.wyn*0.0245,2) + round(self.wyn*0.001,2)
        return round(self.skladki,2)

    def __koszt__(self):
        self.koszt = round(self.wyn + self.skladki, 2)
        return self.koszt
    def __razem__(self):
        return round(self.wyn+ self.__obliczanie_skladki__(),2)      

wszyscy_pracownicy = int(input())
pracownicy = []
for n in range(wszyscy_pracownicy):
    imie_wynagrodzenie = input().split()
    imie = imie_wynagrodzenie[0]
    wynagrodzenie = imie_wynagrodzenie[1]
    pracownik_obj = Pracownik(imie, wynagrodzenie)
    pracownicy.append(pracownik_obj)

laczny_koszt_pracodawcy = 0 

for m in range(wszyscy_pracownicy):
    laczny_koszt_pracodawcy += pracownicy[m].__razem__()
    imie = pracownicy[m].imie
    wyn = pracownicy[m].wyn
    print(imie, f"{pracownicy[m].__wynagrodzenie_netto__():.2f}", f"{pracownicy[m].__obliczanie_skladki__():.2f}", f"{pracownicy[m].__koszt__():.2f}")

print(laczny_koszt_pracodawcy)