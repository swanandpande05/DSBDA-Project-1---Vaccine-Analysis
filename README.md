📊 COVID-19 Vaccination Analyzer (India)
📌 Overview

This project analyzes COVID-19 vaccination trends across different states in India using a dataset sourced from Kaggle. It provides insights into first dose, second dose, and gender-wise vaccination distribution through data analysis and visualization.

🚀 Features
📍 State-wise First Dose Analysis
📍 State-wise Second Dose Analysis
👨 Male Vaccination Insights
👩 Female Vaccination Insights
📊 Data Visualization
🌐 Interactive Web App using Streamlit
🛠️ Tech Stack
Language: Python
Libraries: Pandas, NumPy
Visualization: Matplotlib
Web App: Streamlit
📂 Project Structure
CovidVaccineProject/
│
├── app.py
├── vaccine_analysis.py
├── covid_vaccine_statewise.csv
├── requirements.txt
└── README.md
📁 Dataset
Source: Kaggle
Dataset: covid_vaccine_statewise.csv
👉 https://www.kaggle.com/sudalairajkumar/covid19-in-india
⚙️ Installation & Setup
1. Download Dataset
Download from Kaggle link above
Place the CSV file inside the project folder
2. Install Dependencies
pip install pandas numpy matplotlib streamlit
3. Run Application
streamlit run app.py
📊 How It Works
Loads dataset using Pandas
Cleans and preprocesses data
Performs state-wise aggregation
Extracts cumulative vaccination values
Displays results using charts and tables
📸 Screenshots
<p align="center"> <img src="SS1.png" width="30%" /> <img src="SS2.png" width="30%" /> <img src="SS3.png" width="30%" /> </p>
🎯 Objectives
Analyze vaccination progress in India
Compare state-wise performance
Study gender-based vaccination trends
🔮 Future Improvements
Add filters (state, date)
Improve UI
Add more visualizations
Deploy online
👨‍💻 Author

Your Name

📜 License

This project is for educational purposes.
