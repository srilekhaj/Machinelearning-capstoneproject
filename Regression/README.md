# Machinelearning-capstoneproject

## Healthcare Analytics (Medical Domain)**

### A. **Regression - Predicting healthcare cost**

* **Goal**: Predict patient treatment cost based on age, diagnosis, length of stay, etc.
* **Target**: Total cost (continuous variable)
* **Possible Dataset**:

* [Medical Cost Personal Dataset – Kaggle](https://www.kaggle.com/mirichoi0218/insurance)

flowchart LR
subgraph User
U[User Input Form]
end


subgraph Frontend
FE[React / Streamlit / Django Templates]
end


U --> FE
FE --> BE[Backend (Django REST API)]
BE --> Preproc[Preprocessing & Validation]
Preproc --> Stage1[Stage-1: Clinical Predictors]
Stage1 --> Stage1_Out[Predicted: treatment_type, patient_type, LOS]
Stage1_Out --> Stage2[Stage-2: Cost Prediction Model]
BE --> DB[(Database: Postgres)]
Preproc --> DB
Stage2 --> Result[Predicted Charges]
Result --> FE
FE --> GitHub[Optional: Save Report / Export JSON]


subgraph ML_Training
RawData[Raw Historical Dataset]
DataPipeline[Data Cleaning & FE]
TrainStage1[Train Models A/B/C]
TrainStage2[Train Cost Model]
Evaluate[Evaluation & Explainability]
Deploy[Export Model Artifacts (.pkl / ONNX)]
end


RawData --> DataPipeline --> TrainStage1 --> Evaluate --> Deploy
DataPipeline --> TrainStage2 --> Evaluate --> Deploy
Deploy --> BE
