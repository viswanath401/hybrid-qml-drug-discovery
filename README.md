# Quantum Machine Learning for Drug Discovery

## Overview

This project focuses on developing a **hybrid quantum-classical machine learning model** to predict molecular toxicity, a critical task in drug discovery. The goal is to investigate whether quantum-enhanced models can provide improved performance compared to traditional classical machine learning approaches.

The system processes molecular data in the form of SMILES strings, converts them into numerical representations using cheminformatics techniques, and feeds them into a hybrid architecture combining classical neural networks with quantum circuits.

---

## Problem Statement

Traditional drug discovery pipelines rely heavily on classical machine learning models for predicting molecular properties such as toxicity. However, these models may face limitations in capturing complex molecular interactions.

This project explores the integration of quantum computing with machine learning to enhance predictive capabilities.

---

## Methodology

### 1. Data Processing

* Input: SMILES (Simplified Molecular Input Line Entry System)
* Conversion to molecular structures using RDKit
* Feature extraction using Morgan fingerprints

### 2. Classical Baseline Model

* Model: Random Forest / Neural Network
* Purpose: Serve as a benchmark for comparison

### 3. Quantum Model

* Implementation of Variational Quantum Circuits (VQC)
* Encoding classical data into quantum states using angle embedding
* Entanglement layers for feature interaction

### 4. Hybrid Architecture

* Classical preprocessing layer
* Quantum layer (feature transformation)
* Classical output layer for prediction

### 5. Training

* Loss Function: Binary Cross Entropy
* Optimizer: Adam
* Evaluation using train-test split

---

## Technology Stack

* Quantum Computing:

  * PennyLane
  * Qiskit

* Machine Learning:

  * PyTorch
  * Scikit-learn

* Cheminformatics:

  * RDKit

* Data Processing:

  * NumPy
  * Pandas

* Visualization:

  * Matplotlib

---

## Dataset

* Tox21 Dataset

Contains:

* Molecular structures (SMILES)
* Toxicity labels

---

## Results

The project evaluates performance using:

* Accuracy
* Precision
* Recall
* ROC-AUC

### Comparative Analysis

| Model                | Performance                    |
| -------------------- | ------------------------------ |
| Classical Model      | Baseline accuracy              |
| Hybrid Quantum Model | Improved / Comparable accuracy |

Key observations:

* Hybrid models can capture complex feature interactions
* Quantum circuits provide alternative feature representations
* Performance depends on circuit design and data encoding

---

## Key Contributions

* Implementation of a hybrid quantum-classical pipeline
* Integration of quantum circuits into ML workflow
* Comparative study with classical models
* Exploration of quantum advantage in drug discovery

---

## Future Work

* Scaling to larger datasets (e.g., QM9)
* Exploring quantum kernel methods
* Running models on real quantum hardware
* Optimizing quantum circuit depth and noise handling

---

## Conclusion

This project demonstrates the feasibility of combining quantum computing with machine learning for drug discovery tasks. While current quantum hardware limitations exist, hybrid approaches show promise in advancing molecular property prediction.

---
