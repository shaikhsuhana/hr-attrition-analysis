import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'DejaVu Sans'

df = pd.read_csv("/home/claude/projects/hr-attrition/data/hr_attrition.csv")

CORAL = "#E8622A"
SAND = "#C9B99A"
DARK = "#2C2417"

# ---- 1. Attrition rate by department ----
dept_rate = (df.groupby("department")["attrition"]
             .apply(lambda x: (x == "Yes").mean() * 100)
             .sort_values(ascending=False))

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.barh(dept_rate.index[::-1], dept_rate.values[::-1], color=CORAL)
ax.set_xlabel("Attrition rate (%)")
ax.set_title("Attrition rate by department", fontsize=13, fontweight="bold")
for bar, val in zip(bars, dept_rate.values[::-1]):
    ax.text(val + 0.3, bar.get_y() + bar.get_height()/2, f"{val:.1f}%", va="center", fontsize=9)
ax.spines[['top','right']].set_visible(False)
plt.tight_layout()
plt.savefig("/home/claude/projects/hr-attrition/charts/attrition_by_department.png", dpi=150)
plt.close()

# ---- 2. Attrition rate: overtime vs no overtime ----
ot_rate = (df.groupby("overtime")["attrition"]
           .apply(lambda x: (x == "Yes").mean() * 100))
fig, ax = plt.subplots(figsize=(5, 5))
ax.bar(ot_rate.index, ot_rate.values, color=[SAND, CORAL])
ax.set_ylabel("Attrition rate (%)")
ax.set_title("Attrition rate: overtime vs. no overtime", fontsize=12, fontweight="bold")
for i, val in enumerate(ot_rate.values):
    ax.text(i, val + 0.4, f"{val:.1f}%", ha="center", fontsize=10, fontweight="bold")
ax.spines[['top','right']].set_visible(False)
plt.tight_layout()
plt.savefig("/home/claude/projects/hr-attrition/charts/attrition_by_overtime.png", dpi=150)
plt.close()

# ---- 3. Attrition rate by job satisfaction ----
sat_rate = (df.groupby("job_satisfaction")["attrition"]
            .apply(lambda x: (x == "Yes").mean() * 100))
fig, ax = plt.subplots(figsize=(6, 5))
ax.plot(sat_rate.index, sat_rate.values, marker="o", color=CORAL, linewidth=2)
ax.set_xlabel("Job satisfaction score (1=low, 5=high)")
ax.set_ylabel("Attrition rate (%)")
ax.set_title("Attrition rate falls as satisfaction rises", fontsize=12, fontweight="bold")
ax.set_xticks([1,2,3,4,5])
ax.spines[['top','right']].set_visible(False)
plt.tight_layout()
plt.savefig("/home/claude/projects/hr-attrition/charts/attrition_by_satisfaction.png", dpi=150)
plt.close()

# ---- 4. Tenure distribution: stayed vs left ----
fig, ax = plt.subplots(figsize=(7, 5))
ax.hist(df[df.attrition=="No"]["tenure_years"], bins=20, alpha=0.6, label="Stayed", color=SAND, density=True)
ax.hist(df[df.attrition=="Yes"]["tenure_years"], bins=20, alpha=0.7, label="Left", color=CORAL, density=True)
ax.set_xlabel("Tenure (years)")
ax.set_ylabel("Density")
ax.set_title("Attrition is concentrated in the first 2-3 years", fontsize=12, fontweight="bold")
ax.legend()
ax.spines[['top','right']].set_visible(False)
plt.tight_layout()
plt.savefig("/home/claude/projects/hr-attrition/charts/tenure_distribution.png", dpi=150)
plt.close()

# ---- Key numbers for README ----
overall = (df.attrition == "Yes").mean() * 100
top_dept = dept_rate.index[0]
top_dept_val = dept_rate.iloc[0]
ot_yes = ot_rate["Yes"]
ot_no = ot_rate["No"]
sat_low = sat_rate.loc[1]
sat_high = sat_rate.loc[5]
early_tenure_share = (df[(df.attrition=="Yes")]["tenure_years"] <= 2).mean() * 100
n_high_risk = ((df.overtime=="Yes") & (df.job_satisfaction<=2) & (df.attrition=="No")).sum()

print(f"Overall attrition: {overall:.1f}%")
print(f"Top department: {top_dept} at {top_dept_val:.1f}%")
print(f"Overtime Yes: {ot_yes:.1f}% vs No: {ot_no:.1f}%")
print(f"Satisfaction 1: {sat_low:.1f}% vs Satisfaction 5: {sat_high:.1f}%")
print(f"Share of leavers with <=2yr tenure: {early_tenure_share:.1f}%")
print(f"Currently-employed high-risk (overtime + low satisfaction) headcount: {n_high_risk}")
