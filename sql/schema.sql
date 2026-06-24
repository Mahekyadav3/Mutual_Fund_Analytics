-- Dimension Table: Fund
CREATE TABLE dim_fund (
    fund_id INT PRIMARY KEY,
    amfi_code INT UNIQUE,
    fund_name TEXT,
    category TEXT,
    fund_house TEXT
);
-- Dimension Table: Date
CREATE TABLE dim_date (
    date_id INT PRIMARY KEY,
    full_date DATE,
    year INT,
    month INT,
    quarter INT
);
-- Fact Table: NAV
CREATE TABLE fact_nav (
    nav_id INT PRIMARY KEY,
    fund_id INT,
    date_id INT,
    nav REAL,

    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);
-- Fact Table: Transactions
CREATE TABLE fact_transactions (
    transaction_id INT PRIMARY KEY,
    fund_id INT,
    date_id INT,
    transaction_type TEXT,
    amount_inr REAL,

    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);
--Fact Table: Performance
CREATE TABLE fact_performance (
    performance_id INT PRIMARY KEY,
    fund_id INT,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    expense_ratio_pct REAL,
    sharpe_ratio REAL,

    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id)
);
--Fact Table: AUM
CREATE TABLE fact_aum (
    aum_id INT PRIMARY KEY,
    fund_id INT,
    aum_crore REAL,

    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id)
);
