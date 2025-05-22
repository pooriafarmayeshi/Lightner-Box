import tkinter as tk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1000x600")
        self.root.title("Litner Box")
        self.center_window()
        self.initialize_ui()
    
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

if __name__ == "__main__":
    app = App()
    app.run()
