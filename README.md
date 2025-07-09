# ASEM Analysis App

<img src="https://raw.githubusercontent.com/edavgaun/ASEM-Analysis-App/refs/heads/main/assets/ASEM_logo_web_400px.png" width=300>

This repository was created to support the analysis of 10 years of data from the ASEM conference proceedings (2015–2024).

The project includes:
- Interactive visualizations such as dynamic network graphs, bubble charts, 3D scatterplots, and word clouds.
- Data exploration tools built with Python, Plotly, Seaborn, ipywidgets, and Voila.
- An accessible web application that allows users to explore patterns, trends, and insights from ASEM publications over time.

---

## 🚀 Access the App

You can explore the live app here:  
**[Launch the App](https://asem-analysis-app.onrender.com)**

---

## 📚 Project Structure

- `/Data` – CSV files containing conference proceedings data (2015–2024)
- `/assets` – Images and logos used for visualizations
- `app.ipynb` – Main Jupyter Notebook used to build the application
- `requirements.txt` – Python dependencies

Full Tree:

📁 YourProjectRoot/
├── main.py                     # ✅ Entry point for Streamlit GUI
├── requirements.txt            # ✅ Python dependencies
├── README.md                   # ✅ Project documentation
│
├── 📁 Data/                    # 📊 Datasets & Text Resources
│   ├── CP_2015.csv
│   ├── CP_2016.csv
│   ├── CP_2017.csv
│   ├── CP_2018.csv
│   ├── CP_2019.csv
│   ├── CP_2020.csv
│   ├── CP_2021.csv
│   ├── CP_2022.csv
│   ├── CP_2023.csv
│   ├── CP_2024.csv
│   ├── data_full.csv           # Full dataset (all years)
│   ├── df_long.csv             # Long format for radar/etc.
│   └── own_stopwords.txt       # Custom stopwords for NLP
│
├── 📁 Modules/                 # 🧠 Modular functions
│   ├── __init__.py
│   ├── 📁 Utils/
│   │   ├── __init__.py
│   │   ├── get_df.py
│   │   ├── get_corpus.py
│   │   ├── get_tokens.py
│   │   ├── get_bow.py
│   │   ├── get_bow_df.py
│   │   ├── get_dict.py
│   │   ├── get_word_frq.py
│   │   ├── get_topN_word_bow_df.py
│   │   ├── get_combinations.py
│   │   ├── get_long_df.py
│   │   ├── get_wide_df.py
│   │   └── WS.py
│   │
│   └── 📁 Chart/
│       ├── Bubble_chart.py
│       ├── update_bubble_chart.py
│       ├── compare_radar.py
│       ├── draw_Network.py
│       ├── draw_word_cloud.py
│       ├── radar_chart.py
│       └── scatterplot3D.py
│
├── 📁 assets/                  # 🎨 Static assets (images, masks)
│   └── [your uploaded files, e.g., wordcloud_mask.png, etc.]

---

## 🛠 Technologies Used

- Python 3.11
- Pandas, Numpy, Matplotlib, Seaborn
- Plotly, ipywidgets, WordCloud, NetworkX
- Scikit-learn, Yellowbrick
- Streamlit for rendering

---

## 📜 Notice

This project was developed at Rice University for educational and research demonstration purposes.

It is made publicly available for non-commercial academic and research use only.  
All rights related to commercial use, reproduction, or distribution are reserved.  
Please contact Rice University for licensing inquiries or permissions beyond educational use.



---

## 📬 Contact

For questions or collaborations, please contact:  
**Edgar Avalos-Gauna**  
ea37@rice.edu 
Rice University

---
