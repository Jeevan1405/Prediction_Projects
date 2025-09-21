
# Bengaluru House Price Prediction

## Table of Contents
* [Project Overview](#project-overview)
* [Features](#features)
* [Dataset](#dataset)
* [Model](#model)
* [Technology Stack](#technology-stack)
* [Setup and Installation](#setup-and-installation)
* [Usage](#usage)
* [Project Structure](#project-structure)
* [Contributing](#contributing)
* [License](#license)

## Project Overview

This project is a machine learning application designed to predict house prices in Bengaluru, India. It utilizes a Linear Regression model trained on a comprehensive dataset of real estate properties. The primary goal is to provide a reliable and data-driven estimate of property values based on key features like location, size (in square feet), and the number of bedrooms and bathrooms.

To make the model accessible to a non-technical audience, it is deployed as an interactive web application using Streamlit. Users can input the property's specifications and receive an instant price prediction.

## Features

-   **Accurate Price Prediction**: Leverages a Linear Regression model to provide property price estimates.
-   **Interactive Web Interface**: A user-friendly web application built with Streamlit for easy interaction.
-   **Data-Driven Insights**: The model is trained on a real-world dataset from Bengaluru, capturing market trends.
-   **Simple and Intuitive**: The interface allows users to easily input property details and get a prediction.

## Dataset

The dataset used for this project was sourced from **Kaggle**. It contains 13,320 records of properties in the Bengaluru area.

The key features of the dataset include:
*   `location`: The neighborhood in Bengaluru.
*   `size`: The number of bedrooms (BHK).
*   `total_sqft`: The total area in square feet.
*   `bath`: The number of bathrooms.
*   `balcony`: The number of balconies.
*   `price`: The price of the house in Indian Rupees (Lakhs).

Significant data cleaning and feature engineering were performed to prepare the data for modeling. This included handling missing values, removing outliers, and transforming categorical data.

## Model

The predictive model is based on **Linear Regression**, a fundamental supervised learning algorithm. It was chosen for its interpretability and efficiency in modeling relationships between continuous variables. The model establishes a linear relationship between the input features (location, sqft, bedrooms, etc.) and the target variable (price).

## Technology Stack

*   **Python**: The core programming language for the project.
*   **Pandas & NumPy**: For data manipulation and numerical operations.
*   **Scikit-learn**: For building and training the Linear Regression model.
*   **Streamlit**: For creating and deploying the interactive web application.
*   **Pickle**: For saving and loading the trained model.

## Setup and Installation

To run this project on your local machine, please follow these steps:

**1. Clone the Repository**
```bash
git clone https://github.com/your-username/Bengaluru-House-Price-Prediction.git
cd Bengaluru-House-Price-Prediction
```
*(Remember to replace `your-username` with your actual GitHub username.)*

**2. Create a Virtual Environment (Recommended)**
It is highly recommended to create a virtual environment to manage project dependencies.
```bash
# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
```

**3. Install Dependencies**
This project's dependencies are listed in the `requirements.txt` file. You can install them using pip.
```bash
pip install -r requirements.txt
```

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

## Project Structure

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

## Contributing

Contributions are welcome! If you have suggestions for improving this project, please feel free to fork the repository and submit a pull request. You can also open an issue with the "enhancement" tag.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.


