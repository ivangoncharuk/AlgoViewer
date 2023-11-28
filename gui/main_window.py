import random, sys, threading, time
import customtkinter as ctk

sys.path.append(".")

from algorithms import sorting_algorithms
from gui.animation_canvas import AnimationCanvas
import gui.sidebar_controls as sidebar_controls


class MainWindow(ctk.CTk):
    """
    Main window class for the Algorithm Visualizer application.
    """

    TITLE = "Algorithm Visualizer"
    WINDOW_SIZE = "1024x768"
    INITIAL_DATA_RANGE = (1, 100)
    INITIAL_DATA_COUNT = 50

    def __init__(self):
        super().__init__()
        self.title(self.TITLE)
        self.geometry(self.WINDOW_SIZE)

        self.setup_sidebar()
        self.setup_main_frame()

        self.initial_data = [
            random.randint(*self.INITIAL_DATA_RANGE)
            for _ in range(self.INITIAL_DATA_COUNT)
        ]
        self.current_data = self.initial_data[:]  # Current state of data
        self.display_initial_bars()

        self.sorting_index = 0  # Initialize sorting index
        self.is_visualizing = False  # Track the state of visualization
        self.sorting_completed = False  # Tracking the state of sortedness

    def setup_sidebar(self):
        """
        Set up the sidebar containing controls and widgets.
        """
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.pack(side="left", fill="y", padx=10, pady=10)
        self.setup_controls()

    def setup_controls(self):
        sidebar_controls.setup_play_pause_button(self)
        # sidebar_controls.setup_reset_button(self)
        sidebar_controls.setup_clear_canvas_button(self)
        sidebar_controls.setup_load_random_data_button(self)
        sidebar_controls.setup_algorithm_combo(self)
        sidebar_controls.setup_num_bars_slider(self)
        sidebar_controls.setup_speed_slider(self)

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
            sidebar_controls.enable_controls(self, True)
        else:
            if self.sorting_completed:
                self.randomize_canvas()  # Reset to new random data
                self.sorting_completed = False
            self.start_visualization()
            self.play_pause_button.configure(text="Pause")
            sidebar_controls.enable_controls(self, False)
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
            time.sleep(0.5 / speed)

        if not self.stop_visualization:
            self.animation_canvas.color_bars_complete()
            sidebar_controls.enable_controls(self, True)
            self.play_pause_button.configure(text="Play")
            self.sorting_completed = True
            self.is_visualizing = False
        else:
            self.play_pause_button.configure(text="Play")
            self.is_visualizing = False



if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
