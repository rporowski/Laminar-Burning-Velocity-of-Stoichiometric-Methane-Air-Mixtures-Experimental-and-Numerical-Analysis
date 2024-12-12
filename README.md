# Laminar-Burning-Velocity-of-Stoichiometric-Methane-Air-Mixtures-Experimental-and-Numerical-Analysis
This project investigates the laminar burning velocity (LBV) of stoichiometric methane-air mixtures using experimental data and numerical simulations. It provides insights into methane combustion characteristics, highlighting its importance in efficient and safe energy systems.
Project Description
The project explores the laminar burning velocity (LBV) of methane-air mixtures through a combination of experimental measurements and computational models. The main focus is to validate and compare different numerical models for LBV prediction against experimental data under varying initial temperatures.

Features
Experimental Data
Measurements performed in a 20 L spherical combustion chamber.
Key parameters include:
Maximum explosion pressure (
𝑃
𝑚
𝑎
𝑥
P 
max
​
 ).
Maximum rate of pressure rise (
𝑑
𝑃
/
𝑑
𝑡
dP/dt).
Initial temperature variations were explored to assess the temperature's impact on LBV.
Numerical Modeling
Models Used:
Manton's Method.
Lewis and von Elbe's Model.
Bradley and Mitcheson's Model.
Dahoe's Thin Flame Models (2005 and 2013).
Simulation Framework:
Cantera library with GRI-Mech 3.0 mechanism was employed for numerical validation.
Key Insights
LBV increases with initial temperature, consistent with theoretical expectations.
Dahoe's thin flame model, despite simplifications, demonstrated high reliability.
The experimental results aligned closely with predictions from Cantera and numerical models.
Objectives
Measure LBV experimentally under controlled conditions.
Validate numerical models by comparing them to experimental data.
Provide recommendations for safe and efficient methane combustion system design.
Applications
Industrial Combustion Systems:
Enhances the design of safe and efficient methane burners.
Energy Transition:
Highlights methane's role as a bridge fuel toward cleaner energy sources.
Scientific Research:
Provides a framework for future LBV studies in other fuel-air mixtures.
Project Implementation
Data Sources
Experimental data collected from combustion chamber experiments.
Computational data derived from Cantera simulations and theoretical models.
Tools and Libraries
Python Libraries:
Cantera: For combustion simulations and flame speed analysis.
NumPy and SciPy: For data processing and numerical calculations.
Matplotlib and Seaborn: For data visualization.
Numerical Methods:
Implemented Manton, Lewis and von Elbe, Bradley and Mitcheson, and Dahoe models for LBV calculation.
Repository Structure
bash
Skopiuj kod
.
├── data/                   # Experimental and simulated data files
├── models/                 # Numerical models for LBV calculation
├── notebooks/              # Jupyter Notebooks for analysis and visualization
├── scripts/                # Python scripts for simulations and data processing
├── README.md               # Project description
└── requirements.txt        # Python dependencies
How to Run
Clone the repository:

bash
Skopiuj kod
git clone https://github.com/your-username/methane-lbv-analysis.git
cd methane-lbv-analysis
Install dependencies:

bash
Skopiuj kod
pip install -r requirements.txt
Run simulations:

Use the Jupyter Notebooks in the notebooks/ directory to explore experimental and numerical results.
Example:
bash
Skopiuj kod
jupyter notebook notebooks/lbv_analysis.ipynb
Results
Experimental and numerical results demonstrate that LBV increases with initial temperature.
Dahoe's models (2005 and 2013) are particularly reliable for practical applications.
The project underscores methane's role in industrial and transitional energy systems.
Future Work
Expand the study to include other fuel-air mixtures.
Explore advanced chemical kinetic mechanisms for more detailed analysis.
Integrate other numerical models to refine LBV predictions further.
This README provides an overview of the project and guides users to replicate and extend the analysis. If you'd like further refinements, let me know!
