# DVP - Data Visualization with Python

Welcome! This repository has been fully upgraded to **interactive Jupyter Notebooks (`.ipynb`)** to provide a hands-on, engaging, and premium learning experience for Data Visualization with Python (DVP).

Each topic is structured into individual notebooks featuring rich Markdown headers, step-by-step descriptions, and interactive code cells that let you run and visualize outcomes in real-time.

---

## Repository Structure

The repository is organized into structured chapters:

1. **[01_Python_Basics](file:///d:/Code/Repo/DVP/01_Python_Basics)**:
   - [01.ipynb](file:///d:/Code/Repo/DVP/01_Python_Basics/01.ipynb): Student Test Scores Average Calculator & Palindrome/Digit Frequency Checker.
2. **[02_Functions_and_Conversions](file:///d:/Code/Repo/DVP/02_Functions_and_Conversions)**:
   - [02.ipynb](file:///d:/Code/Repo/DVP/02_Functions_and_Conversions/02.ipynb): Fibonacci Sequence Generator & Number System Conversions.
3. **[03_String_Manipulation](file:///d:/Code/Repo/DVP/03_String_Manipulation)**:
   - [03.ipynb](file:///d:/Code/Repo/DVP/03_String_Manipulation/03.ipynb): Sentence Character & Word Analyzer & String Similarity Calculator.
4. **[04_Matplotlib_Bar_Scatter](file:///d:/Code/Repo/DVP/04_Matplotlib_Bar_Scatter)**:
   - [04.ipynb](file:///d:/Code/Repo/DVP/04_Matplotlib_Bar_Scatter/04.ipynb): Categories Bar Plot Visualization & Bubble Scatter Plot of Chocolate Sales.
5. **[05_Matplotlib_Histogram_Pie](file:///d:/Code/Repo/DVP/05_Matplotlib_Histogram_Pie)**:
   - [05.ipynb](file:///d:/Code/Repo/DVP/05_Matplotlib_Histogram_Pie/05.ipynb): Grade Distribution Histogram & Forest Cover Pie Chart.
6. **[06_Matplotlib_Linear_Plotting](file:///d:/Code/Repo/DVP/06_Matplotlib_Linear_Plotting)**:
   - [06.ipynb](file:///d:/Code/Repo/DVP/06_Matplotlib_Linear_Plotting/06.ipynb): Multi-Line Linear Equations Plotting & Advanced Formatting.
7. **[07_Seaborn_Customization](file:///d:/Code/Repo/DVP/07_Seaborn_Customization)**:
   - [07.ipynb](file:///d:/Code/Repo/DVP/07_Seaborn_Customization/07.ipynb): Multi-chart Statistical Dashboard (Joint plot, KDE, Heatmap, Pair plot, Box/Regression plots).
8. **[08_Bokeh_Linegraph](file:///d:/Code/Repo/DVP/08_Bokeh_Linegraph)**:
   - [08.ipynb](file:///d:/Code/Repo/DVP/08_Bokeh_Linegraph/08.ipynb): Interactive Line Graphs & Multi-plot Bokeh Dashboard.
9. **[09_Plotly_3D](file:///d:/Code/Repo/DVP/09_Plotly_3D)**:
   - [09.ipynb](file:///d:/Code/Repo/DVP/09_Plotly_3D/09.ipynb): Interactive 3D Surface Plots & 3D Scatter Plots using Plotly.
10. **[10_Plotly_TimeSeries_Maps](file:///d:/Code/Repo/DVP/10_Plotly_TimeSeries_Maps)**:
    - [10.ipynb](file:///d:/Code/Repo/DVP/10_Plotly_TimeSeries_Maps/10.ipynb): Financial Time-Series Visualizations & Global Earthquake Map.

---

## Installation & Setup

To run these interactive notebooks locally, we recommend using a Python virtual environment.

### 1. Setup Virtual Environment

- **Create a virtual environment:**
  ```bash
  python -m venv venv
  ```
- **Activate the virtual environment:**
  - **Windows (Command Prompt / PowerShell):**
    ```powershell
    venv\Scripts\activate
    ```
  - **Mac / Linux:**
    ```bash
    source venv/bin/activate
    ```

### 2. Install Dependencies

Install all required visualization and Jupyter tools with:

```bash
pip install -r requirements.txt
```

---

## How to Run the Notebooks

There are two main ways to run these notebooks locally:

### Option A: Using Visual Studio Code (Recommended)

1. Open Visual Studio Code and load the project repository folder.
2. Install the **Python** and **Jupyter** extensions from the VS Code Marketplace.
3. Open any `.ipynb` file.
4. Select the `venv` virtual environment as your active kernel in the top-right corner.
5. Click **Run All** or execute individual cells sequentially!

### Option B: Using Jupyter Classic / JupyterLab

1. Start the Jupyter environment from your terminal:
   ```bash
   jupyter lab
   ```
   _or_
   ```bash
   jupyter notebook
   ```
2. Your browser will open the Jupyter File Tree. Navigate to any folder and select a notebook.
3. Run the cells step-by-step using `Shift + Enter`!
