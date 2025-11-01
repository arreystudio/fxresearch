# PT Krakatau Steel (KRAS): FX Volatility, Hedging, and Firm Performance (2013–2025)

## Chapter 1: Introduction

### Background of the Study
Indonesia’s steel industry is a strategic pillar for national development, enabling infrastructure expansion, industrial manufacturing, and downstream value chains. KRAS, the largest integrated steel producer, relies on USD-denominated imports (raw materials, technology, and finance) while realizing most revenues in IDR, creating a natural foreign exchange (FX) exposure. Over 2013–2025, IDR/USD exhibited pronounced volatility, amplifying uncertainty in input costs and cash flow planning. Despite this, formal hedging adoption across state-owned and industrial sectors remains limited, reflecting constraints in policy frameworks, capabilities, and cost-benefit perceptions.

### Problem Statement
- How does FX volatility affect KRAS’s performance (ROA, Net Income) and cash-flow stability?
- Does hedging moderate these effects?
- How do firm characteristics (leverage, size, liquidity) influence these relationships?

### Research Objectives
- Examine the impact of FX volatility on firm performance and cash-flow volatility.
- Evaluate the role of hedging in mitigating FX risk.
- Analyze how leverage (DER), size (Total Assets), and liquidity (Current Ratio) shape these effects.

### Research Questions
- What is the relationship between FX volatility and firm performance at KRAS?
- Does hedging reduce cash flow volatility and performance fluctuations?
- How do leverage, firm size, and liquidity moderate these relationships?

### Significance of the Study
- Academic: contributes to understanding FX exposure in emerging markets.
- Practical: informs risk management and financial policy for KRAS and other SOEs.
- Policy: supports development of hedging frameworks for Indonesian state enterprises.

### Scope and Limitations
- Time frame: 2013–2025.
- Focus: PT Krakatau Steel (KRAS).
- Variables: FX volatility, hedging, ROA, Net Income, Cash Flow Volatility, firm characteristics.

---

## Chapter 2: Literature Review

### Foreign Exchange Exposure and Volatility
FX exposure commonly encompasses transaction, translation, and economic exposure. Economic exposure captures competitiveness shifts as exchange rates move. IDR/USD volatility affects input costs, pricing power, and financial outcomes for import-reliant firms like KRAS.

### Hedging and Risk Management
Hedging mitigates cash flow variability via financial instruments (forwards, swaps, options) and operational levers (currency matching, natural hedges). Firms hedge to reduce distress costs, align risk with risk appetite, and ease financing constraints.

### Firm Performance Indicators
ROA, Net Income, and Cash Flow Volatility (CFV) assess profitability and stability. Elevated FX volatility can compress margins and destabilize cash management.

### Firm Characteristics as Moderators
- Leverage (DER): heightens sensitivity to shocks.
- Size (Total Assets): improves access to tools and counterparties.
- Liquidity (Current Ratio): buffers working capital pressures.

### Empirical Studies and Research Gap
Global and regional evidence indicates FX volatility often negatively affects performance, while hedging dampens volatility. Yet, there is limited empirical synthesis linking FX volatility, hedging, and firm-specific moderators within Indonesia’s industrial SOEs. This study addresses that gap for KRAS.

---

## Chapter 3: Research Methodology

### Research Design
Quantitative, time-series design using quarterly KRAS data (2013–2025), integrating descriptive analytics, correlation, regression, moderation, and structural break diagnostics.

### Data Sources
Secondary sources include KRAS financial reports, Bank Indonesia exchange rates, and IDX publications.

### Variables and Measurement
- Dependent: ROA, Net Income, Cash Flow Volatility (CFV12Q).
- Independent: FX Volatility (ERVol12Q and alternates).
- Moderators: Hedging activity, Leverage (DER), Size (Total Assets), Liquidity (Current Ratio).
- Controls: Firm characteristics as above; optional regime dummy for post-2020.

### Model Specification
Baseline OLS with HAC-robust SEs and moderation terms. Representative equation:
\[\text{Performance}_t = \alpha + \beta_1 \text{FXVol}_t + \beta_2 \text{Hedge}_t + \beta_3 (\text{FXVol}_t \times \text{Hedge}_t) + \beta_4 \text{Controls}_t + \epsilon_t\]
Sensitivity includes alternative FX volatility windows (3M, 12M), scaling, winsorization, subperiod splits, regime dummy (Post2020), and interaction terms.

