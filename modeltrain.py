import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
import joblib
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

# Load the dataset
data = pd.read_csv("finaldataset.csv")

# Separate features and target variable
X = data.drop("diabetes", axis=1)
y = data["diabetes"]

# Apply one-hot encoding to categorical variables
X_encoded = pd.get_dummies(X, drop_first=True)

# Impute missing values
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X_encoded)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_imputed, y, test_size=0.2, random_state=42)

# Initialize and train the Random Forest Classifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, "trainmodel.joblib")

# Define the column names used for predictions
columns = X.columns.tolist()

print("score: ",model.score(X_test,y_test))

y_pred_over = model.predict(X_test)

print("Classification report: ")
print(classification_report(y_test, y_pred_over))