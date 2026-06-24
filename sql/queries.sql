-- 1. Top 5 Funds by AUM

SELECT
    scheme_name,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- 2. Average NAV per Fund

SELECT
    amfi_code,
    AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;


-- 3. Monthly Average NAV

SELECT
    substr(date,1,7) AS month,
    AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;


-- 4. Transactions by Type

SELECT
    transaction_type,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY transaction_type;


-- 5. Total Investment Amount by Transaction Type

SELECT
    transaction_type,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY transaction_type;


-- 6. Funds with Expense Ratio Below 1%

SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;


-- 7. Top 10 Funds by 1-Year Return

SELECT
    scheme_name,
    return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 10;


-- 8. Average Return by Category

SELECT
    category,
    AVG(return_1yr_pct) AS avg_return
FROM fact_performance
GROUP BY category;


-- 9. Average Sharpe Ratio by Risk Grade

SELECT
    risk_grade,
    AVG(sharpe_ratio) AS avg_sharpe
FROM fact_performance
GROUP BY risk_grade;


-- 10. Fund Count by Fund House

SELECT
    fund_house,
    COUNT(*) AS fund_count
FROM fact_performance
GROUP BY fund_house
ORDER BY fund_count DESC;
