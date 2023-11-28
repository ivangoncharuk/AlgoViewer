import customtkinter as ctk


def enable_controls(obj, enable):
    """
    Enable or disable control buttons.
    """
    # obj.reset_button.configure(state=ctk.NORMAL if enable else ctk.DISABLED)
    obj.load_random_data_button.configure(state=ctk.NORMAL if enable else ctk.DISABLED)
    obj.algorithm_combo.configure(state=ctk.NORMAL if enable else ctk.DISABLED)
    obj.clear_canvas_button.configure(state=ctk.NORMAL if enable else ctk.DISABLED)


def setup_play_pause_button(obj):
    obj.play_pause_button = ctk.CTkButton(
        obj.sidebar, text="Play", command=obj.toggle_visualization
    )
    obj.play_pause_button.pack(pady=10)


# def setup_reset_button(obj):
#     obj.reset_button = ctk.CTkButton(
#         obj.sidebar, text="Reset", command=obj.reset_visualization
#     )
#     obj.reset_button.pack(pady=10)


def setup_clear_canvas_button(obj):
    obj.clear_canvas_button = ctk.CTkButton(
        obj.sidebar, text="Clear Canvas", command=obj.clear_only_canvas
    )
    obj.clear_canvas_button.pack(pady=10)


def setup_load_random_data_button(obj):
    obj.load_random_data_button = ctk.CTkButton(
        obj.sidebar, text="Load Random Data", command=obj.randomize_canvas
    )
    obj.load_random_data_button.pack(pady=10)


def setup_algorithm_combo(obj):
    obj.algorithm_combo = ctk.CTkComboBox(
        obj.sidebar, values=["Bubble Sort", "Quick Sort"]
    )
    obj.algorithm_combo.pack(pady=10)
    obj.algorithm_combo.bind("<<ComboboxSelected>>", obj.on_algorithm_change)


def setup_num_bars_slider(obj):
    obj.num_bars_label = ctk.CTkLabel(obj.sidebar, text="Number of Bars: 50")
    obj.num_bars_label.pack(pady=(10, 0))
    obj.number_of_bars_slider = ctk.CTkSlider(
        obj.sidebar, from_=10, to=100, command=obj.update_num_bars_label
    )
    obj.number_of_bars_slider.set(50)
    obj.number_of_bars_slider.pack(pady=10)


def setup_speed_slider(obj):
    obj.speed_label = ctk.CTkLabel(obj.sidebar, text="Visualization Speed: 1")
    obj.speed_label.pack(pady=(10, 0))
    obj.speed_slider = ctk.CTkSlider(
        obj.sidebar, from_=1, to=100, command=obj.update_speed_label
    )
    obj.speed_slider.set(1)
    obj.speed_slider.pack(pady=10)
