
#définition du Widget: (longeur et largeur sont en caractères, et non en pixels)
EditQuote=Tk.Text(labelframe5, height = 4, width = 40, font=("Cambria",15,"italic"))
#lire le contenu:
citation = EditQuote.get(1.0, "end-1c") # ligne 1 ,caractère zero jusqu'à end
#reset content
EditQuote.delete(1.0,'end-1c') 
#insérer du contenu
EditQuote.insert("1.0",varQuote.get())

sql_select_query = """select * from SqliteDb_developers where id = ?"""
cursor.execute(sql_select_query, (id,))
records = cursor.fetchall()