### Data Analysis Techniques
- Descriptive statistics and visualization.
- Correlation analysis.
- Regression and moderation analysis.
- Structural break tests (CUSUM; Chow around 2020Q1) and regime-augmented models.

### Validity and Reliability
- Multicollinearity: Variance Inflation Factors (VIF).
- Heteroskedasticity: Breusch–Pagan (ROA), HAC SEs.
- Autocorrelation: ACF/PACF; dynamic terms where relevant.

### Ethical Considerations
Use of public data, proper citation, and transparent, reproducible analysis.

---

## Chapter 4: Results and Discussion

### Descriptive Statistics
Key descriptive tables and figures are available:
- Summary stats: ../Output/tables/02_summary_stats.csv
- Correlation matrix: ../Output/tables/02_correlations.csv
- EDA figures: ROA, Net Income, CFV12Q, ERVol12Q
  - ![ROA](../Output/figures/02_eda_ROA.svg)
  - ![NetIncome](../Output/figures/02_eda_NetIncome.svg)
  - ![CFV12Q](../Output/figures/02_eda_CFV12Q.svg)
  - ![ERVol12Q](../Output/figures/02_eda_ERVol12Q.svg)

### Correlation Analysis
Correlation heatmaps indicate patterns between FX volatility, hedging, and performance metrics. See ../Output/figures/02_corr_heatmap.svg.

### Regression Results
- Baseline models: see ../Output/tables/04_roa_baseline_params.csv, ../Output/tables/04_netincome_baseline_params.csv, ../Output/tables/04_cfv_baseline_params.csv.
- Interaction models (FXVol × Hedge): ../Output/tables/05_roa_interaction_params.csv, ../Output/tables/05_netincome_interaction_params.csv, ../Output/tables/05_cfv_interaction_params.csv.
- Sensitivity and regime models: key outputs in ../Output/tables/* including post-2020 dummies and interactions.

Headline findings synthesized from ../Output/summaries/08_results_synthesis.md and ../Output/tables/08_key_effects.csv:
- FX volatility is positively associated with cash flow volatility (CFV12Q), with stronger effects post-2020.
- Hedging generally reduces CFV, though evidence for moderating effects on ROA and Net Income is weaker.
- ROA and Net Income show limited and mixed sensitivity to FX volatility once controls are included.

### Structural Breaks and Regime Effects
- CUSUM tests indicate stability for ROA and Net Income; CFV12Q exhibits a structural shift around 2020.
- Chow test at 2020Q1 supports a regime change in CFV12Q.
- Regime-dummy models (Post2020) and interactions confirm amplified FXVol→CFV link in the post-2020 period.

### Discussion
These results align with KRAS’s operational realities: USD-cost inputs expose cash flows to exchange-rate swings, and hedging helps dampen volatility. Performance measures are influenced by broader operational and macro factors, which may dilute direct FX impacts. Post-2020 dynamics (market stress, policy shifts) intensified exposure channels, underscoring the value of formalized hedging policies and liquidity buffers.

---

## Chapter 5: Conclusion and Recommendations

### Summary of Key Findings and Conclusions
- FX volatility materially increases cash flow volatility, especially post-2020.
- Hedging is effective in reducing cash flow instability; moderation of performance effects is modest.
- Leverage, size, and liquidity shape sensitivity to FX shocks, with stronger effects under higher leverage and lower liquidity.

### Implications
- Corporate: adopt a structured hedging program with risk limits, rolling horizons, and liquidity management.
- Policy: enable cost-effective access to hedging instruments for SOEs and promote governance around FX risk.

### Limitations
- Single-firm focus (KRAS); limited generalizability.
- Measurement constraints and potential omitted variables.
- Regime inference based on statistical diagnostics and available data granularity.

### Suggestions for Future Research
- Extend to cross-firm or multi-sector panels.
- Test additional moderators (governance, export ratio, covenant structure).
- Explore ARDL and rolling-window approaches for time-varying dynamics.

---

## Appendices (Selected Artifacts)
- Pre-estimation checks: ../Output/tables/03_adf_results.csv; ../Output/figures/03_acf_*.svg, ../Output/figures/03_pacf_*.svg
- Diagnostics: ../Output/tables/07_vif.csv; FE/Dynamic summaries in ../Output/models/07_*.
- Structural breaks: ../Output/tables/06_break_tests.csv; regime params in ../Output/tables/06_*_regime_*.csv.
- Synthesis and policy: ../Output/summaries/08_results_synthesis.md; ../Output/summaries/09_policy_implications.md