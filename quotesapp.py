#!/usr/bin/python3
import tkinter as tk
import sqlite3
from numpy import random
from tkinter import filedialog
import csv
import os.path
from pathlib import Path
from PIL import ImageTk, Image
from deep_translator import GoogleTranslator
import pandas as pd

#localPath = "C:/Users/Utilisateur/OneDrive/Documents/0prog/design_app/tp2/"
localPath = ""

db = 'quotes.db'
con = sqlite3.connect(db)
cursor = con.cursor()
lastQuote = []

def add(action):
    if action == '':
        addFrame = tk.Frame(root)
        addFrame.configure(height=570, width=1040)
        labelframe5 = tk.LabelFrame(addFrame)
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
        labelframe5.grid(column=1, row=0)
        labelframe5.pack_propagate(0)
        global addQuoteText
        addQuoteText = tk.Text(labelframe5)
        addQuoteText.configure(height=500, width=800)
        addQuoteText.pack(side="top")
        Avatar = tk.Label(addFrame)
        img_avatar = tk.PhotoImage(file=localPath+"/photos/anonymous.png")
        Avatar.configure(
            height=200,
            image=img_avatar,
            text='label2',
            width=200)
        Avatar.grid(column=0, row=0, sticky="nw")
        global nomAuteur
        nomAuteur = tk.Entry(addFrame)
        nomAuteur.grid(column=0, pady=182, row=0, sticky="nw")
        global descAuteur
        descAuteur = tk.Text(addFrame)
        descAuteur.configure(height=10, width=23)
        descAuteur.grid(
            column=0,
            pady=220,
            row=0,
            rowspan=100,
            sticky="nw")
        labelDesc = tk.Label(addFrame)
        labelDesc.configure(text="Description de l'auteur")
        labelDesc.grid(column=0, pady=205, row=0, sticky="nw")
        global source
        source = tk.Text(addFrame)
        source.configure(height=10, width=23)
        source.grid(column=0, pady=390, row=0, rowspan=100, sticky="nw")
        labelSource = tk.Label(addFrame)
        labelSource.configure(text='Source')
        labelSource.grid(
            column=0,
            pady=380,
            row=0,
            rowspan=1000,
            sticky="nw")
        Confirmer = tk.Button(addFrame)
        Confirmer.configure(text='Confirmer', width=20, command=lambda:change('add'))
        Confirmer.grid(column=1, padx=5, row=1, sticky="w")
        Annuler = tk.Button(addFrame)
        Annuler.configure(text='Annuler', width=20, command=reloadBottomFrame)
        Annuler.grid(column=1, padx=200, row=1, sticky="w")
        addFrame.grid(column=0, row=2)
        addFrame.grid_propagate(0)
        addFrame.rowconfigure(2, uniform=1)

def edit():
    print("Hello, world!")

def delete():
    print("Hello, world!")

def importcsv():
    bottomFrame.forget()
    importFrame = tk.Frame(root)
    importFrame.pack()
    importButton = tk.Button(importFrame, text="Importer un fichier CSV")
    importButton.pack(pady=200)

def export():
    filetype = (('text files', 'csv'), ('All files', '*.*'))

def copy():
    print("Hello, world!")

def change(action):
    if action == "add":
        getChangeQuoteText = addQuoteText.get()
        getChangeAuteurText = nomAuteur.get()
        getChangeDescText = descAuteur.get()
        getChangeSourceText = source.get()

        query="""SELECT Auteur FROM Auteurs WHERE Auteur='%s';""" % getChangeAuteurText
        cursor.execute(query)
        auteurInDb = cursor.fetchall()[0][0]

        if auteurInDb.len() < 1:
            query="""INSERT INTO Auteurs (Auteur, Desc) VALUES ('%s', '%s')""" % getChangeAuteurText, getChangeDescText
            cursor.execute(query)

            query="""SELECT AuteurID FROM Auteurs WHERE Auteur='%s' """ % getChangeAuteurText
            cursor.fetchall()[0][0]
            idAuteur = int(cursor.fetchall()[0][0])
            query="""INSERT INTO Citations (AuteurID, Citation_en, Source) VALUES ('%i', '%s', 's')""" % idAuteur, getChangeQuoteText, getChangeSourceText
            cursor.execute(query)
        else:
            query="""SELECT AuteurID FROM Auteurs WHERE Auteur=%s""" % getChangeAuteurText
            cursor.fetchall()[0][0]
            idAuteur = int(cursor.fetchall()[0][0])
            query="""INSERT INTO Citations (AuteurID, Citation_en, Source) VALUES ('%i', '%s', 's')""" % idAuteur, getChangeQuoteText, getChangeSourceText
            cursor.execute(query)


