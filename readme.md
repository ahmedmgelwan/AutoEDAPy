# AutoEDA-Py Documentation

The **AutoEDA-Py** module provides a Python-based toolkit for automating Exploratory Data Analysis (EDA) tasks. This module simplifies the process of uncovering insights, cleaning data, and visualizing patterns within datasets. It leverages popular libraries like pandas, matplotlib, and seaborn to enhance your data analysis workflow.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Class: AutoEDA](#class-autoeda)
    - [Constructor](#constructor)
    - [Exploratory Data Analysis](#exploratory-data-analysis)
    - [Data Cleaning](#data-cleaning)
    - [Data Visualization](#data-visualization)
- [Example](#example)

## Introduction

The AutoEDA-Py module offers an efficient way to perform Exploratory Data Analysis on your datasets. It handles essential tasks such as data summary, duplicate removal, missing value handling, and visualization.

## Installation

To use the `AutoEDA` class, ensure you have the required libraries installed:

```bash
pip install pandas matplotlib seaborn
```

## Usage

```
pythonCopy codefrom auto_eda import AutoEDA

# Replace 'your_dataset.csv' with your actual dataset file path
eda_instance = AutoEDA('your_dataset.csv')
```

## Class: AutoEDA

### Constructor

#### `AutoEDA(file_path)`

The EDA class constructor accepts a file path parameter that points to a CSV or Excel dataset file. It loads the dataset into a pandas DataFrame based on the file extension.

### Exploratory Data Analysis

#### `explore_data()`

This method performs exploratory data analysis on the loaded dataset. It displays basic information about the data, including the number of rows and columns, data types, and summary statistics.

### Data Cleaning

#### `clean_data()`

The `clean_data` method handles duplicate rows and missing values in the dataset. It identifies and removes duplicate rows if present and provides options to handle missing values by either dropping them, filling with the mean, or filling with the median.

### Data Visualization

#### `visualize_data()`

The `visualize_data` method generates various visualizations for the dataset, including:

- Heatmap for numeric feature correlations (if more than one numeric feature exists).
- Count plots for categorical features with less than 10 unique values.
- Histograms for quantitative features.
- Pair plots for visualizing relationships between numeric features.

## Example
```
from auto_eda import EDA

eda_instance = EDA()
```

# Perform exploratory data analysis
eda_instance.explore_data()

# Clean the dataset
eda_instance.clean_data()

# Visualize the data
eda_instance.visualize_data()
```



