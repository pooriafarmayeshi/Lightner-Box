import tkinter as tk
import sqlite3
from datetime import date

#-----------------Logic-----------------
class DataBase():
    def __init__(self):
        self.conn = sqlite3.connect("mainDataBase.db")
        self.cursor = self.conn.cursor()
        self.createTable()

    def createTable(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS box (
            id INTEGER PRIMARY KEY,
            front TEXT,
            back TEXT,
            date TEXT           
            )''')
        self.conn.commit()
        
    def addValue(self, dataTuple):
        addingQuery = "INSERT INTO box (front, back, date) VALUES (?, ?, ?)"
        self.cursor.execute(addingQuery, dataTuple)
        self.conn.commit()
    
    def close(self):
        self.cursor.close()
        self.conn.close()

class Functions:
    def __init__(self, app):
        self.app = app
        self.db = app.db

    def getCards(self):
        # Grab data from the two entry fields and insert into DB
        front_text = self.app.front_entry.get()
        back_text = self.app.back_entry.get()

        if front_text and back_text:
            today = date.today().isoformat()
            return (front_text, back_text, today)
        return None
    
    def clearTextBoxes(self):
        # Clear the entries after adding
        self.app.front_entry.delete(0, tk.END)
        self.app.back_entry.delete(0, tk.END)

    def addCard(self, value):
        #add a new card to dataBase.
        if value:
            self.db.addValue(value)
            self.clearTextBoxes()

#-----------------Graphic-----------------
class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1000x600")
        self.root.title("Lightner Box")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.db = DataBase()
        self.initialize_ui()
        self.center_window()
        self.funcs = Functions(self)
        self.front_back_toggle = True

    def center_window(self):
        # Opens the root at center
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2) - 40
        self.root.geometry(f"+{x}+{y}")
    
    def initialize_ui(self):
        # Entry for Front
        self.front_label = tk.Label(self.root, text="Front:")
        self.front_label.pack()
        self.front_entry = tk.Entry(self.root, width=50)
        self.front_entry.pack(pady=5)

        # Entry for Back
        self.back_label = tk.Label(self.root, text="Back:")
        self.back_label.pack()
        self.back_entry = tk.Entry(self.root, width=50)
        self.back_entry.pack(pady=5)

        # Submit Button
        self.submit_button = tk.Button(self.root, text="Add Card", command=self.submit_button_func, width=15, height=2)
        self.submit_button.pack(pady=20)

        # Card Button
        self.card_button = tk.Button(self.root, text="Card", command=self.card_button_func, width=60, height=10, background="#edc453")
        self.card_button.pack(pady=20)
    
    def submit_button_func(self):
        card_data = self.funcs.getCards()
        self.funcs.addCard(card_data)

    def card_button_func(self):
        if self.front_back_toggle:
            self.card_button.config(text = "x")
            self.front_back_toggle = not self.front_back_toggle
        else :
            self.card_button.config(text = "y")
            self.front_back_toggle = not self.front_back_toggle


    def run(self):
        self.root.mainloop()

    def on_close(self):
        self.db.close()
        self.root.destroy()

if __name__ == "__main__":
    App().run()
