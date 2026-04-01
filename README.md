# Machine Learning Capstone Project

## Healthcare Cost Prediction (Regression)

## Project Description

This capstone is a **healthcare-focused regression project** that predicts **annual medical insurance charges** for individuals from structured tabular data. It follows a full machine learning lifecycle: acquiring and cleaning data, exploring patterns, training and comparing regression models, selecting a strong final model, and exposing predictions through a **Django** web app so results are usable beyond notebooks.

The dataset includes demographic and lifestyle attributes (for example age, BMI, smoking status, and region) alongside historical **charges**. The workflow is split into numbered stages under the `Regression/` folder so each step—collection, preprocessing, EDA, modeling, final model, and deployment—stays reproducible and easy to show in a portfolio or interview.

**What you get from this repository:** documented notebooks for analysis and modeling, derived/preprocessed CSV artifacts where applicable, and a deployable application folder for interactive cost prediction—all framed around a realistic **supervised regression** problem in the medical cost domain.

## Project Objective

- Build a regression model to estimate medical insurance charges.
- Understand key factors that influence healthcare expenses.
- Deliver a practical prediction interface through a Django web application.

## Problem Statement

Healthcare costs vary significantly based on factors such as age, BMI, smoking habits, and region.  
Accurate cost prediction helps stakeholders estimate expenses early and supports better financial planning.

- **Task Type**: Supervised Machine Learning - Regression
- **Target Variable**: `charges` (continuous value)
- **Domain**: Healthcare Analytics

## Dataset

- **Source**: [Medical Cost Personal Dataset (Kaggle)](https://www.kaggle.com/mirichoi0218/insurance)
- **Primary File**: `insurance.csv`
- **Typical Features**:
  - `age`
  - `sex`
  - `bmi`
  - `children`
  - `smoker`
  - `region`
  - `charges` (target)

## End-to-End Workflow

The project is organized stage-by-stage for clarity and reproducibility:

1. **Data Collection**  
   - Notebook: `Regression/1.Data Collection/datacollection.ipynb`
2. **Data Preprocessing**  
   - Notebook: `Regression/2.Data Preprocessing/data preprocessing.ipynb`  
   - Output: cleaned/preprocessed dataset
3. **Exploratory Data Analysis (EDA)**  
   - Notebook: `Regression/3.Datascience Univariate & Bivariate/Data_Analysis.ipynb`  
   - Includes univariate and bivariate analysis
4. **Feature Selection & Model Building**  
   - Notebook: `Regression/4.Feature selection and model creation/regresssionalgorithms.ipynb`
5. **Final Model Development**  
   - Notebook: `Regression/5.Final model/final_model.ipynb`
6. **Deployment (Django Web App)**  
   - App Folder: `Regression/6.Djangowebapp`

## Tech Stack

- **Language**: Python
- **Data Analysis**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Machine Learning**: Scikit-learn
- **Deployment**: Django
- **Environment**: Jupyter Notebook

## Repository Structure

```text
Machinelearning-capstoneproject/
|- insurance.csv
|- README.md
`- Regression/
   |- 1.Data Collection/
   |- 2.Data Preprocessing/
   |- 3.Datascience Univariate & Bivariate/
   |- 4.Feature selection and model creation/
   |- 5.Final model/
   `- 6.Djangowebapp/
```

## How to Run This Project

### 1) Clone the repository

```bash
git clone <your-repo-url>
cd Machinelearning-capstoneproject
```

### 2) Run notebooks in sequence

Open the notebooks in order from Step 1 to Step 5 to reproduce preprocessing, EDA, and model training.

### 3) Run the Django app (optional)

```bash
cd "Regression/6.Djangowebapp"
python manage.py runserver
```

Then open `http://127.0.0.1:8000/` in your browser.

## Results and Insights

- Built regression models to estimate insurance charges.
- Identified major cost-driving factors through EDA and model interpretation.
- Delivered a deployable prediction interface using Django.

> Tip: Add your best model name and metrics here (for example: R2 score, MAE, RMSE) for stronger portfolio impact.

## Portfolio Highlights

- Clear end-to-end ML lifecycle implementation.
- Structured experimentation across preprocessing, EDA, and model selection.
- Real-world deployment integration beyond notebook-only work.

## Future Enhancements

- Add model versioning and experiment tracking.
- Containerize the Django app using Docker.
- Deploy to cloud (Render, Railway, or AWS).
- Add CI/CD and unit/integration tests.

## Author

**Srilekha**  
Machine Learning Enthusiast | Healthcare Analytics

---

If you found this project useful, consider starring the repository.
