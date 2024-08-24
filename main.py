from flask import Flask, jsonify, render_template, request
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
import joblib
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

print("hi")

app = Flask(__name__)
app.static_folder = 'static'

# Load the dataset
data = pd.read_csv("finaldataset.csv")

# Separate features and target variable
X = data.drop("diabetes", axis=1)
y = data["diabetes"]

# Apply one-hot encoding to categorical variables
categorical_features = ['gender', 'family_history', 'heart_disease']
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

numeric_features = ['age', 'bmi', 'blood_sugar_level', 'HbA1c_level']
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', categorical_transformer, categorical_features),
        ('num', numeric_transformer, numeric_features)
    ])

# Append classifier to preprocessing pipeline
clf = Pipeline(steps=[('preprocessor', preprocessor),
                      ('classifier', LinearRegression())])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit the model
clf.fit(X_train, y_train)

# Save the trained model
joblib.dump(clf, "linear_regression_model.joblib")

# Define the column names used for predictions
columns = X.columns.tolist()

print("score: ", clf.score(X_test, y_test))

# pred = clf.prediction()
# print("classification report: ")
# print(classification_report(y_test,pred))
# Preprocess input data
def preprocess_input_data(input_data):
    return input_data  # No preprocessing required for linear regression

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/predictform', methods=['POST'])
def predictform():
    print("Predict form route accessed")  # Debugging statement
    try:
        user_input = request.get_json()
        
        # Preprocess input data
        input_data = pd.DataFrame([user_input], columns=columns)

        # Make predictions
        prediction = clf.predict(input_data)
        print(prediction[0])

        # Make predictions
        prediction = clf.predict(input_data)

        # Extract decimal part
        decimal_part = prediction[0] - int(prediction[0])
        print(abs(decimal_part))
        if abs(decimal_part) > 0.5:
            return jsonify({'prediction': 'You are possibly diabetic'}),200
        else:
            return jsonify({'prediction': 'You are not diabetic'}),200

    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return jsonify({'error': error_message}),500

@app.route('/')
def index():
    section = request.args.get('section', default=None)
    prediction = request.args.get('prediction', default=None)
    return render_template('index.html', section=section, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
