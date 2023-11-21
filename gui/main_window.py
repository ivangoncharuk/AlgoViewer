import customtkinter as ctk


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Algorithm Visualizer")
        self.geometry("800x600")
