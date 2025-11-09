# Chapter 3: Research Methodology

### Research Design
Quantitative time-series design using quarterly data (2013–2025), combining descriptive statistics, correlation analysis, regression, moderation, and structural break diagnostics.

### Data Sources
- KRAS financial statements (ROA, Net Income, cash flow components, firm characteristics).
- Bank Indonesia exchange rates (IDR/USD).
- IDX publications and market data.

### Variables and Measurement
- Dependent: ROA, Net Income, Cash Flow Volatility (CFV12Q).
- Independent: FX Volatility (ERVol12Q; alternatives include 3M/12M windows).
- Moderators: Hedging activity (Hedge), Leverage (DER), Size (Total Assets), Liquidity (Current Ratio).
- Controls: Firm characteristics and, where relevant, regime dummy (Post2020).

### Model Specification
Baseline OLS with HAC-robust SEs, plus moderation and regime-augmented models. Representative equation:

\\[ \text{Performance}_t = \alpha + \beta_1 \text{FXVol}_t + \beta_2 \text{Hedge}_t + \beta_3 (\text{FXVol}_t \times \text{Hedge}_t) + \beta_4 \text{Controls}_t + \epsilon_t \\]

Sensitivity checks include alternative volatility windows (3M, 12M), scaling, winsorization, subperiod splits (pre/post-2020), and Post2020 interactions.

### Data Analysis Techniques
- Descriptive statistics and visualization.
- Correlation analysis.
- Regression and moderation analysis.
- Structural break tests: CUSUM stability test; Chow test around 2020Q1.

### Validity and Reliability
- Multicollinearity: Variance Inflation Factors (VIF).
- Heteroskedasticity: Breusch–Pagan; HAC robust SEs.
- Autocorrelation: ACF/PACF; dynamic terms as diagnostics.

### Treatment of Non-Stationarity and Dynamic Specification
- Stationarity screening with ADF is applied to all continuous series (ROA, Net Income, ERVol12Q, CFV12Q, DER, lnTA, CR). Findings indicate CFV12Q and several controls are I(1) at level.
- To avoid spurious regression, models incorporate dynamics (lagged dependent variable) and quarterly time effects, and use HAC/Newey–West robust standard errors. Residual tests (Breusch–Godfrey up to 4 lags; Durbin–Watson ≈ 1.9–2.0) show minimal residual autocorrelation in dynamic specifications.
- Robustness checks include a first-difference model for CFV (ΔCFV12Q) and an Engle–Granger residual-based cointegration test between CFV12Q and the predictor set (ERVol12Q, DER, lnTA, CR, Hedge). EG rejects unit root in residuals (p ≈ 0.00077), supporting cointegration and validating level estimation with dynamics and robust SEs.
- Documentation and detailed outputs are consolidated in `Thesis/Tables/Diagnostics.md` (sources: `../Output/tables/03_adf_results.csv`, `../Output/tables/07_breusch_godfrey_*.csv`, `../Output/tables/07_cointegration_cfv12q.csv`).

### Ethical Considerations
Use of public data, proper citation, and transparent, reproducible workflow.