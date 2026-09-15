# Employee Attrition Analysis

**Business question:** Which employees are most likely to leave, and what should the company
do about it before it shows up as a resignation?

A 1,200-employee dataset (department, tenure, salary, satisfaction, overtime, commute,
performance) analysed with Python/pandas to find the strongest drivers of attrition and turn
them into a targeted retention recommendation, instead of a blanket "improve engagement" memo.

## Key findings

- **Overall attrition sits at 13.9%.** Employees working overtime leave at **21.4%**, roughly
  **2x** the rate of those who don't (10.5%) — the single strongest driver in the data.
- **Attrition is heavily front-loaded**: **45.5%** of everyone who left did so within their
  first 2 years of tenure. Retention risk is highest right after onboarding, not after years
  of service.
- **Operations (17.5%) and HR (16.5%)** have the highest attrition rates, well above
  Marketing (10.0%) and Engineering (12.0%) — this is not a company-wide problem, it's
  concentrated in specific teams.
- **Low job satisfaction (score 1) correlates with 16.0% attrition** vs. **11.0%** for the
  most satisfied employees (score 5) — a real but smaller effect than overtime, suggesting
  workload is a more direct lever than sentiment alone.
- Salary and commute distance show only weak standalone effects once overtime and satisfaction
  are accounted for — cutting the org's retention budget straight to "pay more" would miss
  the bigger driver.
- **103 currently-employed people** are working overtime *and* report low satisfaction —
  this is the actionable at-risk list, not a theoretical segment.

## Recommendation

Prioritise a retention intervention on the **103 flagged employees** (overtime + low
satisfaction) before their tenure crosses the 2-year mark, with Operations and HR as the
first departments to review workload distribution. This targets the group carrying the
highest combined risk rather than spreading a generic engagement survey across the whole
company.

## Charts

| Chart | Insight |
|---|---|
| `charts/attrition_by_department.png` | Where attrition is concentrated |
| `charts/attrition_by_overtime.png` | The single strongest driver |
| `charts/attrition_by_satisfaction.png` | Satisfaction's effect on attrition |
| `charts/tenure_distribution.png` | Attrition is a first-2-years problem |

## How it was built

```
pip install pandas matplotlib numpy
python generate_data.py   # synthesises a realistic 1,200-row HR dataset
python analysis.py        # runs the analysis, saves 4 charts to /charts
```

**Note on the dataset:** synthesised for this project (real HR data is confidential), but built
with realistic distributions and deliberately-embedded relationships (overtime, satisfaction,
and tenure genuinely drive the simulated attrition outcome) so the analysis technique,
findings, and recommendation process reflect real analyst work.

## Tools

Python · pandas · matplotlib · statistical grouping/aggregation (the pandas equivalent of SQL
`GROUP BY` + `AVG`)

## Author

Suhana Shaikh · [Portfolio](https://shaikhsuhana.github.io/suhana-portfolio) ·
[GitHub](https://github.com/shaikhsuhana)
