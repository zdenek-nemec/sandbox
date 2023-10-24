import tkinter as tk


class Frame:
    def __init__(self, app: tk.Tk, columns: int = 1):
        self.frame = tk.Frame(app)
        self.frame.pack(side=tk.TOP)
        self.items = []
        self.columns = columns

    def add_label(self, text: str = None):
        self.items.append({
            "item": tk.Label(self.frame, text=text)
        })

    def add_entry(self, text: str = ""):
        variable = tk.StringVar()
        variable.set(text)
        self.items.append({
            "item": tk.Entry(self.frame, textvariable=variable),
            "variable": variable,
            "default": text
        })

    def display(self):
        for i, item in enumerate(self.items):
            item["item"].grid(row=i // self.columns, column=i % self.columns)

    def clear(self):
        for item in self.items:
            if "variable" in item:
                item["variable"].set("")

    def reset(self):
        for item in self.items:
            if "variable" in item:
                item["variable"].set(item["default"])


class Page:
    def __init__(self, title: str):
        self.app = tk.Tk()
        self.app.title(title)
        self.frames = []
        self.current_frame = None
        self.submits = 0
        self.result_label = None
        self.buttons = None

    def submit_action(self):
        self.submits += 1
        self.result_label.config(text=f"{self.submits=}")

    def clear_action(self):
        self.submits = 0
        self.result_label.config(text=f"{self.submits=}")
        for frame in self.frames:
            frame.clear()

    def reset_action(self):
        self.submits = 0
        self.result_label.config(text=f"{self.submits=}")
        for frame in self.frames:
            frame.reset()

    def add_frame(self, columns: int = 1):
        frame = Frame(self.app, columns)
        self.frames.append(frame)
        self.current_frame = frame

    def add_label(self, text: str = ""):
        self.current_frame.add_label(text)

    def add_entry(self, text: str = ""):
        self.current_frame.add_entry(text)

    def display(self):
        for frame in self.frames:
            frame.display()

    def add_buttons(self):
        frame = tk.Frame(self.app)
        frame.pack(side=tk.TOP)
        self.result_label = tk.Label(frame, text=f"{self.submits=}")
        self.buttons = [
            tk.Button(self.app, text="Submit", width=20, command=self.submit_action),
            tk.Button(self.app, text="Clear", width=20, command=self.clear_action),
            tk.Button(self.app, text="Reset", width=20, command=self.reset_action),
            tk.Button(self.app, text="Exit", width=20, fg="white", bg="red", command=self.app.destroy)
        ]
        self.result_label.pack(side=tk.LEFT)
        for item in self.buttons:
            item.pack(side=tk.LEFT)

    def run(self):
        self.app.mainloop()


def main():
    page = Page("Helios Green 2VV Order Detail Mock")

    page.add_frame(columns=4)
    page.add_label(text="Typ:")
    page.add_entry(text="ABC")
    page.add_label(text="Stav:")
    page.add_entry()
    page.add_label(text="Interní číslo:")
    page.add_entry(text="12345")
    page.add_label(text="Externí číslo:")
    page.add_entry()
    page.add_label(text="Druh dopravy:")
    page.add_entry()
    page.add_label(text="Datum objednávky:")
    page.add_entry()
    page.add_label(text="Druh:")
    page.add_entry()
    page.add_label(text="Datum ceny:")
    page.add_entry()
    page.add_label(text="Sklad:")
    page.add_entry()
    page.add_label(text="Datum nakládky:")
    page.add_entry()
    page.add_label(text="Cenová úroveň:")
    page.add_entry()
    page.add_label(text="Datum vykládky:")
    page.add_entry()
    page.add_label(text="DIČ Vlastní:")
    page.add_entry()
    page.add_label(text="Realizováno:")
    page.add_entry()
    page.display()

    page.add_frame(columns=3)
    page.add_label(text="Dopravce:")
    page.add_entry()
    page.add_entry()
    page.add_label(text="IČ:")
    page.add_entry()
    page.add_entry()
    page.add_label(text="Expozitura - dodavatel:")
    page.add_entry()
    page.add_entry()
    page.add_label(text="Zakázka:")
    page.add_entry()
    page.add_entry()
    page.add_label(text="Aktivita:")
    page.add_entry()
    page.add_entry()
    page.add_label(text="Útvar:")
    page.add_entry()
    page.add_entry()
    page.add_label(text="Organizace místo vykládky:")
    page.add_entry()
    page.add_entry()
    page.add_label(text="Expozitura místo vykládky:")
    page.add_entry()
    page.add_entry()
    page.add_label(text="Sklad 2:")
    page.add_entry()
    page.add_entry()
    page.display()

    page.add_buttons()

    page.run()


if __name__ == "__main__":
    main()
