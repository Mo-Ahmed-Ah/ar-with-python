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

6. **Run Your Program**:
   - After setting up the environment and installing the required libraries, you can run your program using:
     ```bash
     python path_to_your_script.py
     ```

---

### Notes:
- Make sure to update your environment when installing new libraries.
- You can use `conda deactivate` to deactivate the environment at any time.
