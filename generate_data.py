import numpy as np
import pandas as pd

np.random.seed(42)
n = 1200

departments = ["Sales", "Engineering", "Customer Support", "Marketing", "Operations", "HR"]
dept_weights = [0.22, 0.25, 0.18, 0.12, 0.15, 0.08]

df = pd.DataFrame({
    "employee_id": [f"E{1000+i}" for i in range(n)],
    "department": np.random.choice(departments, n, p=dept_weights),
    "age": np.random.randint(21, 60, n),
    "tenure_years": np.round(np.random.exponential(3, n), 1).clip(0.1, 20),
    "monthly_salary": np.random.normal(55000, 15000, n).clip(18000, 150000).round(-2),
    "commute_km": np.random.exponential(12, n).clip(1, 60).round(1),
    "overtime": np.random.choice(["Yes", "No"], n, p=[0.32, 0.68]),
    "job_satisfaction": np.random.randint(1, 6, n),   # 1-5
    "work_life_balance": np.random.randint(1, 6, n),  # 1-5
    "last_promotion_years": np.random.exponential(2.5, n).clip(0, 15).round(1),
    "performance_rating": np.random.choice([1,2,3,4,5], n, p=[0.03,0.10,0.42,0.35,0.10]),
    "training_hours_last_year": np.random.poisson(18, n),
})

# Department pay adjustment (Sales/Engineering pay more)
dept_adj = {"Sales": 1.05, "Engineering": 1.25, "Customer Support": 0.85, "Marketing": 0.95, "Operations": 0.90, "HR": 0.92}
df["monthly_salary"] = (df["monthly_salary"] * df["department"].map(dept_adj)).round(-2)

# Build attrition probability from realistic drivers
logit = (
    -2.4
    + 1.15 * (df["overtime"] == "Yes")
    + 0.55 * (df["job_satisfaction"] <= 2)
    + 0.45 * (df["work_life_balance"] <= 2)
    - 0.35 * (df["tenure_years"] > 5)
    + 0.40 * (df["commute_km"] > 25)
    + 0.30 * (df["last_promotion_years"] > 4)
    - 0.30 * (df["monthly_salary"] > df["monthly_salary"].median())
    + 0.25 * (df["department"] == "Customer Support")
    + 0.20 * (df["department"] == "Sales")
    - 0.02 * df["training_hours_last_year"]
    + np.random.normal(0, 0.5, n)
)
prob = 1 / (1 + np.exp(-logit))
df["attrition"] = np.where(np.random.random(n) < prob, "Yes", "No")

df.to_csv("/home/claude/projects/hr-attrition/data/hr_attrition.csv", index=False)
print(df["attrition"].value_counts(normalize=True))
print(df.shape)
