# Movies Data Analysis: Genres Distribution

## 📌 Project overview
This project is an exploratory data analysis (EDA) of a movie dataset.  
The main goal is to clean the data, extract movie genres, and analyze how often each genre appears.

The project demonstrates basic data analysis skills using **pandas**, **NumPy**, **matplotlib**, and **seaborn**.

---

## 📂 Dataset
The dataset used in this project:

- **File:** `movies_metadata.csv`
- **Source:** provided locally in the `data/` folder
- **Description:** contains metadata about movies such as genres, tagline, homepage, and collections.

---

## 🛠 Libraries used
- `pandas` — data loading and manipulation  
- `numpy` — numerical operations  
- `matplotlib` — data visualization  
- `seaborn` — improved visualization styling  
- `ast` — converting genre strings into Python objects  

---

## 🧹 Data cleaning steps
The following data cleaning steps were performed:

1. Replaced missing values:
   - `tagline` → `"without tagline"`
   - `homepage` → `"no homepage"`
   - `belongs_to_collection` → empty dictionary (`{}`)

2. Removed rows with remaining missing values using:
   ```python
   df.dropna(inplace=True)