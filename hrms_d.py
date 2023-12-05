class HRMS:
    def __init__(self):
        self.pracownicy = []
        self.wczytaj_z_pliku()
        self.zapisz_do_pliku()

    def dodaj_pracownika(self, imie, nazwisko, stanowisko, data_zatrudnienia, wynagrodzenie):
        pracownik = {
            "Imię": imie,
            "Nazwisko": nazwisko,
            "Stanowisko": stanowisko,
            "Data zatrudnienia": data_zatrudnienia,
            "Wynagrodzenie": wynagrodzenie,
        }
        if pracownik in self.pracownicy:#jeżeli podane dane już istnieją...
            return('Taki pracownik już istnieje')
        elif pracownik['Imię']=='' or pracownik['Nazwisko']=='' or pracownik['Stanowisko']=='' or pracownik['Data zatrudnienia']=='' or pracownik['Wynagrodzenie']=='':#jeżeli podane imię jest puste (czyli nic nie podano)...
            return('Nieprawidłowe dane')
        else:
            self.pracownicy.append(pracownik)
            self.zapisz_do_pliku()
            return('Dodano pracownika :)')

    def aktualizuj_pracownika(self, nazwisko, pole, nowa_wartosc):
        for pracownik in self.pracownicy:
            if pracownik["Nazwisko"] == nazwisko:
                pracownik[pole] = nowa_wartosc
                self.zapisz_do_pliku()
                return("Dane pracownika zaktualizowane.")
        return "Pracownik o podanym imieniu nie istnieje"
    
    def wyswietl_pracownikow(self):
            if not self.pracownicy:#pusta lista ma wartość False wieć not False = True
                return("Brak pracowników w bazie danych.")
            pracownik_info=[]
            for i, pracownik in enumerate(self.pracownicy, start=1):#enumerate tworzy listę krotek z Numerkiem (jakby indeksem) i wartością
                info=[f"Pracownik {i}:"]#lista pomocnicza, nadajemy jej Napis: Pracownik {numer indeksu}
                for pole, wartosc in pracownik.items():#.items() zwraca listę krotek (w każdej krotce znajdują się 2 elementy: klucz i wartość)
                    info.append(f"- {pole}: {wartosc}")#dodajemy ten string do listy (tyle elementów ile jest pracowników)
                pracownik_info.append('\n'.join(info))#dodajemy string do "głównej listy pomocniczej" który od nowej linii wyświetla info o pracowniku
                #.join() zamienia listę w ciąg znaków gdzie elementy oddzielone są nową linią
            return '\n'.join(pracownik_info)#zwraca cały opis wszystkich pracowników

    def zapisz_do_pliku(self):
        with open("dane.txt", "w",encoding='utf-8') as plik:#z otwartego pliku dane.txt zapisuj ('w') z kodowaniem utf-8 (polskie znaczki)
            for pracownik in self.pracownicy:
                for pole, wartosc in pracownik.items():#znowu zamiana na listę składającą się z krotek
                    plik.write(f"{pole}: {wartosc}\n")#dla każdej krotki (klucz, wartość) zapisz + nowa linia
                plik.write("\n")#zapisz na końcu znak nowej linii

    def wczytaj_z_pliku(self):
        try:
            with open("dane.txt", "r",encoding='utf-8') as plik:#czytaj z pliku
                linie = plik.readlines()#zwraca listę w której elementami są linie tekstu
                pracownik = {}#dane jednego pracownika
                for line in linie:
                    #.strip() usuwa białe znaki (spacje,tab, itp)
                    if line.strip():  # jeżeli linia nie jest pusta to kod się wykona
                        pole, wartosc = line.strip().split(": ")#dla każdej linni usuwa spację itp i tworzy listę elementów znajdujących się między ":"
                        pracownik[pole] = wartosc
                    else:#jeżeli linia jest pusta to zapisuję słownik na liście pracowników (jak dochodzimy do pustej linni to znaczy że informacje o 1 pracowniku się skończyły)
                        self.pracownicy.append(pracownik)
                        pracownik = {}#ustawiamy zmienną na pusty słownik aby można było wpisać info o drugim pracowniku
        except FileNotFoundError:
            pass  # ignoruj błąd, jeśli plik nie istnieje

    def usun_pracownika(self, nazwisko='0'):
        if self.pracownicy != []:#jeżeli lista nie jest pusta
            for pracownik in self.pracownicy:
                if pracownik["Nazwisko"] == nazwisko:#jeżeli wpisane nazwisko należy do danego pracownika to usuwa się go z listy i robi się zapis od nowa
                    self.pracownicy.remove(pracownik)
                    self.zapisz_do_pliku()
                    return(f"Pracownik o nazwisku {nazwisko} został usunięty z listy.")
                else:
                    return("Pracownik o podanym nazwisku nie został znaleziony")
        else:#jeżeli lista jest pusta
            return 'Baza danych jest pusta'
