import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle
from extract_features import extract_features_from_url

# Load the dataset
df = pd.read_csv("phishing-detector 2\phishing-detector\dataset.csv")

# Apply the same feature extractor to all URLs
feature_data = df['URL'].apply(extract_features_from_url)
feature_df = pd.DataFrame(feature_data.tolist(), columns=[
    "not_facebook", "has_https", "has_@", "is_long_url", "has_login_or_secure"
])

# Set labels
X = feature_df
y = df['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Save the model
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("✅ Model trained on consistent features and saved.")
