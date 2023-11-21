import customtkinter as ctk


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Algorithm Visualizer")
        self.geometry("1024x768")

        self.setup_sidebar()
        self.setup_main_frame()

    def setup_sidebar(self):
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.pack(side="left", fill="y", padx=10, pady=10)
        self.setup_controls()

    def setup_controls(self):
        # Start button
        self.start_button = ctk.CTkButton(
            self.sidebar, text="Start", command=self.start_visualization
        )
        self.start_button.pack(pady=10)

        # Dropdown menu for algorithm selection
        self.algorithm_label = ctk.CTkLabel(self.sidebar, text="Select Algorithm")
        self.algorithm_label.pack(pady=(10, 0))
        self.algorithm_combo = ctk.CTkComboBox(
            self.sidebar,
            values=["Bubble Sort", "Quick Sort"],
        )
        self.algorithm_combo.pack(pady=10)

        # Slider for speed control
        self.speed_label = ctk.CTkLabel(self.sidebar, text="Visualization Speed")
        self.speed_label.pack(pady=(10, 0))
        
        self.speed_slider = ctk.CTkSlider(self.sidebar, from_=1, to=10)
        self.speed_slider.pack(pady=10)

    def setup_main_frame(self):
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)
        # Placeholder for animation canvas

    def start_visualization(self):
        selected_algorithm = self.algorithm_combo.get()
        speed = self.speed_slider.get()
        print(f"Starting {selected_algorithm} visualization at speed {speed}")


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
