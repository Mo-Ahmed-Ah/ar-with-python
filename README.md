# AR with Python

## Recommendation to Use Conda for Installing Python:

To ensure a stable and compatible development environment, it is recommended to use **Conda** for installing Python. Follow these steps:

### Steps:

1. **Download Conda**:
   - Download Conda from the following link:
     [Download Anaconda](https://repo.anaconda.com/archive/Anaconda3-2024.06-1-Windows-x86_64.exe).

2. **Install Anaconda**:
   - After downloading, install Anaconda on your system.

3. **Open Anaconda Prompt**:
   - After installation, open Anaconda Prompt from the programs menu.

4. **Create a Python 3.7 Environment**:
   - Create and activate a Python 3.7 environment using the following commands:
     ```bash
     conda create --name python3.7 python=3.7
     conda activate python3.7
     ```

5. **Install OpenCV Library**:
   - Install the OpenCV library and the version with additional modules using the following commands:
     ```bash
     pip install opencv-python==4.5.5.64
     pip install opencv-contrib-python==4.5.5.64
     ```

---

## Running Python Files in Visual Studio Code (VS Code)

To run Python files using **Visual Studio Code (VS Code)**, follow these steps:

### Steps:

1. **Download and Install VS Code**:
   - If you don’t have VS Code installed, download it from:
     [Download Visual Studio Code](https://code.visualstudio.com/download).

2. **Install Python Extension for VS Code**:
   - Open VS Code.
   - Go to the **Extensions** view by clicking on the square icon in the sidebar (or press `Ctrl+Shift+X`).
   - Search for the **Python** extension by Microsoft and install it.

3. **Set Python Interpreter**:
   - Once you have installed the Python extension, open your Python file or create a new one.
   - Press `Ctrl+Shift+P` to open the command palette.
   - Type **Python: Select Interpreter** and choose the interpreter from the Conda environment you created (e.g., `python3.7`).

4. **Open Terminal in VS Code**:
   - To run your Python file, open the integrated terminal in VS Code by navigating to the **Terminal** menu and selecting **New Terminal**.
   - Make sure your Conda environment is activated in the terminal by typing:
     ```bash
     conda activate python3.7
     ```

5. **Run the Python File**:
   - In the terminal, navigate to the folder where your Python file is located:
     ```bash
     cd path_to_your_project
     ```
   - Run the Python file using the following command:
     ```bash
     python your_script.py
     ```

6. **Running Python Code in VS Code**:
   - Alternatively, you can run the Python file directly in VS Code by pressing `F5` (or `Ctrl+F5` for running without debugging).

---

### Notes:
- Make sure to activate the correct Conda environment in the terminal before running your Python scripts.
- You can install any additional Python packages using the VS Code terminal with the `pip install package_name` command.

---

### Example:
If your Python script is located in `e:\larne\python\ar-with-python\code\CREATE_MARKER`, the steps would be:
```bash
cd e:\larne\python\ar-with-python\code\CREATE_MARKER
python main.py
