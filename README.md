# Proteasome-Interactome-AF-Predictions

This repository provides tools for analyzing **AlphaFold2-predicted protein-protein interactions**, focusing on spatial, confidence, and accuracy metrics. It enables a **systematic evaluation** of protein complex predictions with emphasis on three key confidence metrics:

---

## Key Metrics

1. **Model Confidence**  
   A weighted combination of:
   - **ipTM**: Interface predicted TM-score (inter-chain confidence)
   - **pTM**: Predicted TM-score (chain-level confidence)  
   **Formula:**  
   `Model Confidence = 0.8 × ipTM + 0.2 × pTM`

2. **pDockQ**  
   Confidence metric for protein-protein docking quality.

3. **pLDDT**  
   Per-residue confidence score from AlphaFold2 predictions.

---

## Scripts Overview

### `model_confidence.py`
Calculates the **model confidence score** for each of the five AlphaFold models used in a prediction.

**Usage:**

python model_confidence.py -run_ids <IDs> -path_to_run <PATH> -path_to_prediction <PATH> -project_name <NAME>

### `pdockq.py`
Generates the **pDockQ score** for each of the five models.

**Usage:**
```bash
python pdockq.py
```

### 'plot_AF_all_unrelaxed.py'
Generates the **plddt** scores for each of the five models, along with the **PAE (Predicted Aligned Error)** heatmaps 

**Usage:**
```bash
python plot_AF_all_unrelaxed.py
```
