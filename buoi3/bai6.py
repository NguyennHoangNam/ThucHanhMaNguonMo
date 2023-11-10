import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Function to load data from a CSV or Excel file
def load_data(file_path):
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.xls') or file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    else:
        raise ValueError('Invalid file format. Only CSV and Excel files are supported.')

# Function to train a linear regression model
def train_linear_regression(X, y):
    model = LinearRegression()
    model.fit(X, y)
    return model

# Function to make predictions using a trained model
def predict(model, X):
    return model.predict(X)

# Main function
def main():
    # Prompt the user for the file path
    file_path = input("Enter the file path: ")

    # Load the data from the file
    data = load_data(file_path)

    # Prompt the user for the target column name
    target_column = input("Enter the target column name: ")

    # Split the data into features (X) and target variable (y)
    X = data.drop(target_column, axis=1)
    y = data[target_column]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a linear regression model
    model = train_linear_regression(X_train, y_train)

    # Make predictions on the test set
    y_pred = predict(model, X_test)

    # Print the predicted values
    print("Predicted values:")
    print(y_pred)

if __name__ == '__main__':
    main()
