# Healthcare & Pharma Data Analytics Portfolio
🏥 Hospital Readmission Risk Analysis
Healthcare Analytics using Python

📊 Live Analysis & Outputs:
👉 Kaggle Notebook: https://www.kaggle.com/code/nikitashelke01/eda-completed

📌 Project Type: Exploratory Data Analysis (EDA)
📊 Domain: Healthcare Analytics
🛠️ Tools: Python, Pandas, NumPy, Matplotlib
📂 Dataset: Diabetes 130-US Hospitals (1999–2008)

📌 Project Overview

Hospital readmissions significantly increase healthcare costs and often indicate gaps in treatment quality, discharge planning, or post-hospital follow-up care. Reducing avoidable readmissions is a critical priority for healthcare organizations to improve patient outcomes and optimize operational efficiency.

This project performs an exploratory healthcare analytics study using electronic health record (EHR) data to identify patient characteristics and hospital utilization patterns associated with 30-day hospital readmissions.

The analysis demonstrates how healthcare data can be transformed into actionable insights to support data-driven clinical and operational decision-making.

🎯 Business Objective

The primary objectives of this project are to:

Analyze hospital readmission patterns using real-world healthcare data

Identify patient groups with higher 30-day readmission risk

Generate actionable insights that can support improved discharge planning and patient care strategies

📊 Key Performance Indicators (KPIs)

The following KPIs were analyzed to understand readmission behavior:

Total patient encounters

30-day hospital readmission rate

Average length of hospital stay

Number of prior inpatient visits

Medication usage intensity

These indicators help identify high-risk patient segments and hospital utilization trends linked to readmission outcomes.

📂 Dataset Description

The dataset contains anonymized patient encounter records from U.S. hospitals between 1999 and 2008, focused on diabetes-related admissions.

Each record represents a single hospital encounter and includes:

Patient demographics

Hospital utilization history

Diagnostic information

Medication usage

Readmission outcome

🧹 Data Cleaning & Preparation

To ensure data quality and analytical reliability, the following steps were performed:

Converted placeholder symbols (?) into proper missing values

Removed columns with more than 50% missing data to reduce bias

Verified data types and dataset structure

Selected clinically relevant features for focused analysis

These steps ensured consistency and improved interpretability of results.

🧩 Feature Engineering

Key feature engineering steps included:

Conversion of the readmission outcome into a binary target variable:

1 → Readmitted within 30 days

0 → Not readmitted within 30 days

Grouping prior inpatient visits into utilization-based categories

Selection of features relevant to patient risk assessment

This approach improved analytical clarity and enabled meaningful comparison across patient groups.

📈 Exploratory Data Analysis (EDA)

Exploratory analysis was conducted using statistical summaries and visualizations to identify patterns associated with readmission risk.

🔹 Readmission Rate by Age Group

Readmission risk increases with patient age

Elderly patients (70+ years) show higher readmission rates

🔹 Readmission Rate by Prior Inpatient Visits

Patients with frequent prior hospitalizations exhibit significantly higher readmission risk

Indicates chronic or severe health conditions requiring enhanced care planning

🔹 Readmission Rate by Gender

Readmission rates are similar across genders

Gender alone is not a strong predictor of 30-day readmission risk

🧠 Key Insights

Readmission risk increases with age, particularly among elderly patients

Prior inpatient visit frequency is a strong indicator of future readmission risk

Gender does not significantly influence 30-day readmission outcomes

🏥 Business Recommendations

Based on the analysis, healthcare providers may reduce readmissions by:

Implementing enhanced discharge planning for elderly patients

Closely monitoring patients with frequent prior inpatient admissions

Strengthening post-discharge follow-up and outpatient care programs

Improving patient education on medication adherence and after-care

These measures can improve patient outcomes while reducing avoidable healthcare costs.

✅ Conclusion

This project highlights the importance of patient age and hospital utilization history in understanding hospital readmission risk.

The analysis demonstrates how exploratory healthcare analytics can support evidence-based decision-making and help hospitals identify high-risk patients for targeted interventions.
