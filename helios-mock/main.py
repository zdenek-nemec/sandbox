import tkinter as tk


class PageFields:
    """docstring for PageFields"""
    def __init__(self, app):
        self.app = app
        self.fields = {}
        self.frames = {}

    def add_field(self, frame: int, label: str = None):
        app = self.app
        frames = self.frames
        if frame not in frames:
            frames[frame] = tk.Frame(app)
            frames[frame].pack(side=tk.TOP)
        fields = self.fields
        fields[len(fields)] = {
            "label": tk.Label(frames[frame], text=label),
            "item": tk.Entry(frames[frame])
        }

    def add_dropdown(self, frame: int, label: str = None, selected: str = None, options: list[str] = None):
        app = self.app
        frames = self.frames
        if frame not in frames:
            frames[frame] = tk.Frame(app)
            frames[frame].pack(side=tk.TOP)
        fields = self.fields
        selected_var = tk.StringVar()
        selected_var.set(selected)
        fields[len(fields)] = {
            "label": tk.Label(frames[frame], text=label),
            "item": tk.OptionMenu(frames[frame], selected_var, *options)
        }

    def add_checkbox(self, frame: int, label: str = None, checked: bool = False):
        app = self.app
        frames = self.frames
        if frame not in frames:
            frames[frame] = tk.Frame(app)
            frames[frame].pack(side=tk.TOP)
        fields = self.fields
        status_var = tk.BooleanVar()
        status_var.set(checked)
        fields[len(fields)] = {
            "label": tk.Label(frames[frame], text=label),
            "item": tk.Checkbutton(frames[frame], variable=status_var),
            "checked": status_var
        }

    def display(self):
        fields = self.fields
        for field_id in fields.keys():
            fields[field_id]["label"].pack(side=tk.LEFT)
            fields[field_id]["item"].pack(side=tk.LEFT)


def submit_action(numbers: list[int], result_label: tk.Label):
    numbers[0] += 1
    result_label.config(text=f"{numbers[0]} ... ulozeno")


def main():
    print("Helios Nephrite Invoice Detail Mock")

    app = tk.Tk()
    app.title("Helios Nephrite Invoice Detail Mock")

    pf = PageFields(app)
    pf.add_field(1, "Interni cislo:")
    pf.add_field(1, "Cislo faktury:")
    pf.add_field(2, "Typ dod.:")
    pf.add_field(3, "Dodavatel:")
    pf.add_field(3)
    pf.add_field(4, "ICO:")
    pf.add_field(5, "DIC:")
    pf.add_field(5, "DIC vlastni:")
    pf.add_field(6, "Cislo uctu:")
    pf.add_field(6)
    pf.add_field(7, "Expozitura - dodavatel:")
    pf.add_field(7)
    pf.add_field(8, "Prijato:")
    pf.add_field(8, "DUZP:")
    pf.add_field(8, "Splatno:")
    pf.add_field(8, "Intrastat:")
    pf.add_field(9, "Datum porizeni:")
    pf.add_field(10, "Datum pripadu:")
    pf.add_dropdown(10, "Obdobi DPH:", "08", [f"{month:02}" for month in range(1, 13)])
    pf.add_dropdown(10, selected="2023", options=[f"{year}" for year in range(2020, 2030)])
    pf.add_checkbox(10, "Dodatecne danove priznani:", False)
    pf.add_checkbox(11, "Automaticke prepocitavani castek na formulari:", True)
    pf.add_checkbox(12, "Mena:", False)
    pf.add_field(12, "Datum kurzu:")
    pf.add_dropdown(12, "Kod meny:", "", options=["", "CZK", "EUR", "PLN"])
    pf.add_field(12)
    pf.add_field(12)
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
