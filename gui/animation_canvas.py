import customtkinter as ctk


class AnimationCanvas(ctk.CTkCanvas):
    """
    Custom Tkinter canvas for visualizing sorting algorithms.
    """

    def __init__(self, parent, **kwargs):
        """
        Initialize the AnimationCanvas.

        Args:
            parent: The parent widget.
            **kwargs: Additional keyword arguments for the canvas.
        """
        super().__init__(parent, **kwargs)
        self.config(bg="white")
        self.rectangles = []

    def create_initial_bars(self, data, max_value):
        """
        Create initial bars on the canvas based on input data.

        Args:
            data (list): List of data values to visualize.
            max_value (int): Maximum value in the data for scaling.
        """
        self.clear_canvas()
        self.rectangles = self.generate_bars(data, max_value)

    def clear_canvas(self):
        """
        Clear the canvas by deleting all items on it.
        """
        self.delete("all")

    def generate_bars(self, data, max_value):
        """
        Generate bar rectangles on the canvas based on input data.

        Args:
            data (list): List of data values to visualize.
            max_value (int): Maximum value in the data for scaling.

        Returns:
            list: List of generated bar rectangles on the canvas.
        """
        rectangles = []
        c_width, c_height = self.winfo_width(), self.winfo_height()
        for i, val in enumerate(data):
            rect = self.create_rectangle(
                *self.calculate_bar_dimensions(
                    i, val, len(data), c_width, c_height, max_value
                ),
                fill="blue"
            )
            rectangles.append(rect)
        return rectangles

    def update_bars(self, data, max_value):
        """
        Update the positions of existing bar rectangles on the canvas based on new data.

        Args:
            data (list): List of data values to update the bars.
            max_value (int): Maximum value in the data for scaling.
        """
        c_width, c_height = self.winfo_width(), self.winfo_height()
        for i, val in enumerate(data):
            self.coords(
                self.rectangles[i],
                *self.calculate_bar_dimensions(
                    i, val, len(data), c_width, c_height, max_value
                )
            )

    def calculate_bar_dimensions(
        self, index, value, data_length, canvas_width, canvas_height, max_value
    ):
        """
        Calculate the dimensions of a bar rectangle.

        Args:
            index (int): Index of the bar in the data.
            value (int): Value of the bar.
            data_length (int): Total number of data elements.
            canvas_width (int): Width of the canvas.
            canvas_height (int): Height of the canvas.
            max_value (int): Maximum value in the data for scaling.

        Returns:
            tuple: A tuple containing (x1, y1, x2, y2) coordinates of the bar.
        """
        bar_width = canvas_width / data_length
        x1 = index * bar_width
        y1 = canvas_height - (value / max_value) * canvas_height  # Use max_value here
        x2 = (index + 1) * bar_width
        y2 = canvas_height
        return x1, y1, x2, y2

    def visualize_sorting(self, data):
        """
        Visualize sorting by drawing bar rectangles on the canvas based on input data.

        Args:
            data (list): List of data values to visualize.
        """
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
