# TEP Anomaly Classification with Mamba2

> **Note**: For access to the completely raw version of the dataset, please refer to: https://github.com/camaramm/tennessee-eastman-profBraatz

## Project Overview
This project focuses on anomaly classification using the Mamba2 architecture on the Tennessee Eastman Process (TEP) dataset.

## Folder Structure
- `data/`: Contains the dataset files (csv and rdata formats). *Excluded from version control due to size.*
- `notebooks/`: Jupyter notebooks for training and analysis (e.g., `mamba_anomaly_classification.ipynb`).
- `scripts/`: Helper scripts, including data conversion tools (`Rdata_to_csv_converter.py`).
- `models/`: Trained model files (`mamba_model.pth`).

## Model Architecture
The model consists of 4 fixed-size Mamba blocks.

### Configuration Parameters
| Parameter | Value |
|-----------|-------|
| window_length | 128 |
| batch_size | 64 |
| d_state | 64 |
| n_layers | 4 |
| learning_rate | 5e-4 |
| dropout | 0.25 |
| num_classes | 21 |
| dmodel | 48 |

## Usage
1. Ensure your data is placed in the `data/` directory.
2. Run the `Rdata_to_csv_converter.py` if you need to convert `.rdata` files to `.csv`.
3. Open `notebooks/mamba_anomaly_classification.ipynb` to view the training process or train the model.


## Detection Rate
![Detection Rate](images/detectionRate.png)

## Future Improvements to the Model

To further improve performance, the following steps are recommended:

The current model utilizes significantly fewer parameters while achieving performance comparable to transformer-based models found in the literature. However, to improve class 0 accuracy, it is recommended to train two separate models:
1. An autoencoder for anomaly detection.
2. A 20-class classifier for anomaly classification.
