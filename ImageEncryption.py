import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import font
import os


def operate(key):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()

    try:
        with open(file_path, 'rb') as file:
            data = bytearray(file.read())
            for i in range(len(data)):
                data[i] = data[i] ^ key
        with open(file_path, 'wb') as file:
            file.write(data)
        messagebox.showinfo("Done", "Process complete")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def main():
    print("this is testing")
    root = tk.Tk()
    root.title("Image Operation")
    root.geometry("400x400")
    root.configure(bg='white')
    root.resizable(False, False)
    roboto_font = font.Font(family="Roboto", size=25, weight="bold")

    button = tk.Button(root, text="Open Image", font=roboto_font, command=lambda: operate(int(textField.get())))
    button.pack(pady=20)

    textField = tk.Entry(root, font=roboto_font)
    textField.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()

