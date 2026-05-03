# ADOS Clinical AI Production System

This repository contains an institutional-grade Clinical AI Research and Production system engineered to enhance the diagnostic precision of Autism Diagnostic Observation Schedule (ADOS) assessments. By modeling complex clinical features (gaze patterns, phrase repetition rate, functional play, social smiles) under significant, realistic noise conditions, this system serves both as a research framework for data scientists and a robust reporting pipeline for healthcare providers.

---

## Technical Approach

- **Realistic ML Simulation**: Aggressive noise injection (25-35% measurement error), missing data patterns (8-15%), and challenging diagnostic borders (maximum 60-80% group overlap).
- **Diagnostics vs. Heuristics**: The models employ conservative hyperparameters and heavy regularization to avoid unrealistic over-fitting commonly seen in synthetic medical pipelines.
- **Reporting & Telemetry**: Generates end-to-end HTML-based clinical reports that provide clear interpretability, uncertainty/confidence analysis, and evidence-based recommendations.

## Repository Structure

```
ADOS/
├── deliverables/
│   ├── Clinical_AI_Research_and_Production_System_Technical_Report.pdf  # Comprehensive system guide
│   ├── clinician_demo_report_1.html                                     # Sample output reports
│   ├── clinician_demo_report_2.html
│   ├── clinician_demo_report_3.html
│   └── comprehensive_research_report.html
├── notebooks/
│   └── ML_ADOS.ipynb                                                    # Core integrated AI pipeline
├── src/                                                                 # Reserved for extracted Python modules
├── .gitignore
├── README.md
└── requirements.txt
```

## Quick Start

```bash
# 1. Clone the repository
git clone <repo-url>
cd ADOS

# 2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # macOS / Linux
# venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the notebook
jupyter notebook notebooks/ML_ADOS.ipynb
```

## Deliverables Generated

The executing pipeline produces two tiers of outputs:
1. **Research Reports (`comprehensive_research_report.html`)**: Designed for data scientists, focusing on AUC, precision/recall characteristics, feature importance (SHAP), and model validation under missingness.
2. **Clinical Output (`clinician_demo_report_*.html`)**: High-fidelity, user-friendly assessments formatted with modern typography and explicit confidence intervals tailored for doctors and healthcare providers.

## License

This project is shared for portfolio and educational purposes.
