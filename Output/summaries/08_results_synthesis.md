# Results Synthesis

Key effects (ERVol, Hedge, Interaction):

- baseline_roa | ERVol12Q: est=0.8981, p=0.0195
- baseline_roa | Hedge: est=-0.003217, p=0.851
- baseline_netincome | ERVol12Q: est=3.046e+06, p=0.0174
- baseline_netincome | Hedge: est=-1.044e+04, p=0.846
- baseline_cfv | ERVol12Q: est=0.03894, p=0.682
- baseline_cfv | Hedge: est=0.005724, p=0.161
- interaction_roa | ERVol12Q: est=0.8228, p=0.0499
- interaction_roa | Hedge: est=-0.0326, p=0.522
- interaction_roa | ERVol12Q_Hedge: est=0.6166, p=0.612
- interaction_netincome | ERVol12Q: est=2.855e+06, p=0.0446
- interaction_netincome | Hedge: est=-8.502e+04, p=0.578
- interaction_netincome | ERVol12Q_Hedge: est=1.565e+06, p=0.673
- interaction_cfv | ERVol12Q: est=-0.06938, p=0.123
- interaction_cfv | Hedge: est=-0.03657, p=2.6e-08
- interaction_cfv | ERVol12Q_Hedge: est=0.8875, p=6.1e-10

Structural Break Tests (CUSUM and Chow at 2020Q1):

- ROA | CUSUM: stat=0.5619, p=0.91; crit(1/5/10%)=(1.63,1.36,1.22)
- ROA | Chow(2020Q1): F=0.6439, p=0.695 (df1=6, df2=38)
- NetIncome | CUSUM: stat=0.5431, p=0.93; crit(1/5/10%)=(1.63,1.36,1.22)
- NetIncome | Chow(2020Q1): F=0.7807, p=0.59 (df1=6, df2=38)
- CFV12Q | CUSUM: stat=1.349, p=0.0526; crit(1/5/10%)=(1.63,1.36,1.22)
- CFV12Q | Chow(2020Q1): F=6.457, p=9.35e-05 (df1=6, df2=38)