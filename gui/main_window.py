import customtkinter as ctk


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Algorithm Visualizer")
        self.geometry("1024x768")

        # Create a sidebar for controls
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.pack(side="left", fill="y", padx=10, pady=10)

        # Add a start button to the sidebar
        self.start_button = ctk.CTkButton(
            self.sidebar, text="Start", command=self.start_visualization
        )
        self.start_button.pack(pady=10)

        # Placeholder for more controls like sliders, dropdowns, etc.

        # Create a main frame for the animation canvas
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Placeholder for animation canvas
        # self.animation_canvas = ...

    def start_visualization(self):
        # Placeholder for starting the visualization
        print("Visualization started")


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
