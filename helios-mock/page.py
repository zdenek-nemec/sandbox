import tkinter as tk

from frame import Frame


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


if __name__ == "__main__":
    pass
