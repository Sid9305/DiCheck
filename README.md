# DiCheck

DiCheck is a diabetes prediction application that uses machine learning to assess an individual's risk of developing diabetes based on various health parameters. The app analyzes factors such as BMI, insulin levels, and HbA1c to provide users with insights into their health and recommendations for preventive measures.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset Creation](#dataset-creation)
- [How It Works](#how-it-works)
- [Contributing](#contributing)

## Features

- Predict the likelihood of diabetes based on user-inputted health metrics.
- User-friendly interface for easy data entry.
- Comprehensive health insights based on machine learning algorithms.
- Clear visualizations of prediction results.

## Technologies Used

- **Programming Languages**: Python
- **Machine Learning Libraries**: scikit-learn, pandas, NumPy
- **Web Framework**: Flask
- **Data Visualization**: Matplotlib, Seaborn
- **Frontend**: HTML, CSS, JavaScript

## Installation

To run the DiCheck application locally, follow these steps:

1. Clone the repository:
   
   git clone https://github.com/Sid9305/DiCheck.git
2. Navigate to the project directory:

cd DiCheck

3. Create a virtual environment (optional but recommended):

python -m venv venv

4. Activate the virtual environment:

On Windows:
venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

5. Install the required packages:

pip install -r requirements.txt

## Usage
Run the Flask application:
python app.py

Open your web browser and go to http://127.0.0.1:5000.

Enter the required health metrics (e.g., age, BMI, insulin levels) into the form.

Click on the "Predict" button to see the prediction results and insights.

## Dataset Creation
The dataset was created using extensive research into diabetes indicators. It includes two subsets:

Diabetic: Contains data points for individuals diagnosed with diabetes.
Non-Diabetic: Contains data points for individuals without diabetes.
The datasets were created using a combination of real-world data and synthetic data generation techniques, ensuring a balanced representation of both groups for accurate predictions.

## How It Works
Data Input: Users input their health metrics through a web form.
Prediction Model: The model processes the input data and uses linear regression to predict the likelihood of diabetes.
Output: Users receive a prediction along with insights and recommendations based on their health metrics.

## Contributing
Contributions are welcome! If you would like to contribute to DiCheck, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch and submit a pull request.
