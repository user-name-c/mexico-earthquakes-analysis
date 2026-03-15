# Mexico Earthquake Analysis (EDA)

![Magnitude Distribution](https://github.com/user-name-c/mexico-earthquakes-analysis/blob/main/outputs/figures/earthquake_distribution_magnitudes.png)

An automated data pipeline and exploratory analysis of seismic activity in Mexico using the **USGS Earthquake Hazards Program API**. This project demonstrates professional data handling, from raw API ingestion to visual insights.

## 🎯 Project Overview

This project addresses the challenge of handling nested API data and transforming it into actionable insights. It answers:

* **Seismic Frequency:** How often do earthquakes occur in the region?
* **Magnitude Distribution:** What is the probability of high-magnitude events?
* **Regional Risk:** Which Mexican states report the highest seismic activity?

## 🛠️ Tech Stack

* **Data Processing:** Python, Pandas, NumPy.
* **Visualization:** Matplotlib, Seaborn.
* **Ingestion:** Requests (REST API).

## 📂 Project Structure

```bash
mexico-earthquakes-analysis/
├── data/
│   ├── raw/            # Original JSON from API (Ignored by Git)
│   └── processed/      # Cleaned CSV for analysis
├── notebooks/
│   └── analysis.ipynb  # Main EDA and visualizations
├── scripts/
│   ├── fetch_data.py   # API connection logic
│   └── process_data.py # Data cleaning and ETL
├── outputs/
│   └── figures/        # Generated plots
└── README.md

```

## 🚀 How to Run

1. **Clone the repository:**
```bash
git clone https://github.com/youruser/mexico-earthquakes-analysis.git

```


2. **Install dependencies:**
```bash
pip install -r requirements.txt

```


3. **Run the pipeline:**
Open `notebooks/analysis.ipynb` and run all cells. The notebook automatically triggers the scripts to fetch and process the latest data.

## 📈 Key Insights 

* **Standardization:** Successfully converted Unix/UTC timestamps to local Mexico City timezone for better reporting.
* **Cleaning:** Filtered out seismic noise (magnitudes < 2.5) to focus on significant geological events.
