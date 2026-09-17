import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, PolynomialFeatures
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error


# 1. LOAD DATA
df = pd.read_csv("plant_loving.csv")

# 2. FEATURES AND TARGET

features = [
    "plant_number",
    "plant_diversity",
    "rare_exotic",
    "plant_type"
]

target = "PLS"

X = df[features]
y = df[target]


# 3. DEFINE VARIABLE TYPES

numeric_features = [
    "plant_number",
    "plant_diversity",
    "rare_exotic"
]

categorical_features = [
    "plant_type"
]

# 4. PREPROCESSING

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(
                handle_unknown="ignore",
                drop="first"
            ),
            categorical_features
        )
    ],
    remainder="passthrough"
)


# 5. TRAIN / TEST SPLIT


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# 6. DEFINE MODELS


models = {

    "Linear Regression": Pipeline([
        ("preprocessing", preprocessor),
        ("model", LinearRegression())
    ]),

    "Polynomial Regression": Pipeline([
        ("preprocessing", preprocessor),
        (
            "polynomial",
            PolynomialFeatures(
                degree=2,
                include_bias=False
            )
        ),
        ("model", LinearRegression())
    ]),

    "Decision Tree": Pipeline([
        ("preprocessing", preprocessor),
        (
            "model",
            DecisionTreeRegressor(
                max_depth=6,
                random_state=42
            )
        )
    ]),

    "Random Forest": Pipeline([
        ("preprocessing", preprocessor),
        (
            "model",
            RandomForestRegressor(
                n_estimators=300,
                max_depth=8,
                min_samples_leaf=2,
                random_state=42
            )
        )
    ]),

    "Gradient Boosting": Pipeline([
        ("preprocessing", preprocessor),
        (
            "model",
            GradientBoostingRegressor(
                n_estimators=200,
                learning_rate=0.05,
                max_depth=3,
                random_state=42
            )
        )
    ])
}


# 7. TRAIN AND EVALUATE

results = []

for name, model in models.items():

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)

    mae = mean_absolute_error(
        y_test,
        y_pred
    )

    rmse = np.sqrt(
        mean_squared_error(
            y_test,
            y_pred
        )
    )

    results.append({
        "Model": name,
        "R2": r2,
        "MAE": mae,
        "RMSE": rmse
    })


# 8. RESULTS TABLE

results_df = pd.DataFrame(results)

results_df = results_df.sort_values(
    by="R2",
    ascending=False
)

print("\nMODEL PERFORMANCE")
print(  results_df.to_string(
        index=False,
        float_format=lambda x: f"{x:.4f}"
    )
)
 #9 NEW SAMPLE

new_sample = pd.DataFrame({
    "plant_number": [15],
    "plant_diversity": [7],
    "rare_exotic": [1],
    "plant_type": ["Succulent"]
})

# 10. PREDICT PLS USING ALL MODELS

for name, model in models.items():
    predicted_pls = model.predict(new_sample)[0]
    print(f"{name}: {predicted_pls:.2f}")

# 11. PREDICT CATEGORY
def get_pls_category(pls):
    if pls <= 20:
        return "Novice"
    elif pls <= 40:
        return "Occasional"
    elif pls <= 60:
        return "Enthusiast"
    elif pls <= 80:
        return "Passionate"
    else:
        return "Avid"

for name, model in models.items():
    predicted_pls = model.predict(new_sample)[0]    
    category = get_pls_category( predicted_pls )
    print( f"{name}: {category}")
