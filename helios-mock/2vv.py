import tkinter as tk


def main():
    app = tk.Tk()
    app.title("Helios Green 2VV Order Detail Mock")

    frame1 = tk.Frame(app)
    frame1.pack(side=tk.TOP)
    items1 = [
        tk.Label(frame1, text="Typ:"),
        tk.Entry(frame1),
        tk.Label(frame1, text="Stav:"),
        tk.Entry(frame1),
        tk.Label(frame1, text="Interní číslo:"),
        tk.Entry(frame1),
        tk.Label(frame1, text="Externí číslo:"),
        tk.Entry(frame1),
        tk.Label(frame1, text="Druh dopravy:"),
        tk.Entry(frame1),
        tk.Label(frame1, text="Datum objednávky:"),
        tk.Entry(frame1),
        tk.Label(frame1, text="Druh:"),
        tk.Entry(frame1),
        tk.Label(frame1, text="Datum ceny:"),
        tk.Entry(frame1),
        tk.Label(frame1, text="Sklad:"),
        tk.Entry(frame1),
        tk.Label(frame1, text="Datum nakládky:"),
        tk.Entry(frame1),
        tk.Label(frame1, text="Cenová úroveň:"),
        tk.Entry(frame1),
        tk.Label(frame1, text="Datum vykládky:"),
        tk.Entry(frame1),
        tk.Label(frame1, text="DIČ Vlastní:"),
        tk.Entry(frame1),
        tk.Label(frame1, text="Realizováno:"),
        tk.Entry(frame1)
    ]
    for i, item in enumerate(items1):
        item.grid(row=i // 4, column=i % 4)

    frame2 = tk.Frame(app)
    frame2.pack(side=tk.TOP)
    items2 = [
        tk.Label(frame2, text="Dopravce:"),
        tk.Entry(frame2),
        tk.Entry(frame2),
        tk.Label(frame2, text="IČ:"),
        tk.Entry(frame2),
        tk.Entry(frame2),
        tk.Label(frame2, text="Expozitura - dodavatel:"),
        tk.Entry(frame2),
        tk.Entry(frame2),
        tk.Label(frame2, text="Zakázka:"),
        tk.Entry(frame2),
        tk.Entry(frame2),
        tk.Label(frame2, text="Aktivita:"),
        tk.Entry(frame2),
        tk.Entry(frame2),
        tk.Label(frame2, text="Útvar:"),
        tk.Entry(frame2),
        tk.Entry(frame2),
        tk.Label(frame2, text="Organizace místo vykládky:"),
        tk.Entry(frame2),
        tk.Entry(frame2),
        tk.Label(frame2, text="Expozitura místo vykládky:"),
        tk.Entry(frame2),
        tk.Entry(frame2),
        tk.Label(frame2, text="Sklad 2:"),
        tk.Entry(frame2),
        tk.Entry(frame2)
    ]
    for i, item in enumerate(items2):
        item.grid(row=i // 3, column=i % 3)

    app.mainloop()


if __name__ == "__main__":
    main()
