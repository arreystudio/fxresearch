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

### Ethical Considerations
Use of public data, proper citation, and transparent, reproducible workflow.