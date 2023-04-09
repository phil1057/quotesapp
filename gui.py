#!/usr/bin/python3
import tkinter as tk

def add():
    root.destroy()
    add = tk.Tk()
    add.configure(height=720, width=1080)
    add.resizable(False, False)
    add.title("QuotesApp")
    topFrame = tk.Frame(add)
    topFrame.configure(height=85, width=1060)
    translateEn = tk.Radiobutton(topFrame)
    translateEn.configure(text='English')
    translateEn.grid(column=0, row=1, sticky="w")
    translateEn.configure(command=translate)
    translateFr = tk.Radiobutton(topFrame)
    translateFr.configure(text='Français')
    translateFr.grid(column=0, row=0, sticky="w")
    translateFr.configure(command=translate)
    labelKeywords = tk.Label(topFrame)
    labelKeywords.configure(text='Mot-Clés')
    labelKeywords.grid(column=0, row=2)
    entryKeywords = tk.Entry(topFrame)
    entryKeywords.grid(column=1, row=2)
    buttonKeywords = tk.Button(topFrame)
    buttonKeywords.configure(text='Filtrer')
    buttonKeywords.grid(column=2, row=2)
    labelTitre = tk.Label(topFrame)
    labelTitre.configure(
        font="{Arial} 36 {italic}",
        padx=400,
        text='" Citations "')
    labelTitre.grid(column=3, row=1, rowspan=2)
    topFrame.grid(column=0, padx=15, pady=5, row=0)
    topFrame.grid_propagate(0)
    middleFrame = tk.Frame(add)
    middleFrame.configure(height=30, width=1040)
    ajouterButton = tk.Button(middleFrame)
    ajouterButton.configure(text='add')
    ajouterButton.grid(column=0, row=0)
    modifierButton = tk.Button(middleFrame)
    modifierButton.configure(text='mod')
    modifierButton.grid(column=1, row=0)
    deleteButton = tk.Button(middleFrame)
    deleteButton.configure(text='del')
    deleteButton.grid(column=2, row=0)
    importButton = tk.Button(middleFrame)
    importButton.configure(text='imp')
    importButton.grid(column=3, row=0)
    exportButton = tk.Button(middleFrame)
    exportButton.configure(text='exp')
    exportButton.grid(column=4, row=0)
    copyButton = tk.Button(middleFrame)
    copyButton.configure(text='cop')
    copyButton.grid(column=5, row=0)
    precedantButton = tk.Button(middleFrame)
    precedantButton.configure(
        overrelief="flat",
        takefocus=False,
        text='Précédent',
        width=20)
    precedantButton.grid(column=6, padx=70, row=0)
    randomButton = tk.Button(middleFrame)
    randomButton.configure(text='Aléatoire', width=20)
    randomButton.grid(column=7, row=0)
    suivantButton = tk.Button(middleFrame)
    suivantButton.configure(text='Suivant', width=20)
    suivantButton.grid(column=8, padx=70, row=0)
    middleFrame.grid(column=0, pady=10, row=1)
    middleFrame.grid_propagate(0)
    bottomFrame = tk.Frame(add)
    bottomFrame.configure(height=570, width=1040)
    labelframe5 = tk.LabelFrame(bottomFrame)
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
    entry1 = tk.Entry(labelframe5)
    entry1.pack(side="top")
    labelframe5.grid(column=1, row=0)
    labelframe5.pack_propagate(0)
    Avatar = tk.Label(bottomFrame)
    img_avatar = tk.PhotoImage(file="avatar.png")
    Avatar.configure(
        height=200,
        image=img_avatar,
        text='label2',
        width=200)
    Avatar.grid(column=0, row=0, sticky="nw")
    AuteurLabel = tk.Label(bottomFrame)
    auteur = tk.StringVar(value='Joe Blo')
    AuteurLabel.configure(
        font="{Times New Roman} 11 {}",
        relief="ridge",
        text='Joe Blo',
        textvariable=auteur)
    AuteurLabel.grid(column=0, pady=182, row=0, sticky="nw")
    AuteurInfoLabel = tk.Label(bottomFrame)
    auteurInfo = tk.StringVar(
        value="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.\n\n")
    AuteurInfoLabel.configure(
        justify="left",
        text="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.\n\n",
        textvariable=auteurInfo,
        wraplength=200)
    AuteurInfoLabel.grid(pady=210, row=0, rowspan=10, sticky="nw")
    SourceLabel = tk.Label(bottomFrame)
    source = tk.StringVar(
        value="Source: Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.\n")
    SourceLabel.configure(
        justify="left",
        text="Source: Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.\n",
        textvariable=source,
        wraplength=200)
    SourceLabel.grid(pady=350, row=0, rowspan=100, sticky="w")
    bottomFrame.grid(column=0, row=2)
    bottomFrame.grid_propagate(0)
    add.grid_propagate(0)
    add.rowconfigure(2, uniform=1)

def edit():
    print("Hello, world!")

def delete():
    print("Hello, world!")

def importcsv():
    print("Hello, world!")

def export():
    print("Hello, world!")

