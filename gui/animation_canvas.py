import customtkinter as ctk


class AnimationCanvas(ctk.CTkCanvas):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.config(bg="white")  # Set background color for visibility

        # Placeholder for future drawing methods
