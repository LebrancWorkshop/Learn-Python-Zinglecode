import tkinter as tk

window = tk.Tk()
window.title("Vera GUI")
window.minsize(400, 300)


def show_table():
  content = ""
  text = text_input.get()
  num = int(text)
  for i in range(1, 13):
    content += f"{num} x {i} = {num * i}\n"
  content_label.configure(text=content)

header_label = tk.Label(master=window, text="Vera GUI 1.0")
header_label.pack()

text_input = tk.Entry(master=window)
text_input.pack()

ok_button = tk.Button(master=window, text="OK", command=show_table)
ok_button.pack()

content_label = tk.Label(master=window, text="")
content_label.pack()

window.mainloop()
