import tkinter as tk


# Function to update the label text with the content of the input boxes
def update_label():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    full_name = f"Full Name: {first_name} {last_name}"
    label_result.config(text=full_name)


def main():
    print("Helios Nephrite Invoice Detail Mock")

    # Create the main application window
    app = tk.Tk()
    app.title("Helios Nephrite Invoice Detail Mock")

    # Create Entry widgets for first name and last name
    label_first_name = tk.Label(app, text="First Name:")
    entry_first_name = tk.Entry(app)

    label_last_name = tk.Label(app, text="Last Name:")
    entry_last_name = tk.Entry(app)

    # Create a button to trigger the update_label function
    update_button = tk.Button(app, text="Update", command=update_label)

    # Create a label to display the result
    label_result = tk.Label(app, text="Full Name: ")

    # Pack the widgets into the window
    label_first_name.pack()
    entry_first_name.pack()
    label_last_name.pack()
    entry_last_name.pack()
    update_button.pack()
    label_result.pack()

    # Start the Tkinter event loop
    app.mainloop()


if __name__ == "__main__":
    main()
