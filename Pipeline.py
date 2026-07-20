import pandas as pd

# Step 1: Load dataset
df = pd.read_csv("telecom_churn.csv")   # apna dataset yahan rakho
print("Original Data:")
print(df.head())

# Step 2: Cleaning
df['DataUsage'] = df['DataUsage'].fillna(df['DataUsage'].mean())   # missing values handle
df.drop_duplicates(inplace=True)                                   # duplicates remove
df['ContractRenewal'] = df['ContractRenewal'].astype(int)          # datatype fix
df['DataPlan'] = df['DataPlan'].astype(int)
df['Churn'] = df['Churn'].map({0:'No', 1:'Yes'})                   # churn encode

# Step 3: Save cleaned dataset
df.to_csv("telecom_churn_clean.csv", index=False)
print("Cleaned dataset saved successfully!")
# Step 4: Exploratory Data Analysis (EDA)
import seaborn as sns
import matplotlib.pyplot as plt

df_numeric = df.select_dtypes(include=['int64','float64'])

plt.figure(figsize=(10,6))
sns.heatmap(df_numeric.corr(), annot=True, cmap="coolwarm")
plt.show()

# Step 5: Feature Engineering
df['TenureBucket'] = pd.cut(df['AccountWeeks'], bins=[0,50,100,150], labels=['Short','Medium','Long'])
df['AvgMonthlyUsage'] = df['DataUsage'] / df['AccountWeeks']
df = pd.get_dummies(df, drop_first=True)

# Step 6: Model Building & Evaluation
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# Features (X) aur Target (y) define karo
    y = df[target_col]
    X = df.drop(target_col, axis=1)
else:
    print("Target column not found. Available columns:", df.columns)# Features (X) aur Target (y) define karo
y = df['Churn_Yes']   # target column
X = df.drop('Churn_Yes', axis=1)   # baaki sab features

# Train/Test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

 
# Train/Test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Logistic Regression model train karo
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
import seaborn as sns
import matplotlib.pyplot as plt

cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()
from sklearn.metrics import roc_curve, auc

y_prob = model.predict_proba(X_test)[:,1]
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}")
plt.plot([0,1],[0,1],'--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.show()




