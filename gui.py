import tkinter as tk
import hrms_d as HRMS
class HRMSGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("HRMS System")

        self.hrms = HRMS.HRMS()

        self.employee_name_label = tk.Label(root, text="Imię:")#etykieta odnosząca się do okienka root z tekstem
        self.employee_name_label.pack()#dzięki temu etykieta się wyświetla

        self.employee_name_entry = tk.Entry(root)#dodawanie miejsca na wpisanie czegoś w okienku root
        self.employee_name_entry.pack()

        self.employee_surname_label = tk.Label(root, text="Nazwisko:")
        self.employee_surname_label.pack()

        self.employee_surname_entry = tk.Entry(root)
        self.employee_surname_entry.pack()

        self.workplace_label = tk.Label(root, text="Stanowisko:")
        self.workplace_label.pack()

        self.workplace_entry = tk.Entry(root)
        self.workplace_entry.pack()

        self.date_of_employment_label = tk.Label(root, text="Data zatrudnienia:")
        self.date_of_employment_label.pack()

        self.date_of_employment_entry = tk.Entry(root)
        self.date_of_employment_entry.pack()

        self.reward_label = tk.Label(root, text="Wynagrodzenie:")
        self.reward_label.pack()

        self.reward_entry = tk.Entry(root)
        self.reward_entry.pack()

        self.add_employee_button = tk.Button(root, text="Dodaj pracownika", command=self.add_employee)#dodanie guzika który wykonuje funkcje self.add_employee po naciśnięciu
        self.add_employee_button.pack()

        self.show_employees_button = tk.Button(root, text="Wyświetl pracowników", command=self.show_employees)
        self.show_employees_button.pack()

        self.employee_name_update_label = tk.Label(root, text="Nazwisko pracownika do aktualizacji:")
        self.employee_name_update_label.pack()

        self.employee_name_update_entry = tk.Entry(root)
        self.employee_name_update_entry.pack()

        self.update_field_label = tk.Label(root, text="Pole do aktualizacji:")
        self.update_field_label.pack()
# a tutaj robi się ciekawie :)
        self.v=tk.StringVar(root,'1') #srtingVar to inaczej zmienna tekstowa (zapisana tak bo odnosi się do tkintera)
#tworzymy słownik z punkcikami które mają się wyświetlić i wartości które są dla danego zaznaczenia
        self.values ={'Imię':'1',
                      'Nazwisko':'2',
                      'Stanowisko': '3', 
                      'Data':'4',
                      'Zarobki':'5'}
        for text,value in self.values.items():
            self.place_button=tk.Radiobutton(root,text=text,variable=self.v,value=value).pack(side="top",ipadx=5)
    #radiobutton odnosi się do roota, wyświetla tekst czyli key ze słownika, wartość którą zaznaczymy będzie przechowywać zmienna self.v, no i pobierane wartości to values ze słownika

        self.new_value_label = tk.Label(root, text="Nowa wartość:")
        self.new_value_label.pack()

        self.new_value_entry = tk.Entry(root)
        self.new_value_entry.pack()

        self.update_employee_button = tk.Button(root, text="Aktualizuj pracownika", command=self.update_employee)
        self.update_employee_button.pack()

        self.delete_employee_label=tk.Label(root,text='Nazwisko pracownika do usunięcia')
        self.delete_employee_label.pack()

        self.delete_employee_entry = tk.Entry(root)
        self.delete_employee_entry.pack()

        self.delete_employee_button = tk.Button(root,text='Usuń',command=self.delete_employee)
        self.delete_employee_button.pack()

        

        self.output_text = tk.Text(root, height=10, width=40)#prowadza okienko w którym wyświetla się tekst
        self.output_text.pack()

    def add_employee(self):
        name = self.employee_name_entry.get()#pobiera zawartość z okienka wejścia
        surname = self.employee_surname_entry.get()
        workplace = self.workplace_entry.get()
        date_of_employment = self.date_of_employment_entry.get()
        reward = self.reward_entry.get()
        self.clear_input_fields()#czyści pola wpisu Entry
        self.output_text.delete(1.0, tk.END)#usuwa tekst który się wyświetla
        self.output_text.insert(tk.END, self.hrms.dodaj_pracownika(name, surname, workplace, date_of_employment, reward))#pokazuje tekst który odnosi się do funkcji w module hrms

    def show_employees(self):
        employees_info = self.hrms.wyswietl_pracownikow()
        self.clear_input_fields()
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END,'Lista pracowników: \n')
        self.output_text.insert(tk.END, employees_info)

    def update_employee(self):
        name = self.employee_name_update_entry.get()
        place = self.v.get()
        match place:#rozważ dane wartości dla zmiennej place
            case "1":# jeżeli zmienna ma wartość '1' to...
                place='Imię'
            case "2":
                place='Nazwisko'
            case '3':
                place='Stanowisko'
            case '4':
                place='Data zatrudnienia'
            case '5':
                place='Wynagrodzenie'
        new_value = self.new_value_entry.get()
        result = self.hrms.aktualizuj_pracownika(name, place, new_value)#odnoszenie się do zmiennej w module hrms
        self.clear_input_fields()
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, result)

    def delete_employee(self):
        surname=self.delete_employee_entry.get()
        self.clear_input_fields()
        self.output_text.delete(1.0, tk.END)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END,self.hrms.usun_pracownika(surname))

    def clear_input_fields(self):
        self.employee_name_entry.delete(0, tk.END)
        self.employee_surname_entry.delete(0, tk.END)
        self.workplace_entry.delete(0, tk.END)
        self.date_of_employment_entry.delete(0, tk.END)
        self.reward_entry.delete(0, tk.END)
        self.employee_name_update_entry.delete(0, tk.END)
        self.new_value_entry.delete(0, tk.END)