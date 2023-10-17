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


if __name__ == "__main__":
    pass