def changeQuote(action):
    global photo
    global lastQuote
    global img_avatar
    global quoteId
    global lang
    global quoteNumber
    global sessionCount
    sessionCount = 1
    langValue = lang.get()
    cursor.execute("SELECT COUNT(*) FROM Citations")
    size = cursor.fetchall()[0][0]
    if action == "last":
        quoteId = quoteId - 1
    elif action == "next":
        quoteId = quoteId + 1
    elif action == "previous":
        sessionCount =+ 2
        quoteId = lastQuote[-sessionCount]
    elif action == "random":
        randomQuoteId = random.randint(0, size)
        quoteId = randomQuoteId
    else:
        langValue = action
    queryEn="""SELECT Citation_en FROM Citations WHERE rowid='%i';""" % quoteId
    cursor.execute(queryEn)
    quoteTextEn = cursor.fetchall()[0][0]
    lastQuote.append(quoteId)
    if langValue == "en":
        quoteNumber.set(f"{quoteId}/{size}")
        #cursor.execute(f"SELECT Citation_en, rowid FROM Citations WHERE rowid={quoteId}")
        #print(quoteText)
        quote.set(quoteTextEn)
    elif langValue == "fr":
        quoteNumber.set(f"{quoteId}/{size}")
        #cursor.execute(f"SELECT Citation_en, rowid FROM Citations WHERE rowid={quoteId}")
        queryFr="""SELECT Citation_fr FROM Citations WHERE rowid='%i';""" % quoteId
        cursor.execute(queryFr)
        quoteText = cursor.fetchall()[0][0]
        if len(quoteText) <= 2:
            quoteFrancais = GoogleTranslator(source='auto', target='fr').translate(quoteTextEn) + "\n[Traduction automatique]"
            quoteText = quoteFrancais
        #print(quoteText)
        quote.set(quoteText)

    query="""SELECT AuteurID FROM Citations WHERE rowid='%i';""" % quoteId
    cursor.execute(query)
    auteurId = cursor.fetchall()[0][0]

    query="""SELECT Desc FROM Auteurs WHERE AuteurID='%i';""" % auteurId
    cursor.execute(query)
    desc = cursor.fetchall()[0][0]
    auteurInfo.set(desc)

    query="""SELECT Auteur FROM Auteurs WHERE AuteurID='%i';""" % auteurId
    cursor.execute(query)
    quoteAuteur = cursor.fetchall()[0][0]
    auteur.set(quoteAuteur)

    findSource="""SELECT Source FROM Citations WHERE rowid='%i';""" % quoteId
    cursor.execute(findSource)
    souse = cursor.fetchall()[0][0]
    source.set(souse)

    auteurSansEspaces = quoteAuteur
    auteurSansEspaces = auteurSansEspaces.replace(" ","")
    auteurSansEspaces = auteurSansEspaces.replace("-","")
    auteurSansEspaces = auteurSansEspaces.replace("'","")
    auteurSansEspaces = auteurSansEspaces.replace(".","")
    """
    pngPath = Path(localPath+"photos/"+auteurSansEspaces+".png")
    jpgPath = Path(localPath+"photos/"+auteurSansEspaces+".jpg")
    pngFile = localPath+"photos/"+auteurSansEspaces+".png"
    jpgFile = localPath+"photos/"+auteurSansEspaces+".jpg"
    if pngPath.is_file():
        img_avatar = Image.open(pngFile)
        photo = img_avatar.resize((200,200))
        photo = ImageTk.PhotoImage(photo)
        Avatar.config(image=photo)

    elif jpgPath.is_file():
        jpg = ImageTk.PhotoImage(Image.open(jpgFile, "r"))
        Avatar.configure(image=jpg)

    else:
        pathAvatar = Path(localPath+"photos/avatar.png")
        Avatar.configure(image=pathAvatar)
    """
    chemin = localPath+"photos/"
    filelist = [file for file in os.listdir(chemin) if file.startswith(auteurSansEspaces) and file.endswith(('.png', '.PNG', '.GIF', '.gif', '.jpg', '.JPG', '.jpeg', '.JPEG'))]
    if len(filelist)> 0:
        imgAuthor= Image.open(chemin+filelist[0])
    else:
        imgAuthor= Image.open(chemin+"anonymous.png")
    photo = imgAuthor.resize((200,200))
    photo = ImageTk.PhotoImage(photo)
    Avatar.config(image=photo)

