# 🧮 K-Means Clustering with Manhattan Distance (Python)

This project implements a modified K-Means clustering algorithm that uses **Manhattan distance** (L1 norm) for grouping 2D data points on a grid. It's a simple yet insightful way to understand unsupervised machine learning techniques using only built-in Python modules.

---

## 📌 Features

- Random generation of data points and initial cluster centers
- K-Means clustering using Manhattan distance metric
- Text-based visualization of clusters on a grid
- Saves initial data to a file for reproducibility

---

## 🧠 How It Works

1. **Data Generation**: 
   - `N` random data points and `K` random initial cluster centers are created on a 2D grid.
2. **Clustering**:
   - Each point is assigned to the nearest cluster center using **Manhattan distance**.
   - Cluster centers are updated based on the **mean** (approximation of median) of their assigned points.
   - This process repeats until the centers converge or a maximum number of iterations is reached.
3. **Visualization**:
   - Final cluster assignment is visualized using a simple grid in the console.

---

## 🛠️ Installation & Usage

### Requirements
- Python 3.x
- No external libraries required

### Run the Program

```bash
python clustering.py
```

