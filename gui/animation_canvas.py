import customtkinter as ctk


class AnimationCanvas(ctk.CTkCanvas):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.config(bg="white")  # Set background color for visibility

    def visualize_sorting(self, data):
        self.delete("all")  # Clear the canvas
        c_width = self.winfo_width()
        c_height = self.winfo_height()
        bar_width = c_width / len(data)

        for i, val in enumerate(data):
            # Calculate position and size of each bar
            x1 = i * bar_width
            y1 = c_height - (val / max(data)) * c_height
            x2 = (i + 1) * bar_width
            y2 = c_height

            self.create_rectangle(x1, y1, x2, y2, fill="blue")  # Draw the bar
