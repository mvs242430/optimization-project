# TECH4: Optimization & Network Design



## Project Overview

### Part A: Electrical Station Location Problem
The objective is to determine the optimal locations for electrical stations to serve 20 neighborhoods while minimizing the total cost.
* **Constraints:** 100 possible station locations arranged in a $10 \times 10$ grid.
* **Cost Structure:** Total cost = Fixed installation cost + Variable wiring cost ($km \times unit\_cost$).



### Part B: Road Network Optimization
This part utilizes a Minimum Spanning Tree (MST) approach to identify the most cost-effective road network to connect a set of cities (N, E, S, W, etc.).

* **Analysis:** Evaluates net profit across 5, 10, and 20-year utilization periods.
* **Implementation:** Employs Prim's algorithm to resolve the network connectivity.



## Repository Structure

The project is modularized into scripts for data processing, modeling, and visualization.

```text
home_exam/
├── part_A/
│   ├── models_A.py            # Integer Linear Optimization model
│   ├── util_generate_data.py  # Data generation/transformation
│   ├── util_visualize_A.py    # Result visualization
│   └── solution_tasks_A.py    # Main execution for Part A
├── part_B/
│   ├── prim_alg_B.py          # MST algorithm implementation
│   ├── util_generate_data.py  # Network data generation
│   ├── util_visualize_B.py    # Result visualization
│   └── solution_tasks_B.py    # Main execution for Part B
├── hom_exam_report.pdf        # Detailed project report
└── env.yml                    # Conda environment dependencies