def reloadBottomFrame():
    bottomFrame = tk.Frame(root)
    bottomFrame.configure(height=570, width=1040)
    labelframe5 = tk.LabelFrame(bottomFrame)
    labelframe5.configure(
        background="white",
        borderwidth=5,
        height=500,
        text='Citation\n',
        width=800)
    QuoteLabel = tk.Label(labelframe5)
    quote = tk.StringVar()
    QuoteLabel.configure(
        background="#ffffff",
        font="{Times New Roman} 16 {italic}",
        textvariable=quote,
        wraplength=600)
    QuoteLabel.pack(
        anchor="center",
        fill="both",
        pady=100,
        side="top")
    labelframe5.grid(column=1, row=0)
    labelframe5.pack_propagate(0)
    Avatar = tk.Label(bottomFrame,height=200,image=img_avatar,width=200)
    Avatar.grid(column=0, row=0, sticky="nw")
    AuteurLabel = tk.Label(bottomFrame)
    auteur = tk.StringVar()
    AuteurLabel.configure(
        font="{Times New Roman} 11 {}",
        relief="ridge",
        textvariable=auteur)
    AuteurLabel.grid(column=0, pady=183, row=0, sticky="nw")
    AuteurInfoLabel = tk.Label(bottomFrame)
    auteurInfo = tk.StringVar()
    AuteurInfoLabel.configure(
        justify="left",
        textvariable=auteurInfo,
        wraplength=200)
    AuteurInfoLabel.grid(pady=210, row=0, rowspan=10, sticky="nw")

    SourceLabel = tk.Label(bottomFrame)
    source = tk.StringVar()
    SourceLabel.configure(
        justify="left",
        textvariable=source,
        wraplength=200)
    SourceLabel.grid(pady=350, row=0, rowspan=100, sticky="w")
    bottomFrame.grid(column=0, row=2)
    bottomFrame.grid_propagate(0)
    changeQuote('random')


root = tk.Tk()
root.configure(height=720, width=1080)
root.resizable(False, False)
root.title("QuotesApp")
topFrame = tk.Frame(root)
topFrame.configure(height=85, width=1060)

lang = tk.StringVar()
lang.set('en')
img_avatar = tk.PhotoImage()

translateEn = tk.Radiobutton(topFrame, text='English', variable=lang, value='en', command=lambda:changeQuote('en'))
translateEn.grid(column=0, row=1, sticky="w")

translateFr = tk.Radiobutton(topFrame, text='Français', variable=lang, value='fr', command=lambda:changeQuote('fr'))
translateFr.grid(column=0, row=0, sticky="w")

labelKeywords = tk.Label(topFrame, text='Mot-Clés')
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
middleFrame = tk.Frame(root)
middleFrame.configure(height=30, width=1040)

ajouterButtonIcon = tk.PhotoImage(file="icons\plus.png")
ajouterButton = tk.Button(middleFrame, image=ajouterButtonIcon, height=20, width=20, relief="flat")
ajouterButton.configure(command=lambda:add(''))
ajouterButton.grid(column=0, row=0)

modifierButtonIcon = tk.PhotoImage(file="icons\edit.png")
modifierButton = tk.Button(middleFrame, image=modifierButtonIcon, height=20, width=20, relief="flat")
modifierButton.configure(command=edit)
modifierButton.grid(column=1, row=0)

