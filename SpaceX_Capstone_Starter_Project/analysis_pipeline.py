import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, f1_score, jaccard_score, classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
import urllib.request

URL = "https://raw.githubusercontent.com/IslamSaqer/Applied-Data-Science-Capstone/main/spacex_launch_dash.csv"
DATA = Path("spacex_launch_dash.csv")

if not DATA.exists():
    print("Downloading attributed public course dataset...")
    urllib.request.urlretrieve(URL, DATA)

df = pd.read_csv(DATA)
df.columns = [c.strip() for c in df.columns]
target = "class"
if target not in df.columns:
    raise ValueError(f"Expected target column '{target}'. Found: {list(df.columns)}")

# Select only fields available in the dashboard snapshot.
candidate_features = ["Launch Site", "Payload Mass (kg)", "Booster Version Category"]
features = [c for c in candidate_features if c in df.columns]
X, y = df[features].copy(), df[target].astype(int)

numeric = [c for c in features if pd.api.types.is_numeric_dtype(X[c])]
categorical = [c for c in features if c not in numeric]
numeric_pipe = Pipeline([("imputer", SimpleImputer(strategy="median")), ("scale", StandardScaler())])
categorical_pipe = Pipeline([("imputer", SimpleImputer(strategy="most_frequent")),
                             ("onehot", OneHotEncoder(handle_unknown="ignore"))])
prep = ColumnTransformer([("num", numeric_pipe, numeric), ("cat", categorical_pipe, categorical)])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

models = {
    "Logistic Regression": LogisticRegression(max_iter=2000),
    "SVM": SVC(),
    "Decision Tree": DecisionTreeClassifier(random_state=42, max_depth=4),
    "KNN": KNeighborsClassifier(n_neighbors=5)
}

print("\\nDATA SUMMARY")
print("Rows:", len(df), "| Columns:", len(df.columns))
print("Landing class counts:\\n", y.value_counts().sort_index())
print("Landing success rate:", round(y.mean() * 100, 1), "%")
if "Payload Mass (kg)" in df:
    print("Average payload mass:", round(df["Payload Mass (kg)"].mean(), 1), "kg")
if "Launch Site" in df:
    print("Launch-site counts:\\n", df["Launch Site"].value_counts())

print("\\nMODEL EVALUATION (your results may differ from published source results)")
for name, estimator in models.items():
    pipe = Pipeline([("preprocess", prep), ("model", estimator)])
    pipe.fit(X_train, y_train)
    pred = pipe.predict(X_test)
    print(f"\\n{name}")
    print("Accuracy:", round(accuracy_score(y_test, pred), 4))
    print("F1:", round(f1_score(y_test, pred, zero_division=0), 4))
    print("Jaccard:", round(jaccard_score(y_test, pred, zero_division=0), 4))
    print("Confusion matrix:\\n", confusion_matrix(y_test, pred))
    print(classification_report(y_test, pred, zero_division=0))
