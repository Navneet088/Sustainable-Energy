# Sustainable Energy Project 🌱⚡

## 📌 Project Overview
The **Sustainable Energy** project aims to analyze global energy data and build **predictive models** for energy consumption and renewable energy adoption.  
The project provides **insights for sustainable energy planning** and helps understand factors influencing **electricity access, renewable energy usage, and emissions**.

---

## 🎯 Objectives
- Analyze global electricity and energy trends.
- Predict **access to electricity** and **renewable energy metrics**.
- Provide data-driven insights for **sustainable energy planning**.
- Explore relationships between **economic indicators** and energy consumption.

---

## 📂 Dataset
The dataset contains global energy-related metrics per country and year. Key columns include:

| Column Name | Description |
|-------------|-------------|
| Entity | Country or region name |
| Year | Year of the data |
| Access to electricity (% of population) | Percentage of population with electricity access |
| Access to clean fuels for cooking | Percentage of population using clean cooking fuels |
| Renewable-electricity-generating-capacity-per-capita | Installed renewable electricity capacity per person |
| Financial flows to developing countries (US $) | Energy-related financial flows to developing countries |
| Renewable energy share in the total final energy consumption (%) | Share of renewables in total energy consumption |
| Electricity from fossil fuels (TWh) | Electricity produced from fossil fuels |
| Electricity from nuclear (TWh) | Electricity produced from nuclear sources |
| Electricity from renewables (TWh) | Electricity produced from renewable sources |
| Low-carbon electricity (% electricity) | Share of low-carbon electricity in total electricity generation |
| Primary energy consumption per capita (kWh/person) | Energy consumed per person |
| Energy intensity level of primary energy (MJ/$2017 PPP GDP) | Energy used per unit of GDP |
| Value_co2_emissions_kt_by_country | CO2 emissions by country (in kilotons) |
| Renewables (% equivalent primary energy) | Renewable energy as % of primary energy |
| gdp_growth | GDP growth rate |
| gdp_per_capita | GDP per capita |
| Density (P/Km2) | Population density |
| Land Area (Km2) | Total land area |
| Latitude | Latitude coordinate |
| Longitude | Longitude coordinate |

**Files in the repository:**
- `sustainable_energy.csv` → Raw dataset
- `sustainable_energy_preprocessed.csv` → Cleaned and preprocessed dataset
- `model.pkl` → Trained machine learning model
- `main.py` → Python script for prediction
- `output1.csv` → Predicted results

---

## ⚙️ Tech Stack
- **Programming Language:** Python 🐍  
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Joblib  
- **Environment:** Jupyter Notebook / VS Code  

---

## 📊 Project Workflow
1. **Data Preprocessing**
   - Handle missing values
   - Encode categorical variables
   - Normalize numeric features

2. **Exploratory Data Analysis (EDA)**
   - Visualize energy access trends and renewable adoption
   - Correlation analysis between energy metrics, GDP, and emissions

3. **Model Building**
   - Split data into training and testing sets
   - Train models like:
     - Linear Regression
     - Random Forest
     - Decision Tree
   - Select the best-performing model

4. **Model Evaluation**
   - Metrics: MAE, RMSE, R² score
   - Compare **actual vs predicted values**

5. **Prediction & Output**
   - Predict electricity access, renewable share, and energy consumption
   - Save predictions in `output1.csv`

---

## 🚀 Features
- Predict electricity and renewable energy metrics globally
- Explore correlations between energy, GDP, and emissions
- Scalable and reusable machine learning model
- Clean visualizations for better insights

---

## 📌 Future Enhancements
- Deploy as a **web app** using Flask/Django  
- Include **real-time energy consumption data**  
- Use **deep learning models** for improved predictions  
- Build an **interactive dashboard** for global energy analytics  

---

## 📌 Usage
1. Clone the repository:
```bash
git clone https://github.com/Navneet088/Sustainable-Energy.git
