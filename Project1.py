import pandas as pd

# Read the real financial data
df = pd.read_csv("uk_supermarkets.csv")

# First look
print("The full dataset:")
print(df)

print("\nShape (rows, columns):", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nCompanies in the data:")
print(df["company"].value_counts())

# CALCULATED COLUMNS - the heart of financial analysis
df["gross_margin_pct"] = (df["gross_profit_m"] / df["revenue_m"]) * 100
df["operating_margin_pct"] = (df["operating_profit_m"] / df["revenue_m"]) * 100

# Show the data with the new metrics
print("\nData with margins calculated:")
print(df[["company", "fiscal_year", "revenue_m", "gross_margin_pct", "operating_margin_pct"]].round(2))

# Average margins by company (who runs the most profitable model?)
print("\nAverage margins by company:")
print(df.groupby("company")[["gross_margin_pct", "operating_margin_pct"]].mean().round(2))

# Revenue growth: each company's 2025 vs 2022
print("\nRevenue growth 2022 to 2025:")
growth = df.groupby("company").agg(
    revenue_2022=("revenue_m", "first"),
    revenue_2025=("revenue_m", "last")
)
growth["growth_pct"] = ((growth["revenue_2025"] - growth["revenue_2022"]) / growth["revenue_2022"] * 100).round(2)
print(growth)

# QUESTION 1: Best and worst operating margin year per company
print("\nBest operating margin year per company:")
best_year = df.loc[df.groupby("company")["operating_margin_pct"].idxmax()]
print(best_year[["company", "fiscal_year", "operating_margin_pct"]].round(2))

print("\nWorst operating margin year per company:")
worst_year = df.loc[df.groupby("company")["operating_margin_pct"].idxmin()]
print(worst_year[["company", "fiscal_year", "operating_margin_pct"]].round(2))

# QUESTION 2: Year-on-year revenue growth for every step
df = df.sort_values(["company", "fiscal_year"])
df["revenue_yoy_growth_pct"] = (df.groupby("company")["revenue_m"].pct_change() * 100).round(2)

print("\nYear-on-year revenue growth:")
print(df[["company", "fiscal_year", "revenue_m", "revenue_yoy_growth_pct"]])
import matplotlib.pyplot as plt

# ============================================================
# CHART 1: Average margins by company (comparison view)
# ============================================================
avg_margins = df.groupby("company")[["gross_margin_pct", "operating_margin_pct"]].mean().round(2)

avg_margins.plot(
    kind="bar",
    figsize=(10, 6),
    color=["#1f77b4", "#ff7f0e"],
    edgecolor="black"
)
plt.title("Average Profit Margins: UK Supermarkets, FY2022-FY2025", fontsize=13, fontweight="bold")
plt.ylabel("Margin (%)")
plt.xlabel("")
plt.xticks(rotation=0)
plt.legend(["Gross Margin", "Operating Margin"])
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("chart_avg_margins.png", dpi=150)
plt.show()

# ============================================================
# CHART 2: Revenue trend over time (time-series view)
# ============================================================
fig, ax = plt.subplots(figsize=(10, 6))

for company in df["company"].unique():
    company_data = df[df["company"] == company].sort_values("fiscal_year")
    ax.plot(
        company_data["fiscal_year"],
        company_data["revenue_m"],
        marker="o",
        linewidth=2,
        label=company
    )

ax.set_title("Revenue Trend: UK Supermarkets, FY2022-FY2025", fontsize=13, fontweight="bold")
ax.set_xlabel("Fiscal Year")
ax.set_ylabel("Revenue (£ millions)")
ax.legend()
ax.grid(alpha=0.3)
ax.set_xticks(df["fiscal_year"].unique())
plt.tight_layout()
plt.savefig("chart_revenue_trend.png", dpi=150)
plt.show()