# Foreign Exchange Risk Management and Its Impact on Financial Performance in Indonesia Steel Industry: A Case Study of PT Krakatau Steel (Persero) Tbk

## Background and Rationale
Indonesia’s steel industry underpins national development, with demand driven by infrastructure and urbanization. Firms, including PT Krakatau Steel (KRAS), rely heavily on imported inputs priced in USD while most revenues are in IDR, creating a structural FX mismatch. Over 2013–2025, IDR/USD exhibited pronounced volatility. KRAS reported losses in several years amid FX pressures and rising input costs. Formal hedging adoption in Indonesia’s industrial/state sectors remains limited. This study examines whether FX volatility and hedging are associated with firm performance and cash-flow stability at KRAS.

## Research Questions
1) How does FX volatility affect KRAS’s ROA, Net Income, and Cash Flow Volatility?  
2) Does the existence of hedging activities affect ROA, Net Income, and Cash Flow Volatility?  
3) How do firm characteristics (leverage/DER, size/Total Assets, liquidity/Current Ratio) shape these relationships?

## Hypotheses
- H1: FX volatility negatively affects ROA.  
- H2: FX volatility negatively affects Net Income.  
- H3: FX volatility positively affects Cash Flow Volatility.  
- H4: Hedging (existence) positively affects ROA.  
- H5: Hedging positively affects Net Income.  
- H6: Hedging negatively affects Cash Flow Volatility.  
- H7: Leverage, size, and liquidity significantly affect performance.

## Data and Variables
Source: `/Volumes/Rey/roa/EViews Test.csv` (quarterly, 2013Q1–2025Q2). Columns used:
- Quarter: period index.
- ROA: profitability ratio.
- NetIncome: quarterly net profit (IDR).
- CFV12Q: 12-quarter rolling cash-flow volatility.
- ERVol12Q: 12-quarter rolling IDR/USD volatility.
- DER: Debt-to-Equity Ratio.
- lnTA: natural log of Total Assets.
- CR: Current Ratio.
- Hedge: 0/1 indicator for hedging existence.
- ERVolM3M, ERVolM12M: alternative volatility windows (3-month and 12-month).

Operational definitions align with corporate finance conventions: FX volatility via rolling standard deviation of log exchange-rate changes; hedging as binary presence; ROA ≈ Net Income / Total Assets; CF volatility as rolling SD; DER = Debt/Equity; size proxied by ln(TA); liquidity via Current Ratio.

## Methodology
Design: Single-firm, quarterly time-series analysis (2013–2025).

Main models (estimated separately):
1) ROA_t = α + β1·ERVol_t + β2·Hedge_t + γ·Controls_t + ε_t
2) NetIncome_t = α + β1·ERVol_t + β2·Hedge_t + γ·Controls_t + ε_t
3) CFV12Q_t = α + β1·ERVol_t + β2·Hedge_t + γ·Controls_t + ε_t

Where Controls_t = {DER_t, lnTA_t, CR_t}. We will also test interaction effects:
- ERVol × Hedge to assess whether hedging mitigates volatility’s impact.

Estimation and diagnostics:
- OLS with robust (Newey–West/HAC) standard errors to address heteroskedasticity and autocorrelation.
- Stationarity checks (ADF) for key series; difference or detrend if needed (e.g., NetIncome may be scaled/logged). 
- Autocorrelation tests (Durbin–Watson/ACF), heteroskedasticity tests (Breusch–Pagan), multicollinearity (VIF). 
- Model fit and inference via adjusted R², F-tests, and coefficient t-tests. 
- Sensitivity: alternative volatility windows (ERVolM3M, ERVolM12M vs ERVol12Q); alternative scaling of NetIncome (e.g., per assets) and ROA definition; winsorization to reduce outlier influence; subperiods (pre-2020 vs post-2020).

Robustness extensions:
- Add quarter dummies (seasonality). 
- Use AR terms or ARDL if residual autocorrelation persists. 
- Consider dynamic specifications (lagged dependent variable) where economically justified.

Interpretation:
- Sign and significance of β1 (FX volatility) and β2 (Hedge) across models. 
- If ERVol × Hedge interaction is significant and negative (for ROA/NetIncome models), it suggests hedging mitigates adverse FX effects.

## What We Should Do (Step-by-Step)
1) Data intake and cleaning: verify types, missing values, and consistency of CSV; confirm units and scaling. 
2) Descriptive analysis: summary stats, time-series plots for ROA, NetIncome, ERVol, CFV12Q, Hedge; correlation matrix. 
3) Pre-estimation checks: stationarity (ADF), autocorrelation (ACF/PACF), heteroskedasticity (visual and tests). 
4) Baseline regressions: estimate models (1)–(3) with ERVol12Q, Hedge, and controls; compute HAC robust SEs. 
5) Interaction analysis: add ERVol × Hedge; assess mitigation effects. 
6) Sensitivity: re-estimate with ERVolM3M and ERVolM12M; try alternative scaling (e.g., NetIncome/TA), winsorization, and subperiod splits. 
7) Diagnostics and refinement: check residuals, multicollinearity (VIF), re-specify (lags/quarter FE) as needed. 
8) Results synthesis: tables of coefficients, SEs, fit metrics; concise narrative on findings vs hypotheses. 
9) Policy and managerial implications: translate results into risk-management recommendations for KRAS. 
10) Write-up: finalize figures, tables, and conclusions.

## Expected Outputs
- Clean dataset and EDA visuals.
- Regression tables (baseline, interaction, sensitivity). 
- Interpretation of ERVol and Hedge effects on ROA, NetIncome, and CFV. 
- Practical recommendations for hedging and liquidity/leverage management.

## Limitations
Single-firm case limits generalizability; potential measurement error in hedging indicator; structural breaks (e.g., 2020) may complicate inference; limited availability of detailed hedge ratios.