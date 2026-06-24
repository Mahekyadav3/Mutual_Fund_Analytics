# Mutual Fund Analytics Platform - Data Dictionary

## Source Datasets

### 1. NAV History (02_nav_history.csv)

| Column Name | Data Type | Description |
|------------|------------|------------|
| amfi_code | INTEGER | Unique AMFI scheme identifier |
| date | DATE | NAV date |
| nav | FLOAT | Net Asset Value of the mutual fund |

---

### 2. Investor Transactions (08_investor_transactions.csv)

| Column Name | Data Type | Description |
|------------|------------|------------|
| investor_id | INTEGER | Unique investor identifier |
| amfi_code | INTEGER | Mutual fund scheme code |
| transaction_date | DATE | Date of transaction |
| transaction_type | TEXT | SIP, Lumpsum, or Redemption |
| amount_inr | FLOAT | Transaction amount in INR |
| kyc_status | TEXT | Investor KYC verification status |

---

### 3. Scheme Performance (07_scheme_performance.csv)

| Column Name | Data Type | Description |
|------------|------------|------------|
| amfi_code | INTEGER | Unique AMFI scheme identifier |
| scheme_name | TEXT | Mutual fund scheme name |
| fund_house | TEXT | Asset management company |
| category | TEXT | Fund category |
| return_1yr_pct | FLOAT | One-year return percentage |
| return_3yr_pct | FLOAT | Three-year return percentage |
| return_5yr_pct | FLOAT | Five-year return percentage |
| sharpe_ratio | FLOAT | Risk-adjusted return metric |
| expense_ratio_pct | FLOAT | Annual expense ratio percentage |
| aum_crore | FLOAT | Assets Under Management (Crores) |
| risk_grade | TEXT | Fund risk classification |

---

## Database Tables

### Dimension Tables

#### dim_fund

Stores fund-level descriptive information.

#### dim_date

Stores date-related attributes such as year, month, and quarter.

---

### Fact Tables

#### fact_nav

Stores NAV values over time.

#### fact_transactions

Stores investor transaction records.

#### fact_performance

Stores fund return and risk metrics.

#### fact_aum

Stores Assets Under Management information.

---

## Data Sources

- AMFI Mutual Fund Dataset
- MFAPI NAV Data
- Internship-provided CSV datasets
