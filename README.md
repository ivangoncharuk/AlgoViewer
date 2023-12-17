# README for Algorithm Visualizer Project

## Introduction

The Algorithm Visualizer is a Python application designed to visualize sorting algorithms. Currently, it supports Bubble Sort and Quick Sort. This tool is ideal for educational purposes, allowing users to see how these algorithms operate in real-time.

## Video Demo



https://github.com/ivangoncharuk/AlgoViewer/assets/85744041/37e0f18a-cd1f-4aef-8391-32732cee2867



## Getting Started

### Prerequisites

- Python 3.11

### Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory.

### Running the Application

Execute the following command in the project directory:

```bash
python main.py
```

## Features

- **Visual Representation**: Visualize the sorting process in a graphical interface.
- **Algorithm Selection**: Choose between Bubble Sort and Quick Sort.
- **Customization**: Adjust the number of elements and the speed of visualization.

## How It Works

The application is built using the `customtkinter` library for the GUI and is structured around the `MainWindow` class.

- **MainWindow Class**: The central class that manages the GUI, including the sidebar and main frame for animation.
- **Visualization**: The sorting process is visualized on an animation canvas where each element's height represents its value.
- **Controls**: Play/Pause, Reset, and other controls are available in the sidebar to interact with the visualization.
- **Performance Tracking**: The application tracks and displays the number of comparisons and swaps made during the sorting process.

## Conclusion

This project serves as a useful educational tool for understanding and visualizing sorting algorithms. 
Future enhancements will include:
- adding more algorithms
- improving the GUI
- refactoring components into their own classes
- adding pathfinding algorithms
- including sounds
- better animations
