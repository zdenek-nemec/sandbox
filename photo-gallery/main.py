import tkinter as tk

from photo_gallery import PhotoGallery


def main():
    root = tk.Tk()
    app = PhotoGallery(root)
    root.mainloop()


if __name__ == "__main__":
    main()
