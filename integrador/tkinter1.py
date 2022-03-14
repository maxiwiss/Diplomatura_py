import tkinter as tk
from tkinter import E, END, Frame, ttk
from PIL import ImageTk, Image
import os


BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
ruta = os.path.join(BASE_DIR, "lupa.png")

maintk = tk.Tk()
maintk.title("Biblioteca.py (v1.0)")
maintk.config(background="white")
# El frame va a contener el grid, para poder centrarlo en la ventana
frame = Frame(maintk, bg="white")
# --------------SUPERIOR------------------------
blancolb = tk.Label(frame, text="BIBLIOTECA", bg="white", font="Arial 18")
nombrelb = tk.Label(frame, text="NOMBRE", bg="#d9d9d9",
                    font="Arial 12", width="15", height="1")
editoriallb = tk.Label(frame, text="EDITORIAL", bg="#d9d9d9",
                       font="Arial 12", width="15", height="1")
autorlb = tk.Label(frame, text="AUTOR", bg="#d9d9d9",
                   font="Arial 12", width="15", height="1")
generolb = tk.Label(frame, text="GENERO", bg="#d9d9d9",
                    font="Arial 12", width="15", height="1")
stocklb = tk.Label(frame, text="STOCK", bg="#d9d9d9",
                   font="Arial 12", width="15", height="1")
nombretry = tk.Entry(frame, bg="#efefef", font="Arial 12", relief=tk.FLAT,
                     bd=3)
editorialtry = tk.Entry(frame, bg="#efefef", font="Arial 12", relief=tk.FLAT,
                        bd=3)
autortry = tk.Entry(frame, bg="#efefef", font="Arial 12", relief=tk.FLAT,
                    bd=3)
generotry = tk.Entry(frame, bg="#efefef", font="Arial 12", relief=tk.FLAT,
                     bd=3)
stocktry = tk.Entry(frame, bg="#efefef", font="Arial 12", relief=tk.FLAT,
                    bd=3)
ingresarbt = tk.Button(frame, text="INGRESAR", bg="#80FF97", bd=0,
                       width="38", relief=tk.FLAT, activebackground="#CCFFD5",
                       font="Arial 12", cursor="hand2")
separador = tk.Label(frame, text=f"{'___'*47}", bg="white")

blancolb.grid(column=0, row=0, columnspan=4)
nombrelb.grid(column=0, row=1, padx=7, pady=12)
editoriallb.grid(column=0, row=2, padx=7, pady=12)
autorlb.grid(column=0, row=3, padx=7, pady=12)
nombretry.grid(column=1, row=1, padx=7, pady=12)
editorialtry.grid(column=1, row=2, padx=7, pady=12)
autortry.grid(column=1, row=3, padx=7, pady=12)
generolb.grid(column=2, row=1, padx=7, pady=12)
stocklb.grid(column=2, row=2, padx=7, pady=12)
ingresarbt.grid(column=2, row=3, columnspan=2, padx=7, pady=12)
generotry.grid(column=3, row=1, padx=7, pady=12)
stocktry.grid(column=3, row=2, padx=7, pady=12)

separador.grid(column=0, row=4, columnspan=4, pady=20)
# ---------------INFERIOR-----------------
lupa = Image.open(ruta)
lupa = lupa.resize((29, 29), Image.ANTIALIAS)
lupa = ImageTk.PhotoImage(lupa)
buscartry = tk.Entry(frame, bg="#efefef", font="Arial 14 italic",
                     relief=tk.FLAT, bd=3, fg="#999999", width="48")
buscarbt = tk.Button(frame, width="30", height="30", bd=0, relief=tk.FLAT,
                     image=lupa, cursor="hand2")
buscartry.insert(END, "BUSCAR...")
eliminarbt = tk.Button(frame, text="ELIMINAR", bg="#FF5976", bd=0,
                       width="17", relief=tk.FLAT, activebackground="#FFA6B5",
                       font="Arial 12", cursor="hand2")
devolverbt = tk.Button(frame, text="DEVOLVER", bg="#4D6CFF", bd=0,
                       width="17", relief=tk.FLAT, activebackground="#99AAFF",
                       font="Arial 12", cursor="hand2")
prestarbt = tk.Button(frame, text="PRESTAR", bg="#80FF97", bd=0,
                      width="17", relief=tk.FLAT, activebackground="#CCFFD5",
                      font="Arial 12", cursor="hand2")
modifbt = tk.Button(frame, text="MODIFICAR", bg="#FFD966", bd=0,
                    width="17", relief=tk.FLAT, activebackground="#FFECB3",
                    font="Arial 12", cursor="hand2")

tree = ttk.Treeview(frame)
tree["columns"] = ("col1", "col2", "col3", "col4", "col5", "col6")
tree.column("#0", width=53)
tree.column("col1", width=180)
tree.column("col2", width=100)
tree.column("col3", width=120)
tree.column("col4", width=120)
tree.column("col5", width=45)
tree.column("col6", width=72)
tree.heading("#0", text="CÓDIGO")
tree.heading("col1", text="NOMBRE")
tree.heading("col2", text="EDITORIAL")
tree.heading("col3", text="AUTOR")
tree.heading("col4", text="GÉNERO")
tree.heading("col5", text="STOCK")
tree.heading("col6", text="PRESTADOS")

buscarbt.grid(column=0, row=5, pady=12, sticky=E)
buscartry.grid(column=1, row=5, padx=7, pady=12, columnspan=4)
tree.grid(column=0, row=6, columnspan=4)
eliminarbt.grid(column=0, row=7, padx=7, pady=12)
devolverbt.grid(column=1, row=7, padx=7, pady=12)
prestarbt.grid(column=2, row=7, padx=7, pady=12)
modifbt.grid(column=3, row=7, padx=7, pady=12)

frame.pack(expand=True)
maintk.mainloop()
