import tkinter as tk

def afficher_message():
    texte = entree.get().strip()
    if texte:
        message.config(text=texte)

fenetre = tk.Tk()
fenetre.title("Carnet de messages")
fenetre.geometry("380x220")

message = tk.Label(fenetre, text="Bonjour", font=("Arial", 18))
message.pack(pady=20)
entree = tk.Entry(fenetre, width=32)
entree.pack()
bouton = tk.Button(fenetre, text="Afficher", command=afficher_message)
bouton.pack(pady=16)

fenetre.mainloop()
