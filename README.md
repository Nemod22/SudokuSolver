# SudokuSolver
Sudoku eye is an aplicatoin that detects sudoku from an image and displays the solution on to that image. It's build using kivy framework and it curently works on desktop platforms and android.
It uses openCV for sodoku board detection and projection of solution, and tensorflow (lite for android) for digits recognition.

<img src="https://github.com/Nemod22/SudokuSolver/assets/32578790/291ec800-9f00-43ad-85bd-0985b36be92e" alt="Image 1" width="450px">

<img src="https://github.com/Nemod22/SudokuSolver/assets/32578790/57e38f68-6adb-4f54-a8fc-2cca582094cb" alt="Image 1" width="450px">

## Installation
1. Clone the repo
   ```sh
   git clone https://github.com/Nemod22/SudokuSolver.git
   ```
2. Install the required dependencies using pip:
   ```sh
   pip install -r requirements.txt
   ```
## Running the app
1. Run the application on your computer:
   ```sh
   python main.py
   ```

## Build for andorid
Buildozer documentation: https://buildozer.readthedocs.io/en/latest/installation.html
