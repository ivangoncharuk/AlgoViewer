import customtkinter as ctk


class AnimationCanvas(ctk.CTkCanvas):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.config(bg="white")
        self.rectangles = []  # Store references to rectangle objects

    def create_initial_bars(self, data, max_value):
        self.delete("all")  # Clear the canvas
        self.rectangles = []
        c_width = self.winfo_width()
        c_height = self.winfo_height()
        bar_width = c_width / len(data)

        for i, val in enumerate(data):
            x1, y1, x2, y2 = self.calculate_bar_dimensions(
                i, val, len(data), c_width, c_height, max_value
            )
            rect = self.create_rectangle(x1, y1, x2, y2, fill="blue")
            self.rectangles.append(rect)

    def update_bars(self, data, max_value):
        c_width = self.winfo_width()
        c_height = self.winfo_height()

        for i, val in enumerate(data):
            x1, y1, x2, y2 = self.calculate_bar_dimensions(
                i, val, len(data), c_width, c_height, max_value
            )
            self.coords(self.rectangles[i], x1, y1, x2, y2)

    def calculate_bar_dimensions(
        self, index, value, data_length, canvas_width, canvas_height, max_value
    ):
        bar_width = canvas_width / data_length
        x1 = index * bar_width
        y1 = canvas_height - (value / max_value) * canvas_height  # Use max_value here
        x2 = (index + 1) * bar_width
        y2 = canvas_height
        return x1, y1, x2, y2

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
