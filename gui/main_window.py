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

        self.initial_data = [random.randint(1, 100) for _ in range(50)]  # Initial data
        self.current_data = self.initial_data[:]  # Current state of data
        self.display_initial_bars()

        self.sorting_index = 0  # Initialize sorting index
        self.is_visualizing = False  # Track the state of visualization

    def setup_sidebar(self):
        """
        Set up the sidebar containing controls and widgets.
        """
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.pack(side="left", fill="y", padx=10, pady=10)
        self.setup_controls()

    def setup_controls(self):
        self.setup_play_pause_button()
        self.setup_reset_button()
        self.setup_clear_canvas_button()
        self.setup_load_random_data_button()
        self.setup_algorithm_combo()
        self.setup_num_bars_slider()
        self.setup_speed_slider()

    def setup_play_pause_button(self):
        self.play_pause_button = ctk.CTkButton(
            self.sidebar, text="Play", command=self.toggle_visualization
        )
        self.play_pause_button.pack(pady=10)

    def setup_reset_button(self):
        self.reset_button = ctk.CTkButton(
            self.sidebar, text="Reset", command=self.reset_visualization
        )
        self.reset_button.pack(pady=10)

    def setup_clear_canvas_button(self):
        self.clear_canvas_button = ctk.CTkButton(
            self.sidebar, text="Clear Canvas", command=self.clear_only_canvas
        )
        self.clear_canvas_button.pack(pady=10)

    def setup_load_random_data_button(self):
        self.load_random_data_button = ctk.CTkButton(
            self.sidebar, text="Load Random Data", command=self.randomize_canvas
        )
        self.load_random_data_button.pack(pady=10)

    def setup_algorithm_combo(self):
        self.algorithm_combo = ctk.CTkComboBox(
            self.sidebar, values=["Bubble Sort", "Quick Sort"]
        )
        self.algorithm_combo.pack(pady=10)
        self.algorithm_combo.bind("<<ComboboxSelected>>", self.on_algorithm_change)

    def setup_num_bars_slider(self):
        self.num_bars_label = ctk.CTkLabel(self.sidebar, text="Number of Bars: 50")
        self.num_bars_label.pack(pady=(10, 0))
        self.number_of_bars_slider = ctk.CTkSlider(
            self.sidebar, from_=10, to=100, command=self.update_num_bars_label
        )
        self.number_of_bars_slider.set(50)
        self.number_of_bars_slider.pack(pady=10)

    def setup_speed_slider(self):
        self.speed_label = ctk.CTkLabel(self.sidebar, text="Visualization Speed: 1")
        self.speed_label.pack(pady=(10, 0))
        self.speed_slider = ctk.CTkSlider(
            self.sidebar, from_=1, to=10, command=self.update_speed_label
        )
        self.speed_slider.set(1)
        self.speed_slider.pack(pady=10)

    def setup_main_frame(self):
        """
        Set up the main frame for the animation canvas.
        """
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Initialize and pack the animation canvas
        self.animation_canvas = AnimationCanvas(self.main_frame, width=750, height=400)
        self.animation_canvas.pack(pady=10)

    def update_num_bars_label(self, value):
        self.num_bars_label.configure(text=f"Number of Bars: {int(value)}")
        self.number_of_bars = int(value)

    def update_speed_label(self, value):
        self.speed_label.configure(text=f"Visualization Speed: {int(value)}")

    def on_algorithm_change(self, event=None):
        self.randomize_canvas()

    def display_initial_bars(self):
        max_value = max(self.current_data)
        self.animation_canvas.create_initial_bars(self.current_data, max_value)

    def toggle_visualization(self):
        if self.is_visualizing:
            self.stop_visualization = True
            self.play_pause_button.configure(text="Play")
            (
                self.current_data,
                _,
                self.sorting_index,
            ) = self.animation_canvas.get_current_data()
            self.enable_controls(True)  # Enable controls after pausing
        else:
            self.start_visualization()
            self.play_pause_button.configure(text="Pause")
            self.enable_controls(False)  # Disable controls during visualization
        self.is_visualizing = not self.is_visualizing

    def enable_controls(self, enable):
        """
        Enable or disable control buttons.
        """
        self.reset_button.configure(state=ctk.NORMAL if enable else ctk.DISABLED)
        self.load_random_data_button.configure(
            state=ctk.NORMAL if enable else ctk.DISABLED
        )
        self.algorithm_combo.configure(state=ctk.NORMAL if enable else ctk.DISABLED)
        self.clear_canvas_button.configure(state=ctk.NORMAL if enable else ctk.DISABLED)

    def start_visualization(self):
        """
        Start the visualization process when the "Start" button is clicked.
        """
        self.ensure_single_thread()
        self.visualization_thread = threading.Thread(
            target=self.run_visualization, daemon=True
        )
        self.visualization_thread.start()

    def update_canvas(self, data):
        self.current_data = data
        self.sorting_index = 0
        max_value = max(self.current_data)
        self.animation_canvas.create_initial_bars(self.current_data, max_value)

    def stop_visualization_and_reset(self):
        self.stop_visualization = True
        self.visualization_thread.join()
        self.is_visualizing = False
        self.play_pause_button.configure(text="Play")

    def reset_visualization(self):
        if self.is_visualizing:
            self.stop_visualization_and_reset()

        # Reset to initial data using update_canvas
        self.update_canvas(self.initial_data[:])

    def randomize_canvas(self):
        self.number_of_bars = int(self.number_of_bars_slider.get())

        if self.is_visualizing:
            self.stop_visualization_and_reset()

        # Generate a new random dataset based on the number of bars
        new_data = [random.randint(1, 100) for _ in range(self.number_of_bars)]

        # Use the update_canvas method to update the canvas
        self.update_canvas(new_data)

    def clear_only_canvas(self):
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

        self.animation_canvas.set_current_data(
            self.current_data
        )  # Set data before starting

        if algorithm == "Bubble Sort":
            self.visualize_bubble_sort(speed)

    def visualize_bubble_sort(self, speed):
        """
        Visualize the Bubble Sort algorithm.

        Args:
            speed (int): The visualization speed control value.
        """
        data = self.current_data
        max_value = max(data)
        self.animation_canvas.create_initial_bars(data, max_value)

        for step, comparison_indices, i in sorting_algorithms.bubble_sort(
            data, self.sorting_index
        ):
            if self.stop_visualization:
                self.sorting_index = i  # Save the current sorting index
                break
            self.animation_canvas.update_bars(step, comparison_indices, max_value)
            self.update_idletasks()
            time.sleep(0.002 / speed)

        if not self.stop_visualization:
            self.animation_canvas.color_bars_complete()
            self.enable_controls(True)
            self.play_pause_button.configure(text="Play")


# for step, comparison_indices, i in sorting_algorithms.bubble_sort(self.current_data, self.sorting_index):

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
