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
