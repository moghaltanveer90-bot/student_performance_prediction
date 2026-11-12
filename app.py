
from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle
from pathlib import Path


class StudentPerformanceApp:

    def __init__(self):

        self.app = Flask(__name__)

        # Project directory
        self.base_dir = Path(__file__).resolve().parent

        # Model file path
        model_path = self.base_dir / 'model.pkl'

        # Check whether model exists
        if not model_path.exists():
            raise FileNotFoundError(
                "model.pkl not found! Run python main.py first."
            )

        # Load trained model
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)

        # Register routes
        self.app.add_url_rule(
            '/',
            'home',
            self.home,
            methods=['GET']
        )

        self.app.add_url_rule(
            '/predict',
            'predict',
            self.predict,
            methods=['POST']
        )

    # HOME PAGE
    def home(self):

        return render_template(
            'index.html',
            prediction=None,
            error=None
        )

    # PREDICTION
    def predict(self):

        try:

            hours = float(request.form['hours_studied'])

            scores = float(request.form['previous_scores'])

            extracurricular = int(
                request.form['extracurricular']
            )

            sleep = float(request.form['sleep_hours'])

            papers = int(request.form['sample_papers'])

            # Validate inputs
            if not 0 <= hours <= 24:
                raise ValueError("Study hours must be between 0 and 24.")

            if not 0 <= scores <= 100:
                raise ValueError("Previous scores must be between 0 and 100.")

            if extracurricular not in [0, 1]:
                raise ValueError("Select a valid extracurricular option.")

            if not 0 <= sleep <= 24:
                raise ValueError("Sleep hours must be between 0 and 24.")

            if papers < 0:
                raise ValueError("Sample papers cannot be negative.")

            # Prepare input data
            data = pd.DataFrame(
                [[hours, scores, extracurricular, sleep, papers]],
                columns=[
                    'Hours Studied',
                    'Previous Scores',
                    'Extracurricular Activities',
                    'Sleep Hours',
                    'Sample Question Papers Practiced'
                ]
            )

            # Generate prediction
            result = self.model.predict(data)[0]

            prediction = round(
                float(np.clip(result, 0, 100)),
                2
            )

            return render_template(
                'index.html',
                prediction=prediction,
                error=None
            )

        except (ValueError, KeyError) as e:

            return render_template(
                'index.html',
                prediction=None,
                error=str(e)
            )

        except Exception as e:

            print("Prediction error:", e)

            return render_template(
                'index.html',
                prediction=None,
                error="Unable to generate prediction. Check the application terminal."
            )


# CREATE APPLICATION
student_app = StudentPerformanceApp()

app = student_app.app


# RUN FLASK
if __name__ == '__main__':

    app.run(debug=True)
