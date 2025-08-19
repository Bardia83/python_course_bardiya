# California Housing Linear Regression

A machine learning project that implements linear regression models to predict housing prices in California using the California Housing dataset.

## 📁 Project Structure

```
california_housing_linear_regression/
├── california_housing_linear_regression.py  # Main Python script
├── README.md                                # Project documentation
└── requirements.txt                         # Dependencies
```

## 🚀 Features

- **Data Analysis**: Exploratory data analysis and correlation heatmap visualization
- **Multiple Regression Models**:
  - Linear Regression
  - Ridge Regression (L2 regularization)
  - Lasso Regression (L1 regularization)
- **Model Evaluation**: MSE and R² score metrics
- **Visualization**: Actual vs Predicted prices scatter plot

## 📊 Dataset

The project uses the California Housing dataset from scikit-learn, which contains:
- 20,640 samples
- 8 features (median income, house age, average rooms, average bedrooms, population, average occupancy, latitude, longitude)
- Target variable: Median house value

## 🛠️ Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd california_housing_linear_regression
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## 📋 Requirements

- Python 3.7+
- pandas
- scikit-learn
- matplotlib
- seaborn
- numpy

## 🎯 Usage

Run the main script:
```bash
python california_housing_linear_regression.py
```

The script will:
1. Load and explore the California Housing dataset
2. Perform correlation analysis
3. Train linear regression models
4. Evaluate model performance
5. Generate visualizations

## 🔧 Selected Features

The model uses the following key features for prediction:
- `MedInc`: Median income in block group
- `HouseAge`: Median house age in block group
- `AveRooms`: Average number of rooms per household
- `AveOccup`: Average number of household members

## 📈 Results

The models are evaluated using:
- **Mean Squared Error (MSE)**: Lower values indicate better performance
- **R² Score**: Higher values indicate better fit (closer to 1.0 is better)

## 📊 Visualization

The project includes a scatter plot comparing actual vs predicted house prices, helping visualize model performance.

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements.

## 📝 License

This project is open source and available under the MIT License.
