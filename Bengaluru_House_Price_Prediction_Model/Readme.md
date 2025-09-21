# 🏠 Bengaluru House Price Prediction

<div align="center">

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Jupyter](https://img.shields.io/badge/jupyter-%23F37626.svg?style=flat&logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=flat&logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green.svg)

*A comprehensive machine learning project that predicts house prices using linear regression with extensive data analysis and visualization.*

</div>

## 📋 Table of Contents

- [🎯 Project Overview](#-project-overview)
- [✨ Features](#-features)
- [🛠️ Technologies Used](#️-technologies-used)
- [📊 Dataset](#-dataset)
- [🚀 Quick Start](#-quick-start)
- [📈 Project Structure](#-project-structure)
- [🔍 Analysis & Methodology](#-analysis--methodology)
- [📊 Model Performance](#-model-performance)
- [📸 Visualizations](#-visualizations)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

## 🎯 Project Overview

This project is a machine learning application designed to predict house prices in Bengaluru, India. It utilizes a Linear Regression model trained on a comprehensive dataset of real estate properties. The primary goal is to provide a reliable and data-driven estimate of property values based on key features like location, size (in square feet), and the number of bedrooms and bathrooms.

To make the model accessible to a non-technical audience, it is deployed as an interactive web application using Streamlit. Users can input the property's specifications and receive an instant price prediction.

### Key Objectives:
- 🏡 Predict house prices accurately using property features
- 📊 Perform extensive exploratory data analysis (EDA)
- 🎨 Create insightful visualizations
- 📈 Evaluate model performance using multiple metrics
- 🔬 Understand feature importance and correlations

## ✨ Features

-   **Accurate Price Prediction**: Leverages a Linear Regression model to provide property price estimates.
-   **Interactive Web Interface**: A user-friendly web application built with Streamlit for easy interaction.
-   **Data-Driven Insights**: The model is trained on a real-world dataset from Bengaluru, capturing market trends.
-   **Simple and Intuitive**: The interface allows users to easily input property details and get a prediction.

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) | Core programming language |
| ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) | Data manipulation and analysis |
| ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white) | Numerical computing |
| ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white) | Machine learning library |
| ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white) | Interactive development environment |
| ![Streanlit](https://img.shields.io/badge/Streamlit-F37626?style=flat&logo=streamlit&logoColor=white) | For creating and deploying the interactive web application |
| ![Pickle](https://img.shields.io/badge/Pickle-F37626?style=flat&logo=pickle&logoColor=white) | For saving and loading the trained model |

## 📊 Dataset

The dataset used for this project was sourced from **Kaggle**. It contains 13,320 records of properties in the Bengaluru area.

The key features of the dataset include:
*   `location`: The neighborhood in Bengaluru.
*   `size`: The number of bedrooms (BHK).
*   `total_sqft`: The total area in square feet.
*   `bath`: The number of bathrooms.
*   `balcony`: The number of balconies.
*   `price`: The price of the house in Indian Rupees (Lakhs).

Significant data cleaning and feature engineering were performed to prepare the data for modeling. This included handling missing values, removing outliers, and transforming categorical data.

## 🤖 Model

The predictive model is based on **Linear Regression**, a fundamental supervised learning algorithm. It was chosen for its interpretability and efficiency in modeling relationships between continuous variables. The model establishes a linear relationship between the input features (location, sqft, bedrooms, etc.) and the target variable (price).

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip or conda package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd House_Price_Prediction_Using_Linear_Regression
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch Jupyter Notebook**
   ```bash
   jupyter notebook HPPULR.ipynb
   ```

4. **Run the analysis**
   - Execute cells sequentially from top to bottom
   - Enjoy the visualizations and analysis! 📊
  
## Usage

Once the setup is complete, you can run the Streamlit application.

**1. Run the Streamlit App**
In your terminal, navigate to the project's root directory and run the following command:
```bash
streamlit run app.py
```
*(Replace `app.py` with the name of your main Python script if it's different.)*

**2. Interact with the Application**
Your default web browser will open a new tab with the application running.
-   Select the desired **location** from the dropdown menu.
-   Enter the **total square feet**, number of **bedrooms**, **bathrooms**, and **balconies**.
-   Click the "**Predict Price**" button to see the estimated price of the house.

## 📈 Project Structure

```Bengaluru-House-Price-Prediction/
│
├── data/
│   ├── Cleaned_data.csv        # Cleaned data used for training
│   └── Raw_Data.csv            # Raw dataset
│
├── model/
│   └── Bengaluru_House_Price_model.pkl # The trained model file
│
├── app.py                      # Main Streamlit application script
├── background_image.png        # Background image
├── Bengaluru_House_price_Prediction.ipynb        # Jupyter Notebook for model development and analysis
├── requirements.txt            # List of Python dependencies for pip
└── README.md                   # Project documentation (this file)
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🔄 Open a Pull Request

### Ideas for Contributions:
- 🔧 Feature engineering improvements
- 🤖 Additional ML algorithms (Random Forest, XGBoost)
- 📊 More visualization techniques
- 🧪 Cross-validation implementation
- 📝 Documentation enhancements

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

### 🌟 If you found this project helpful, please give it a star! ⭐

**Made with ❤️ and Python**

</div>

---





