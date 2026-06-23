# 📊 Mutual Fund Analytics Platform

A Python-based data analytics project developed as part of the **Bluestock Fintech Internship**.

The project focuses on collecting, validating, analyzing, and visualizing mutual fund data using historical datasets and live NAV data from the MFAPI.

---

## 🎯 Objectives

- Load and validate mutual fund datasets.
- Fetch live NAV data using MFAPI.
- Perform data quality checks.
- Explore fund houses, categories, and scheme information.
- Build a foundation for analytics dashboards and reporting.

---

## 📁 Project Structure

```text
Mutual_Fund_Analytics/
│
├── dashboard/
├── data/
│   ├── raw/
│   ├── processed/
│   └── live_nav/
│
├── notebooks/
├── reports/
├── scripts/
├── sql/
├── src/
│   ├── data_ingestion.py
│   ├── live_nav_fetch.py
│   ├── multiple_nav_fetch.py
│   ├── amfi_validation.py
│   └── main.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🛠️ Tech Stack

- Python 3
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- SQLAlchemy
- Requests
- SciPy
- Jupyter Notebook
- Git & GitHub

---

## 📦 Installation

### Clone the repository

```bash
git clone <your-github-repository-url>
cd Mutual_Fund_Analytics
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📂 Dataset

This project uses multiple mutual fund datasets containing information related to:

- Fund Master
- Historical NAV
- Assets Under Management (AUM)
- SIP Data
- Portfolio Holdings
- Investor Transactions
- Benchmark Information
- Scheme Categories
- Industry Folios
- Scheme Performance

---

## ✅ Day 1 Progress

- Created project folder structure
- Initialized Git repository
- Installed required Python libraries
- Created `requirements.txt`
- Loaded all 10 CSV datasets
- Printed dataset shape, data types, and sample records
- Identified basic data anomalies
- Fetched live NAV data from MFAPI
- Retrieved NAV data for five mutual fund schemes
- Explored fund houses, categories, and risk grades
- Validated AMFI scheme codes
- Prepared a Data Quality Summary

---

## 🚀 Future Work

- Data Cleaning & Preprocessing
- SQL Database Integration
- Exploratory Data Analysis (EDA)
- Interactive Dashboard
- Portfolio Analytics
- Risk Analysis
- Performance Visualization
- Predictive Analytics

---

## 👩‍💻 Author

**Mahek Yadav**

Bluestock Fintech Internship

---

## 📄 License

This project is developed for educational and internship purposes.
