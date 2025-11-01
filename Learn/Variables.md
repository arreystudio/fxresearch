We define each variable consistent with corporate finance literature and standard financial metrics:

1. Exchange Rate Volatility (IDR/USD) - Commonly measured as the variability of the exchange rate over time. A standard approach is to compute the standard deviation of the first differences of log exchange rates (i.e. log returns) over a window (e.g. 12 months). For example, Clark et al. (IMF) note that the "most widely used measure of exchange rate volatility is the standard deviation of the first difference of logarithms of the exchange rate". For quarterly analysis, one could compute the standard deviation of the (log) IDR/USD changes within each quarter or over a rolling year of quarterly rates.

2. Hedging Intensity - Reflects the extent of a firm's currency hedging. In the literature this is often measured by the hedge ratio (e.g. the notional value of hedging contracts divided by the exposure) or by an instrument-count measure. For instance, Bartram, Brown & Fehle (2009) define "hedging intensity" as the number of different derivative types used by a firm (e.g. forwards, options, swaps)[1]. In our case study, hedging intensity is coded as a binary indicator: 1 if the firm used any currency hedge in the quarter, 0 otherwise. (Other studies also use binary "hedger/non-hedger" variables[2] or hedge-ratios; the binary indicator simply flags the presence of hedging.)

3. Return on Assets (ROA) - A profitability ratio. ROA is generally defined as net income divided by total assets (often using average assets over the period). In formula form:
ROA = (Net Income / Total Assets) * 100

As noted by financial analysts, "Return on assets (ROA) is a profitability ratio that measures how efficiently a company generates profit from its total assets, calculated by dividing net income by total assets" [3]. Some sources use average total assets in the denominator (for multi-period analysis), but using ending total assets is also common for single periods[4].

4. Net Income - Net profit for the period after all expenses. Formally, net income is total revenues minus all operating costs, interest, taxes and other expenses[5]. In a formula:
Net Income = Revenues - (COGS + OpEx + Interest + Taxes + ... ).

It is the "bottom line" on the income statement[5] and a basic measure of profitability.

5. Cash Flow Volatility - The variability of operating cash flows. We recommend measuring this as a standard deviation of cash flow over time. For example, one approach is to take the standard deviation of quarterly cash flows (or changes in cash flow) over a rolling horizon. The Federal Reserve note on insurers defines quarterly cash flow volatility as "the standard deviation of the realized change in net cash flows" [6].
Other academic work (e.g. Phillips et al.) computes cash-flow volatility as the standard deviation of the cash-flow-to-assets ratio (profit margin) over the past 12 quarters [7]. In practice, we will compute Cash Flow Volatility by applying a rolling-window standard deviation to quarterly operating cash flow (e.g. over 12 past quarters) so that each quarter's volatility captures recent variability (see next section).

6. Debt-to-Equity Ratio (DER) - A leverage ratio. Defined as total debt divided by shareholders' equity. In formula:
Debt-to-Equity = Total Debt / Shareholders' Equity

Here Total Debt includes all interest-bearing debt (short- and long-term). For example, CFI states "Debt to Equity Ratio = Total Debt / Shareholders' Equity" [8]. This ratio indicates how much of the firm's financing is via debt versus equity[8].

7. Total Assets - The book value of all firm assets. According to standard accounting, Total Assets equals the sum of current and non-current assets on the balance sheet [9]. The identity on a balance sheet is Assets = Liabilities + Shareholders' Equity, so total assets
represent everything the firm owns. We take Total Assets (at period end) directly from financial statements[9].

8. Current Ratio - A liquidity ratio. Defined as current assets divided by current liabilities.
In formula:
Current Ratio = Current Assets / Current Liabilities

It measures the firm's ability to meet short-term obligations. Corporate Finance sources note that the current ratio "compares current assets to current liabilities to determine how well a company can meet all financial obligations due within a year," and explicitly give the formula as Current Assets / Current Liabilities[10][11].