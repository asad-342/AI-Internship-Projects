import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.tree import plot_tree

print("=" * 60)
print("🌺 IRIS FLOWER CLASSIFICATION 🌺")
print("=" * 60)

# ==========================================
# STEP 1: LOAD DATASET
# ==========================================

print("\n📊 Loading the dataset...")
iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
df['target_name'] = df['target'].apply(lambda x: iris.target_names[x])

print(f"\n✅ Dataset shape: {df.shape}")
print("\n📋 First 5 rows:")
print(df.head())

print("\n🎯 Target classes:")
print(f"   0 = {iris.target_names[0]}")
print(f"   1 = {iris.target_names[1]}")
print(f"   2 = {iris.target_names[2]}")

# ==========================================
# STEP 2: SPLIT DATA (80% TRAIN, 20% TEST)
# ==========================================

print("\n📊 Splitting data...")

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"✅ Training: {len(X_train)} samples")
print(f"✅ Testing: {len(X_test)} samples")

# ==========================================
# STEP 3: TRAIN MODEL
# ==========================================

print("\n📊 Training model...")

model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)

print("✅ Model trained!")

# ==========================================
# STEP 4: MAKE PREDICTIONS
# ==========================================

print("\n📊 Making predictions...")

y_pred = model.predict(X_test)

print("✅ Predictions complete!")

# ==========================================
# STEP 5: EVALUATE PERFORMANCE
# ==========================================

print("\n📊 Evaluating performance...")

accuracy = accuracy_score(y_test, y_pred)
print(f"\n🎯 Accuracy: {accuracy * 100:.2f}%")

print("\n📋 Classification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

print("\n📋 Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# ==========================================
# STEP 6: VISUALIZE DECISION TREE
# ==========================================

print("\n📊 Visualizing Decision Tree...")

plt.figure(figsize=(12, 8))
plot_tree(model, feature_names=iris.feature_names, 
          class_names=iris.target_names, filled=True, rounded=True)
plt.title("Decision Tree for Iris Classification")
plt.savefig("decision_tree.png")
print("✅ Saved as 'decision_tree.png'")
plt.show()

# ==========================================
# STEP 7: FEATURE IMPORTANCE
# ==========================================

print("\n📊 Feature Importance...")

feature_importance = pd.DataFrame({
    'Feature': iris.feature_names,
    'Importance': model.feature_importances_
}).sort_values('Importance', ascending=False)

print(feature_importance)

plt.figure(figsize=(8, 5))
plt.barh(feature_importance['Feature'], feature_importance['Importance'])
plt.xlabel('Importance')
plt.title('Feature Importance for Iris Classification')
plt.tight_layout()
plt.savefig("feature_importance.png")
print("✅ Saved as 'feature_importance.png'")
plt.show()

# ==========================================
# STEP 8: TEST WITH NEW SAMPLE
# ==========================================

print("\n📊 Testing with a new sample...")

new_sample = [[5.1, 3.5, 1.4, 0.2]]
prediction = model.predict(new_sample)
predicted_flower = iris.target_names[prediction[0]]

print(f"\n🌺 Sample: {new_sample[0]}")
print(f"🌸 Predicted: {predicted_flower}")

print("\n" + "=" * 60)
print("🎉 PROJECT COMPLETE! 🎉")
print("=" * 60)
