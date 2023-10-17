import tkinter as tk


class Frame:
    """docstring for Frame"""
    def __init__(self, app: tk.Tk):
        self.frame = self._create_frame(app)
        self.fields = {}

    def _create_frame(self, app: tk.Tk):
        frame = tk.Frame(app)
        frame.pack(side=tk.TOP)
        return frame

    def add_field(self, label: str = None):
        frame = self.frame
        fields = self.fields
        fields[len(fields)] = {
            "label": tk.Label(frame, text=label),
            "item": tk.Entry(frame)
        }

    def add_dropdown(self, label: str = None, selected: str = None, options: list[str] = None):
        frame = self.frame
        fields = self.fields
        selected_var = tk.StringVar()
        selected_var.set(selected)
        fields[len(fields)] = {
            "label": tk.Label(frame, text=label),
            "item": tk.OptionMenu(frame, selected_var, *options)
        }

    def add_checkbox(self, label: str = None, checked: bool = False):
        frame = self.frame
        fields = self.fields
        status_var = tk.BooleanVar()
        status_var.set(checked)
        fields[len(fields)] = {
            "label": tk.Label(frame, text=label),
            "item": tk.Checkbutton(frame, variable=status_var),
            "checked": status_var
        }

    def display(self):
        fields = self.fields
        for field_id in sorted(fields.keys()):
            fields[field_id]["label"].pack(side=tk.LEFT)
            fields[field_id]["item"].pack(side=tk.LEFT)


class Page:
    """docstring for Page"""
    def __init__(self, title: str):
        self.app = tk.Tk()
        self.app.title(title)
        self.frames = {}
        self.current_frame = None
        self.result_label = None
        self.buttons = []
        self.submits = 0

    def add_frame(self):
        frame = Frame(self.app)
        self.frames[len(self.frames)] = frame
        self.current_frame = frame

    def add_field(self, label: str = None):
        self.current_frame.add_field(label)

    def add_dropdown(self, label: str = None, selected: str = None, options: list[str] = None):
        self.current_frame.add_dropdown(label, selected, options)

    def add_checkbox(self, label: str = None, checked: bool = False):
        self.current_frame.add_checkbox(label, checked)

    def add_result(self):
        self.result_label = tk.Label(self.app, text=f"{self.submits=}")

    def add_buttons(self):
        app = self.app
        self.add_frame()
        self.buttons = [
            tk.Button(app, text="Submit", width=20, command=self.submit_action),
            tk.Button(app, text="Reset", width=20, command=self.reset_action),
            tk.Button(app, text="Exit", width=20, fg="white", bg="red", command=app.destroy)
        ]

    def submit_action(self):
        self.submits += 1
        self.result_label.config(text=f"{self.submits=}")

    def reset_action(self):
        self.submits = 0
        self.result_label.config(text=f"{self.submits=}")

    def display(self):
        for frame_id in sorted(self.frames.keys()):
            self.frames[frame_id].display()
        if self.result_label:
            self.result_label.pack()
        for button in self.buttons:
            button.pack(side=tk.LEFT)

    def run_loop(self):
        self.app.mainloop()


def main():
    print("Helios Nephrite EPL Invoice Detail Mock")

    page = Page("Helios Nephrite EPL Invoice Detail Mock")
    page.add_frame()
    page.add_field("Interni cislo:")
    page.add_field("Cislo faktury:")
    page.add_frame()
    page.add_field("Typ dod.:")
    page.add_frame()
    page.add_field("Dodavatel:")
    page.add_field()
    page.add_frame()
    page.add_field("ICO:")
    page.add_frame()
    page.add_field("DIC:")
    page.add_field("DIC vlastni:")
    page.add_frame()
    page.add_field("Cislo uctu:")
    page.add_field()
    page.add_frame()
    page.add_field("Expozitura - dodavatel:")
    page.add_field()
    page.add_frame()
    page.add_field("Prijato:")
    page.add_field("DUZP:")
    page.add_field("Splatno:")
    page.add_field("Intrastat:")
    page.add_frame()
    page.add_field("Datum porizeni:")
    page.add_frame()
    page.add_field("Datum pripadu:")
    page.add_dropdown("Obdobi DPH:", "08", [f"{month:02}" for month in range(1, 13)])
    page.add_dropdown(selected="2023", options=[f"{year}" for year in range(2020, 2030)])
    page.add_checkbox("Dodatecne danove priznani:", False)
    page.add_frame()
    page.add_checkbox("Automaticke prepocitavani castek na formulari:", True)
    page.add_frame()
    page.add_checkbox("Mena:", False)
    page.add_field("Datum kurzu:")
    page.add_dropdown("Kod meny:", "", options=["", "CZK", "EUR", "PLN"])
    page.add_field()
    page.add_field()
    page.add_result()
    page.add_buttons()
    page.display()
    page.run_loop()


if __name__ == "__main__":
    main()
