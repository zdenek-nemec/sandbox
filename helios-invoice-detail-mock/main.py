import tkinter as tk


class PageFields:
    """docstring for PageFields"""
    def __init__(self, app):
        self.app = app
        self.fields = {}

    def add_field(self, label: str = None):
        app = self.app
        fields = self.fields
        fields[len(fields)] = {
            "label": tk.Label(app, text=label),
            "item": tk.Entry(app)
        }

    def add_dropdown(self, label: str = None, selected: str = None, options: list[str] = None):
        app = self.app
        fields = self.fields
        selected_var = tk.StringVar()
        selected_var.set(selected)
        fields[len(fields)] = {
            "label": tk.Label(app, text=label),
            "item": tk.OptionMenu(app, selected_var, *options)
        }

    def add_checkbox(self, label: str = None, checked: bool = False):
        app = self.app
        fields = self.fields
        status_var = tk.BooleanVar()
        status_var.set(checked)
        fields[len(fields)] = {
            "label": tk.Label(app, text=label),
            "item": tk.Checkbutton(app, variable=status_var),
            "checked": status_var
        }

    def display(self):
        fields = self.fields
        for field_id in fields.keys():
            fields[field_id]["label"].pack()
            fields[field_id]["item"].pack()


def submit_action(numbers: list[int], result_label: tk.Label):
    numbers[0] += 1
    result_label.config(text=f"{numbers[0]} ... ulozeno")


def main():
    print("Helios Nephrite Invoice Detail Mock")

    app = tk.Tk()
    app.title("Helios Nephrite Invoice Detail Mock")

    pf = PageFields(app)
    pf.add_field("Interni cislo:")
    pf.add_field("Cislo faktury:")
    pf.add_field("Typ dod.:")
    pf.add_field("Dodavatel:")
    pf.add_field()
    pf.add_field("ICO:")
    pf.add_field("DIC:")
    pf.add_field("DIC vlastni:")
    pf.add_field("Cislo uctu:")
    pf.add_field()
    pf.add_field("Expozitura - dodavatel:")
    pf.add_field()
    pf.add_field("Prijato:")
    pf.add_field("DUZP:")
    pf.add_field("Splatno:")
    pf.add_field("Intrastat:")
    pf.add_field("Datum porizeni:")
    pf.add_field("Datum pripadu:")
    pf.add_dropdown("Obdobi DPH:", "08", [f"{month:02}" for month in range(1, 13)])
    pf.add_dropdown(selected="2023", options=[f"{year}" for year in range(2020, 2030)])
    pf.add_checkbox("Dodatecne danove priznani:", False)
    pf.add_checkbox("Autoaticke prepocitavani castek na formulari:", True)
    pf.add_checkbox("Mena:", False)
    pf.add_field("Datum kurzu:")
    pf.add_dropdown("Kod meny:", "", options=["", "CZK", "EUR", "PLN"])
    pf.add_field()
    pf.add_field()
    pf.display()

    numbers = [0]
    result_label = tk.Label(app, text=f"{numbers[0]} ... zadne zmeny")
    submit_button = tk.Button(app, text="Ulozit", command=lambda: submit_action(numbers, result_label))
    exit_button = tk.Button(app, text="Exit", command=app.destroy)
    result_label.pack()
    submit_button.pack()
    exit_button.pack()

    app.mainloop()


if __name__ == "__main__":
    main()
