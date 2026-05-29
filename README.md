# UK Supermarket Financial Analysis (FY2022–FY2025)

A four-year financial deep-dive comparing **Tesco**, **Sainsbury's** and **Marks & Spencer**
across profitability, growth, and margin trends. Built in Python with pandas and matplotlib.

## Key Findings

- **All three retailers hit their worst operating margin in FY2023** — Tesco at 2.27%,
  Sainsbury's at 1.78%, M&S at 4.69%. The UK cost-of-living and input-cost crunch shows
  up as a synchronised sector-wide trough in the data.

- **Marks & Spencer operates a fundamentally different business model.** Its average gross
  margin (~34%) is roughly five times that of the grocers (~7%), reflecting its clothing
  and premium-food mix. But operating margin is only ~5%, narrowing the gap dramatically —
  the cost base behind that headline margin is large.

- **Tesco out-converts Sainsbury's despite similar gross margins.** Tesco averages 3.69%
  operating margin vs Sainsbury's 2.76% on near-identical gross margins (~7%). Scale
  efficiency, not pricing power, is doing the work.

- **M&S grew revenue fastest** at +27% over the four years (Tesco +14%, Sainsbury's +10%),
  recovering from its FY2022 base into a stronger post-pandemic position.

## Method

- Source: statutory financials per Yahoo Finance, cross-checkable against each company's
  annual report
- Tools: Python 3.13, pandas, matplotlib
- Period: FY2022–FY2025 (fiscal year-ends: Tesco/Sainsbury's February, M&S March)

## Files

- `uk_supermarkets.csv` — source dataset
- `project1.py` — full analysis script
- `chart_avg_margins.png` — bar chart of average margins by company
- `chart_revenue_trend.png` — line chart of revenue trajectory

## Limitations

- Statutory figures only; segment-level analysis would require deeper breakdowns from
  each annual report
- Fiscal-year offsets (Feb vs Mar) introduce minor noise into year-on-year comparisons
- Operating margin uses headline operating profit; restructuring charges and exceptional
  items would refine the picture