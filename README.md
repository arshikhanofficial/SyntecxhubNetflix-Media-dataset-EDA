# Netflix / Media Dataset EDA

This project performs **Exploratory Data Analysis (EDA)** on the Netflix Movies and TV Shows dataset.  
The goal is to analyze content distribution, trends over time, and the most common genres available on Netflix.

---

## Project Objectives

- Analyze the number of **Movies vs TV Shows**
- Explore **content growth over the years**
- Identify **top genres on Netflix**
- Visualize **content distribution and trends**
- Generate **top-10 lists for genres and release years**

---

## Project Structure
netflix_eda_project
│
├── data
│   └── netflix_titles.csv
│
├── src
│   ├── data_cleaning.py
│   ├── analysis.py
│   └── visualization.py
│
├── main.py
├── requirements.txt
└── README.md


---

## Dataset

Dataset used: **Netflix Movies and TV Shows Dataset**

Typical columns in the dataset:

- show_id
- type
- title
- director
- cast
- country
- date_added
- release_year
- rating
- duration
- listed_in
- description

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## How to Run the Project

### 1. Clone the repository
git clone <your-repo-link>


### 2. Navigate to the project folder


cd NetflixEDA


### 3. Create a virtual environment


python -m venv venv


Activate it:

Windows


venv\Scripts\activate


---

### 4. Install dependencies


pip install -r requirements.txt


---

### 5. Run the project
python main.py

## Key Insights

### Movies vs TV Shows


Movies: 5377
TV Shows: 2410


Netflix contains **more Movies than TV Shows**.

---

### Top Release Years

| Year | Number of Titles |
|-----|-----|
| 2018 | 1121 |
| 2017 | 1012 |
| 2019 | 996 |
| 2016 | 882 |
| 2020 | 868 |

Netflix content production increased significantly **after 2015**.

---

### Top Genres

| Genre | Count |
|------|------|
| International Movies | 2437 |
| Dramas | 2106 |
| Comedies | 1471 |
| International TV Shows | 1199 |

The platform has a strong focus on **International Movies and Dramas**.

---

## Visualizations Generated

The project generates the following visualizations:

- Movies vs TV Shows distribution
- Content growth over time
- Top genres on Netflix

---

## Conclusion

This exploratory analysis highlights how Netflix expanded its content library rapidly in recent years and shows the dominance of **international and drama content categories**.

---

## Author

**Najish Anjum**  
B.Tech CSE (AI & ML)  
