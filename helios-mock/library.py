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

    def _display_packed(self, items: list):
        for item in items:
            item.pack(side=tk.LEFT)

    def _display_grid(self, items: list, columns: int = 2):
        for i, item in enumerate(items):
            item.grid(row=i // columns, column=i % columns)

    def display(self):
        for frame_id in sorted(self.frames.keys()):
            self.frames[frame_id].display()
        if self.result_label:
            self.result_label.pack()
        self._display_packed(self.buttons)

    def run_loop(self):
        self.app.mainloop()


if __name__ == "__main__":
    pass
