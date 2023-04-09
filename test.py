#!/usr/bin/python3
import tkinter as tk


class AddUiApp:
    def __init__(self, master=None):
        # build ui
        self.add = tk.Tk() if master is None else tk.Toplevel(master)
        self.add.configure(height=720, width=1080)
        self.add.resizable(False, False)
        self.add.title("QuotesApp")
        self.topFrame = tk.Frame(self.add)
        self.topFrame.configure(height=85, width=1060)
        self.translateEn = tk.Radiobutton(self.topFrame)
        self.translateEn.configure(text='English')
        self.translateEn.grid(column=0, row=1, sticky="w")
        self.translateEn.configure(command=self.translate)
        self.translateFr = tk.Radiobutton(self.topFrame)
        self.translateFr.configure(text='Français')
        self.translateFr.grid(column=0, row=0, sticky="w")
        self.translateFr.configure(command=self.translate)
        self.labelKeywords = tk.Label(self.topFrame)
        self.labelKeywords.configure(text='Mot-Clés')
        self.labelKeywords.grid(column=0, row=2)
        self.entryKeywords = tk.Entry(self.topFrame)
        self.entryKeywords.grid(column=1, row=2)
        self.buttonKeywords = tk.Button(self.topFrame)
        self.buttonKeywords.configure(text='Filtrer')
        self.buttonKeywords.grid(column=2, row=2)
        self.labelTitre = tk.Label(self.topFrame)
        self.labelTitre.configure(
            font="{Arial} 36 {italic}",
            padx=400,
            text='" Citations "')
        self.labelTitre.grid(column=3, row=1, rowspan=2)
        self.topFrame.grid(column=0, padx=15, pady=5, row=0)
        self.topFrame.grid_propagate(0)
        self.middleFrame = tk.Frame(self.add)
        self.middleFrame.configure(height=30, width=1040)
        self.ajouterButton = tk.Button(self.middleFrame)
        self.ajouterButton.configure(text='add')
        self.ajouterButton.grid(column=0, row=0)
        self.modifierButton = tk.Button(self.middleFrame)
        self.modifierButton.configure(text='mod')
        self.modifierButton.grid(column=1, row=0)
        self.deleteButton = tk.Button(self.middleFrame)
        self.deleteButton.configure(text='del')
        self.deleteButton.grid(column=2, row=0)
        self.importButton = tk.Button(self.middleFrame)
        self.importButton.configure(text='imp')
        self.importButton.grid(column=3, row=0)
        self.exportButton = tk.Button(self.middleFrame)
        self.exportButton.configure(text='exp')
        self.exportButton.grid(column=4, row=0)
        self.copyButton = tk.Button(self.middleFrame)
        self.copyButton.configure(text='cop')
        self.copyButton.grid(column=5, row=0)
        self.precedantButton = tk.Button(self.middleFrame)
        self.precedantButton.configure(
            overrelief="flat",
            takefocus=False,
            text='Précédent',
            width=20)
        self.precedantButton.grid(column=6, padx=70, row=0)
        self.randomButton = tk.Button(self.middleFrame)
        self.randomButton.configure(text='Aléatoire', width=20)
        self.randomButton.grid(column=7, row=0)
        self.suivantButton = tk.Button(self.middleFrame)
        self.suivantButton.configure(text='Suivant', width=20)
        self.suivantButton.grid(column=8, padx=70, row=0)
        self.middleFrame.grid(column=0, pady=10, row=1)
        self.middleFrame.grid_propagate(0)
        self.addFrame = tk.Frame(self.add)
        self.addFrame.configure(height=570, width=1040)
        labelframe5 = tk.LabelFrame(self.addFrame)
        labelframe5.configure(
            background="white",
            borderwidth=5,
            height=500,
            highlightbackground="#ffffff",
            highlightcolor="#ffffff",
            highlightthickness=3,
            labelanchor="nw",
            text='Citation\n',
            width=800)
        addQuoteText = tk.Text(labelframe5)
        addQuoteText.configure(height=500, width=800)
        addQuoteText.pack(side="top")
        labelframe5.grid(column=1, row=0)
        labelframe5.pack_propagate(0)
        self.Avatar = tk.Label(self.addFrame)
        self.img_avatar = tk.PhotoImage(file="avatar.png")
        self.Avatar.configure(
            height=200,
            image=self.img_avatar,
            text='label2',
            width=200)
        self.Avatar.grid(column=0, row=0, sticky="nw")
        self.nomAuteur = tk.Entry(self.addFrame)
        self.nomAuteur.grid(column=0, pady=182, row=0, sticky="nw")
        self.descAuteur = tk.Text(self.addFrame)
        self.descAuteur.configure(height=10, width=23)
        self.descAuteur.grid(
            column=0,
            pady=220,
            row=0,
            rowspan=100,
            sticky="nw")
        self.labelDesc = tk.Label(self.addFrame)
        self.labelDesc.configure(text="Description de l'auteur")
        self.labelDesc.grid(column=0, pady=205, row=0, sticky="nw")
        self.source = tk.Text(self.addFrame)
        self.source.configure(height=10, width=23)
        self.source.grid(column=0, pady=390, row=0, rowspan=100, sticky="nw")
        self.labelSource = tk.Label(self.addFrame)
        self.labelSource.configure(text='Source')
        self.labelSource.grid(
            column=0,
            pady=380,
            row=0,
            rowspan=1000,
            sticky="nw")
        self.Confirmer = tk.Button(self.addFrame)
        self.Confirmer.configure(text='Confirmer', width=20)
        self.Confirmer.grid(column=1, padx=5, row=1, sticky="w")
        self.Annuler = tk.Button(self.addFrame)
        self.Annuler.configure(text='Annuler', width=20)
        self.Annuler.grid(column=1, padx=200, row=1, sticky="w")
        self.addFrame.grid(column=0, row=2)
        self.addFrame.grid_propagate(0)
        self.add.grid_propagate(0)
        self.add.rowconfigure(2, uniform=1)

        # Main widget
        self.mainwindow = self.add

    def run(self):
        self.mainwindow.mainloop()

    def translate(self):
        pass


if __name__ == "__main__":
    app = AddUiApp()
    app.run()

