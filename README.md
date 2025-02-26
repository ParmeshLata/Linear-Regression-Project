# Linear Regression Model for Predicting Height from Weight

## Overview
This project implements a **Linear Regression Model** using **scikit-learn** to predict height based on weight. The dataset used is `weight-height.csv`, which contains weight and height measurements.

## Dependencies
Ensure you have the following Python libraries installed before running the script:
- `pandas`
- `scikit-learn`
- `matplotlib`

## Dataset
The dataset (weight-height.csv) consists of two main columns:
- `WEIGHT (in kg)`
- `HEIGHT (in cm)`

## Implementation Steps
### Loading the Dataset
- `The dataset is loaded using pandas.read_csv().`

### Data Preprocessing
- `Features (WEIGHT) and target (HEIGHT) are extracted.
The dataset is split into training and testing sets (75% training, 25% testing).
Standardization is applied to the input feature using StandardScaler.`

### Model Training
- `A LinearRegression model is trained using the standardized weight values.`

### Prediction & Evaluation
- `The model makes predictions on both training and test data.
The performance is evaluated using the R² score.`

### Visualization
- `The best-fit line is plotted along with the actual data points.`

### Making New Predictions
- `The model predicts height for a given weight (e.g., 80 kg).`

## Running the Script
- `Save the script as linear_regression.py and execute it:`

## Expected Output
- `A plot showing the best-fit line for training data.`
- `Predicted height for a given weight.`
- `R² score indicating model performance.`

## You can install them using:
```sh
pip install pandas scikit-learn matplotlib

## Conclusion
- `This linear regression model provides a simple yet effective way to predict height based on weight. For better accuracy, additional features (such as age, gender, etc.) can be incorporated.`
