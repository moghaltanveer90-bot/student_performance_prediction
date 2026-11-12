# Student Performance Prediction Model

## Model Description

This project uses a **Linear Regression Machine Learning Model** to predict students' academic performance based on their study habits and academic information.

The model learns the relationship between five input features and the student's Performance Index using historical student data.

## Algorithm Used
- Linear Regression

## Input Features
1. Hours Studied
2. Previous Scores
3. Extracurricular Activities
4. Sleep Hours
5. Sample Question Papers Practiced

## Output
- Predicted Performance Index (0–100)

## Model Training
- Dataset: Student_Performance.csv
- Train-Test Split: 80% Training and 20% Testing
- Feature preprocessing: Extracurricular Activities converted into numerical values (Yes = 1, No = 0).
- Model training: Linear Regression

## Model Evaluation
The model is evaluated using:
- R² Score
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

## Model File
The trained model is saved as `model.pkl` using Python Pickle and loaded into the Flask application for making predictions.

## Prediction Process
1. User enters student information.
2. Input data is converted into the required format.
3. The trained Linear Regression model processes the inputs.
4. The model predicts the Performance Index.
5. The predicted result is displayed on the web application.

## Objective
To estimate student academic performance using Machine Learning and identify how study-related factors contribute to academic outcomes.

## Conclusion

The Student Performance Prediction Model successfully demonstrates how Machine Learning can be used to estimate students' academic performance based on their study habits and academic information. By applying the Linear Regression algorithm, the model learns patterns from historical student data and generates a predicted Performance Index.

This project provides practical experience in data preprocessing, data visualization, model training, model evaluation, and deployment using Flask. It also demonstrates how Machine Learning can be integrated into a web application to make predictions through a simple user interface.

Overall, this project aims to support better understanding of the factors associated with student performance and demonstrates the practical use of predictive analytics in education.
