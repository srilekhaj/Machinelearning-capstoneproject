# Machinelearning-capstoneproject

## Healthcare Analytics (Medical Domain)**

### A. **Regression - Predicting healthcare cost**

* **Goal**: Predict patient treatment cost based on age, diagnosis, length of stay, etc.
* **Target**: Total cost (continuous variable)
* **Possible Dataset**:

* [Medical Cost Personal Dataset – Kaggle](https://www.kaggle.com/mirichoi0218/insurance)



flowchart LR

    %% USER INPUT %%%
    subgraph User
        U[User Input Form<br>(age, bmi, disease, severity, lifestyle,<br>hospital tier, insurance)]
    end

    %% FRONTEND %%%
    subgraph Frontend
        FE[Web UI (Django / Streamlit / React)]
    end

    U --> FE

    %% BACKEND %%%
    subgraph Backend
        BE[Django Backend API]
        Preproc[Preprocessing & Feature Encoding]
    end

    FE --> BE
    BE --> Preproc

    %% STAGE 1 MODELS %%%
    subgraph Stage1["Stage-1 ML (Clinical Predictors)"]
        M1A[Model A: Treatment Type<br>(Classification)]
        M1B[Model B: Patient Type<br>(Classification)]
        M1C[Model C: Length of Stay<br>(Regression)]
    end

    Preproc --> M1A
    Preproc --> M1B
    Preproc --> M1C

    M1A --> S1Out
    M1B --> S1Out
    M1C --> S1Out

    S1Out[Predicted Clinical Variables<br>• treatment_type<br>• patient_type<br>• length_of_stay]

    %% STAGE 2 MODEL %%%
    subgraph Stage2["Stage-2 ML (Cost Prediction)"]
        M2[Final Regression Model (XGBoost / RF)<br>Predicts: charges]
    end

    S1Out --> M2
    Preproc --> M2

    M2 --> Result[Predicted Healthcare Charges (₹)]

    %% DB OPTIONAL %%%
    BE --> DB[(PostgreSQL Database)]

    Result --> FE
