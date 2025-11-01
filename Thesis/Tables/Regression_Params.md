# Consolidated Regression Parameters

This table consolidates top coefficients for ROA, NetIncome, and CFV across baseline (04_*), interaction (05_*), sensitivity (06_* alt FX windows), and regime models (06_*_regime*).

## ROA

- Baseline (ERVol12Q): estimate=0.8981, se=0.3846, p=0.0195
- Baseline (Hedge): estimate=-0.0032, se=0.0171, p=0.8508
- Interaction (ERVol12Q): estimate=0.8228, se=0.4196, p=0.0499
- Interaction (ERVol12Q_Hedge): estimate=0.6166, se=1.2141, p=0.6115
- Sensitivity (ERVolM3M): estimate=1.0327, se=0.6222, p=0.0970
- Sensitivity (ERVolM12M): estimate=0.4864, se=0.6118, p=0.4266
- Regime (Post2020): estimate=0.0228, se=0.0129, p=0.0777

## NetIncome

- Baseline (ERVol12Q): estimate=3,046,026.52, se=1,280,608.67, p=0.0174
- Baseline (Hedge): estimate=-10,439.11, se=53,753.35, p=0.8460
- Interaction (ERVol12Q): estimate=2,855,020.49, se=1,421,305.39, p=0.0446
- Interaction (ERVol12Q_Hedge): estimate=1,564,974.01, se=3,704,660.99, p=0.6727
- Sensitivity (ERVolM3M): estimate=3,274,951.45, se=1,929,254.42, p=0.0896
- Sensitivity (ERVolM12M): estimate=1,587,824.18, se=1,939,406.43, p=0.4129
- Regime (Post2020): estimate=86,286.52, se=46,610.15, p=0.0641

## CFV12Q

- Baseline (ERVol12Q): estimate=0.0389, se=0.0952, p=0.6824
- Baseline (Hedge): estimate=0.0057, se=0.0041, p=0.1612
- Interaction (ERVol12Q): estimate=-0.0694, se=0.0450, p=0.1234
- Interaction (ERVol12Q_Hedge): estimate=0.8875, se=0.1434, p=0.0000000006102
- Sensitivity (ERVolM3M): estimate=0.1147, se=0.0660, p=0.0823
- Sensitivity (ERVolM12M): estimate=0.0896, se=0.1134, p=0.4294
- Regime (ERVol12Q): estimate=0.2118, se=0.0842, p=0.0119
- Regime (Post2020): estimate=-0.0126, se=0.0025, p=0.0000003345
- Regime Interaction (ERVol12Q_Post2020): estimate=-0.3505, se=0.1399, p=0.0123

Notes:
- Values are rounded for readability and drawn from the latest CSV outputs in ../Output/tables/. See individual CSV files for full parameter sets and additional controls.
- CFV regime and interaction results highlight stronger FX volatility linkage and a significant structural adjustment post-2020.