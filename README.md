# Learning From Data -- Machine Learning Implementations

![The Anatomy Lesson of Dr. Nicolaes Tulp](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Rembrandt_-_The_Anatomy_Lesson_of_Dr_Nicolaes_Tulp.jpg/960px-Rembrandt_-_The_Anatomy_Lesson_of_Dr_Nicolaes_Tulp.jpg)

*"The Anatomy Lesson of Dr. Nicolaes Tulp" (1632) by Rembrandt — [Wikipedia](https://en.wikipedia.org/wiki/The_Anatomy_Lesson_of_Dr._Nicolaes_Tulp)*

Implementations of core machine learning algorithms from scratch and applied ML projects, developed for the "Inference and Learning" course at EMAp/FGV (Escola de Matematica Aplicada, Fundacao Getulio Vargas).

## About

This repository contains programming assignments based on the textbook *Learning From Data* by Yasser Abu-Mostafa, Malik Magdon-Ismail, and Hsuan-Tien Lin. Each assignment required implementing a fundamental ML algorithm from scratch in Python, followed by a capstone project applying these techniques to a real-world classification problem.

**Course:** Inference and Learning (Inferencia e Aprendizagem)
**Professor:** Dr. Rodrigo Targino
**Semester:** 2019.1

## Algorithms Implemented

| Algorithm | Description | Directory |
|-----------|-------------|-----------|
| **K-Nearest Neighbors** | Classification via majority vote of k closest training points, using Euclidean distance | `knn/` |
| **Radial Basis Functions** | Function approximation using Gaussian RBF kernels with configurable centroids | `rbf/` |
| **Multilayer Perceptron** | Neural network with sign activation for non-linear decision boundaries | `multilayer_perceptron/` |

## Capstone Project: Breast Cancer Classification

A predictive model to classify breast tumors as malignant or benign using the UCI Wisconsin Breast Cancer dataset (699 samples, 9 features).

**Key results:**

| Model | Test Accuracy |
|-------|--------------|
| Logistic Regression | ~93.8% |
| KNN (k=26) | ~95.7% |
| SVM (RBF kernel) | ~96.7% |

The project includes exploratory data analysis, hyperparameter tuning via k-fold cross-validation, decision boundary visualization, and a comparison across three classifiers of increasing complexity. Full write-up available in `ml-project/`.

## Tech Stack

- Python 3
- NumPy, Pandas, Matplotlib, scikit-learn

## Repository Structure

```
knn/                     # KNN implementation from scratch
rbf/                     # Radial Basis Function network
multilayer_perceptron/   # MLP implementation
ml-project/              # Breast cancer classification project
```

## How to Run

```bash
# Example: run the KNN implementation
python knn/knn.py

# Example: run the RBF network
python rbf/rbf.py
```
