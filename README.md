# Student Performance Prediction using Machine Learning

## Project Overview

The Student Performance Prediction project uses Machine Learning to predict a student's Performance Index based on study habits, previous academic scores, sleep hours, extracurricular activities, and sample question paper practice.

The project uses a **Linear Regression** algorithm to estimate student performance and a **Flask web application** to allow users to enter their details and receive predictions.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Flask
- HTML
- CSS

## Dataset

Dataset: `Student_Performance.csv`

The dataset contains the following input features:

1. Hours Studied
2. Previous Scores
3. Extracurricular Activities
4. Sleep Hours
5. Sample Question Papers Practiced

**Target Variable:** Performance Index

## Machine Learning Algorithm

**Linear Regression**

The model is trained using the dataset and evaluated using:

- R² Score
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

The dataset is divided into training and testing sets using an 80:20 split.

## Project Structure

```text
Student_Performance_Regression/
│
├── app.py
├── main.py
├── Student_Performance.csv
├── model.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Folder

```bash
cd Student_Performance_Regression
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Environment (Windows)

```bash
.venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn flask
```

### 6. Train the Machine Learning Model

```bash
python main.py
```

This generates the trained model file:

`model.pkl`

### 7. Run the Flask Application

```bash
python app.py
```

Open your browser and visit:

`http://127.0.0.1:5000/`

## Application Features

- Student information input form
- Machine Learning-based performance prediction
- Automatic prediction results
- Input validation
- Interactive web interface
- Data visualization

## Expected Output

The application accepts student academic and lifestyle information and predicts an estimated Performance Index between 0 and 100.

## Future Enhancements

- Implement additional Machine Learning algorithms.
- Improve model performance through hyperparameter tuning.
- Add student performance analytics.
- Deploy the application to a cloud platform.
- Develop a student performance dashboard.

## Author

**Moghal Tanveer**

Computer Science and Engineering – Artificial Intelligence

## Project Purpose

This project demonstrates the practical application of Machine Learning, data preprocessing, model evaluation, and Flask web development to predict student academic performance.
