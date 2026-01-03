# TEP Anomaly Classification with Mamba2

## Project Overview
This project focuses on anomaly classification using the Mamba2 architecture on the Tennessee Eastman Process (TEP) dataset.

## Folder Structure
- `data/`: Contains the dataset files (csv and rdata formats). *Excluded from version control due to size.*
- `notebooks/`: Jupyter notebooks for training and analysis (e.g., `mamba_anomaly_classification.ipynb`).
- `scripts/`: Helper scripts, including data conversion tools (`Rdata_to_csv_converter.py`).
- `models/`: Trained model files (`mamba_model.pth`).

## Usage
1. Ensure your data is placed in the `data/` directory.
2. Run the `Rdata_to_csv_converter.py` if you need to convert `.rdata` files to `.csv`.
3. Open `notebooks/mamba_anomaly_classification.ipynb` to view the training process or train the model.

## Future Improvements to the Model
To further improve performance, the following steps are recommended:

1. **Input Augmentation with Derivatives**: 
   Instead of using the raw input shape of (Batch_Size, Window_length, 52), calculate the 1st derivative of the variables and append them. This changes the input shape to **(Batch_Size, Window_length, 104)**. This provides the model with trend information.

2. **Two-Stage Approach**:
   Literature suggests that a two-step approach is more effective:
   - **Step 1**: Train an **Autoencoder** specifically for Anomaly Detection (binary classification: normal vs. anomaly).
   - **Step 2**: Train a separate **Classifier** model for 20-class Anomaly Classification.