def copy():
    print("Hello, world!")

class Main:
    def __init__(self, master=None):
        # build ui
        self.root = tk.Tk()
        self.root.configure(height=720, width=1080)
        self.root.resizable(False, False)
        self.root.title("QuotesApp")
        self.topFrame = tk.Frame(self.root)
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
        self.middleFrame = tk.Frame(self.root)
        self.middleFrame.configure(height=30, width=1040)

        self.ajouterButtonIcon = tk.PhotoImage(file="icons\plus.png")
        self.ajouterButton = tk.Button(self.middleFrame, image=self.ajouterButtonIcon, height=20, width=20, relief="flat")
        self.ajouterButton.configure(command=add)
        self.ajouterButton.grid(column=0, row=0)

        self.modifierButtonIcon = tk.PhotoImage(file="icons\edit.png")
        self.modifierButton = tk.Button(self.middleFrame, image=self.modifierButtonIcon, height=20, width=20, relief="flat")
        self.modifierButton.configure(command=edit)
        self.modifierButton.grid(column=1, row=0)

        self.deleteButton = tk.Button(self.middleFrame)
        self.deleteButtonIcon = tk.PhotoImage(file="icons\delete.png")
        self.deleteButton = tk.Button(self.middleFrame, image=self.deleteButtonIcon, height=20, width=20, relief="flat")
        self.deleteButton.configure(command=delete)
        self.deleteButton.grid(column=2, row=0)

        self.importButton = tk.Button(self.middleFrame)
        self.importButtonIcon = tk.PhotoImage(file="icons\input.png")
        self.importButton = tk.Button(self.middleFrame, image=self.importButtonIcon, height=20, width=20, relief="flat")
        self.importButton.configure(command=importcsv)
        self.importButton.grid(column=3, row=0)

        self.exportButton = tk.Button(self.middleFrame)
        self.exportButtonIcon = tk.PhotoImage(file="icons\output.png")
        self.exportButton = tk.Button(self.middleFrame, image=self.exportButtonIcon, height=20, width=20, relief="flat")
        self.exportButton.configure(command=export)
        self.exportButton.grid(column=4, row=0)

        self.copyButton = tk.Button(self.middleFrame)
        self.copyButtonIcon = tk.PhotoImage(file="icons\clipboard-copy.png")
        self.copyButton = tk.Button(self.middleFrame, image=self.copyButtonIcon, height=20, width=20, relief="flat")
        self.copyButton.config(command=copy)
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
        self.bottomFrame = tk.Frame(self.root)
        self.bottomFrame.configure(height=570, width=1040)
        self.labelframe5 = tk.LabelFrame(self.bottomFrame)
        self.labelframe5.configure(
            background="white",
            borderwidth=5,
            height=500,
            text='Citation\n',
            width=800)
        self.QuoteLabel = tk.Label(self.labelframe5)
        self.quote = tk.StringVar(value="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
        self.QuoteLabel.configure(
            background="#ffffff",
            font="{Times New Roman} 16 {italic}",
            text="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            textvariable=self.quote,
            wraplength=600)
        self.QuoteLabel.pack(
            anchor="center",
            fill="both",
            pady=100,
            side="top")
        self.labelframe5.grid(column=1, row=0)
        self.labelframe5.pack_propagate(0)
        self.Avatar = tk.Label(self.bottomFrame)
        self.img_avatar = tk.PhotoImage(file="avatar.png")
        self.Avatar.configure(
            height=200,
            image=self.img_avatar,
            text='label2',
            width=200)
        self.Avatar.grid(column=0, row=0, sticky="nw")
        self.AuteurLabel = tk.Label(self.bottomFrame)
        self.auteur = tk.StringVar(value='Joe Blo')
        self.AuteurLabel.configure(
            font="{Times New Roman} 11 {}",
            relief="ridge",
            text='Joe Blo',
            textvariable=self.auteur)
        self.AuteurLabel.grid(column=0, pady=182, row=0, sticky="nw")
        self.AuteurInfoLabel = tk.Label(self.bottomFrame)
        self.auteurInfo = tk.StringVar(
            value="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.\n\n")
        self.AuteurInfoLabel.configure(
            justify="left",
            text="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.\n\n",
            textvariable=self.auteurInfo,
            wraplength=200)
        self.AuteurInfoLabel.grid(pady=210, row=0, rowspan=10, sticky="nw")
        self.SourceLabel = tk.Label(self.bottomFrame)
        self.source = tk.StringVar(
            value="Source: Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.\n")
        self.SourceLabel.configure(
            justify="left",
            text="Source: Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.\n",
            textvariable=self.source,
            wraplength=200)
        self.SourceLabel.grid(pady=350, row=0, rowspan=100, sticky="w")
        self.bottomFrame.grid(column=0, row=2)
        self.bottomFrame.grid_propagate(0)
        self.root.grid_propagate(0)
        self.root.rowconfigure(2, uniform=1)

        # Main widget
        self.mainwindow = self.root

    def run(self):
        self.mainwindow.mainloop()

    def translate(self):
        pass


if __name__ == "__main__":
    app = Main().run()