deleteButton = tk.Button(middleFrame)
deleteButtonIcon = tk.PhotoImage(file="icons\delete.png")
deleteButton = tk.Button(middleFrame, image=deleteButtonIcon, height=20, width=20, relief="flat")
deleteButton.configure(command=delete)
deleteButton.grid(column=2, row=0)

importButton = tk.Button(middleFrame)
importButtonIcon = tk.PhotoImage(file="icons\input.png")
importButton = tk.Button(middleFrame, image=importButtonIcon, height=20, width=20, relief="flat")
importButton.configure(command=importcsv)
importButton.grid(column=3, row=0)

exportButton = tk.Button(middleFrame)
exportButtonIcon = tk.PhotoImage(file="icons\output.png")
exportButton = tk.Button(middleFrame, image=exportButtonIcon, height=20, width=20, relief="flat")
exportButton.configure(command=export)
exportButton.grid(column=4, row=0)

copyButton = tk.Button(middleFrame)
copyButtonIcon = tk.PhotoImage(file="icons\clipboard-copy.png")
copyButton = tk.Button(middleFrame, image=copyButtonIcon, height=20, width=20, relief="flat")
copyButton.config(command=copy)
copyButton.grid(column=5, row=0)

precedantButton = tk.Button(middleFrame, text='Précédent',width=20, command=lambda: changeQuote("last"))
precedantButton.grid(column=6, padx=70, row=0)

derniereButton = tk.Button(middleFrame, text='Dernière',width=10, command=lambda: changeQuote("previous"))
derniereButton.grid(column=7, row=0)

randomButton = tk.Button(middleFrame,text='Aléatoire', width=10, command=lambda: changeQuote("random"))
randomButton.grid(column=8, row=0)

suivantButton = tk.Button(middleFrame,text='Suivant', width=20, command=lambda: changeQuote("next"))
suivantButton.grid(column=9, padx=70, row=0)

quoteNumber = tk.StringVar()
quoteIdLabel = tk.Label(middleFrame,textvariable=quoteNumber)
quoteIdLabel.grid(column=10, row=0)



middleFrame.grid(column=0, pady=10, row=1)
middleFrame.grid_propagate(0)
bottomFrame = tk.Frame(root)
bottomFrame.configure(height=570, width=1040)
labelframe5 = tk.LabelFrame(bottomFrame)
labelframe5.configure(
    background="white",
    borderwidth=5,
    height=500,
    text='Citation\n',
    width=800)
QuoteLabel = tk.Label(labelframe5)
quote = tk.StringVar()
QuoteLabel.configure(
    background="#ffffff",
    font="{Times New Roman} 16 {italic}",
    textvariable=quote,
    wraplength=600)
QuoteLabel.pack(
    anchor="center",
    fill="both",
    pady=100,
    side="top")
labelframe5.grid(column=1, row=0)
labelframe5.pack_propagate(0)
Avatar = tk.Label(bottomFrame,height=200,image=img_avatar,width=200)
Avatar.grid(column=0, row=0, sticky="nw")
AuteurLabel = tk.Label(bottomFrame)
auteur = tk.StringVar()
AuteurLabel.configure(
    font="{Times New Roman} 11 {}",
    relief="ridge",
    textvariable=auteur)
AuteurLabel.grid(column=0, pady=183, row=0, sticky="nw")
AuteurInfoLabel = tk.Label(bottomFrame)
auteurInfo = tk.StringVar()
AuteurInfoLabel.configure(
    justify="left",
    textvariable=auteurInfo,
    wraplength=200)
AuteurInfoLabel.grid(pady=210, row=0, rowspan=10, sticky="nw")

SourceLabel = tk.Label(bottomFrame)
source = tk.StringVar()
SourceLabel.configure(
    justify="left",
    textvariable=source,
    wraplength=200)
SourceLabel.grid(pady=350, row=0, rowspan=100, sticky="w")
bottomFrame.grid(column=0, row=2)
bottomFrame.grid_propagate(0)
root.grid_propagate(0)
root.rowconfigure(2, uniform=1)

changeQuote("random")

root.mainloop()
con.close()