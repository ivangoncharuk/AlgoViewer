import random
import sys
import threading
import time
import customtkinter as ctk

sys.path.append(".")

from algorithms import sorting_algorithms
from gui.animation_canvas import AnimationCanvas


class MainWindow(ctk.CTk):
    """
    Main window class for the Algorithm Visualizer application.
    """

    def __init__(self):
        super().__init__()
        self.title("Algorithm Visualizer")
        self.geometry("1024x768")

        self.setup_sidebar()
        self.setup_main_frame()

        self.is_visualizing = False  # Track the state of visualization

    def setup_sidebar(self):
        """
        Set up the sidebar containing controls and widgets.
        """
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.pack(side="left", fill="y", padx=10, pady=10)
        self.setup_controls()

    def setup_main_frame(self):
        """
        Set up the main frame for the animation canvas.
        """
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Initialize and pack the animation canvas
        self.animation_canvas = AnimationCanvas(self.main_frame, width=600, height=400)
        self.animation_canvas.pack(pady=10)

    def setup_controls(self):
        """
        Set up the GUI controls in the sidebar.
        """

        # Play/Pause button
        self.play_pause_button = ctk.CTkButton(
            self.sidebar, text="Play", command=self.toggle_visualization
        )
        self.play_pause_button.pack(pady=10)

        # Clear button
        self.clear_button = ctk.CTkButton(
            self.sidebar, text="Clear", command=self.clear_canvas
        )
        self.clear_button.pack(pady=10)

        # Dropdown menu for algorithm selection
        self.algorithm_combo = ctk.CTkComboBox(
            self.sidebar,
            values=["Bubble Sort", "Quick Sort"],
        )
        self.algorithm_combo.pack(pady=10)
        self.algorithm_combo.bind("<<ComboboxSelected>>", self.on_algorithm_change)

        # Slider for speed control
        self.speed_label = ctk.CTkLabel(self.sidebar, text="Visualization Speed")
        self.speed_label.pack(pady=(10, 0))

        self.speed_slider = ctk.CTkSlider(self.sidebar, from_=1, to=10)
        self.speed_slider.pack(pady=10)

    def on_algorithm_change(self, event=None):
        self.clear_canvas()

    def toggle_visualization(self):
        if self.is_visualizing:
            self.stop_visualization = True
            self.play_pause_button.configure(text="Play")
        else:
            self.start_visualization()
            self.play_pause_button.configure(text="Pause")
        self.is_visualizing = not self.is_visualizing

    def start_visualization(self):
        """
        Start the visualization process when the "Start" button is clicked.
        """
        self.ensure_single_thread()
        self.visualization_thread = threading.Thread(
            target=self.run_visualization, daemon=True
        )
        self.visualization_thread.start()

    def clear_canvas(self):
        if self.is_visualizing:
            self.stop_visualization = True
            self.visualization_thread.join()
            self.is_visualizing = False
            self.play_pause_button.configure(text="Play")
        self.animation_canvas.clear_canvas()

    def ensure_single_thread(self):
        """
        Ensure that only one visualization thread is active at a time.
        """
        if (
            hasattr(self, "visualization_thread")
            and self.visualization_thread.is_alive()
        ):
            self.stop_visualization = True
            self.visualization_thread.join()
        self.stop_visualization = False

    def run_visualization(self):
        """
        Run the selected algorithm visualization based on user input.
        """
        algorithm = self.algorithm_combo.get()
        speed = self.speed_slider.get()

        if algorithm == "Bubble Sort":
            self.visualize_bubble_sort(speed)

    def visualize_bubble_sort(self, speed):
        """
        Visualize the Bubble Sort algorithm.

        Args:
            speed (int): The visualization speed control value.
        """
        data = [random.randint(1, 100) for _ in range(50)]
        max_value = max(data)
        self.animation_canvas.create_initial_bars(data, max_value)

        for step in sorting_algorithms.bubble_sort(data):
            if self.stop_visualization:
                break
            self.animation_canvas.update_bars(step, max_value)
            self.update_idletasks()
            time.sleep(0.25 / speed)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
