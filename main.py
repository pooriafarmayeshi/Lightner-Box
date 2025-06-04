import tkinter as tk
import sqlite3

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


#-----------------Graphic-----------------
class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1000x600")
        self.root.title("Lightner Box")

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.initialize_ui()
        self.center_window()

        self.db = DataBase()
    
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
        # Initialize UI components
        self.button = tk.Button(self.root, text="Click Me", command=self.function1, width=15, height=2)
        self.button.pack(pady=20)
    
    def function1(self):
        # Simple function that shows a message when button is clicked
        print("Button clicked!")
        self.addCard()

    def addCard(self):
        self.db.addValue(("Hello","سلام","1404-03-07"))
        # self.db.close()
    
    def run(self):
        # Runs the mainloop
        self.root.mainloop()

    def on_close(self):
        self.db.close()
        self.root.destroy()


if __name__ == "__main__":
    App().run()
