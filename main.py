import tkinter as tk
import sqlite3


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1000x600")
        self.root.title("Litner Box")
        self.center_window()
        self.initialize_ui()

        DataBase()
    
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
        pass
    
    def run(self):
        # Run the mainloop
        self.root.mainloop()

# The DataBase Class
class DataBase():
    def __init__(self):
        self.connection()
    
    def connection(self):
        conn = sqlite3.connect('mainDataBase.db')
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT,
            salary REAL)''')
        
if __name__ == "__main__":
    App().run()
