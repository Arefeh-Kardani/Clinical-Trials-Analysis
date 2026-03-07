# Clinical Trials Analysis

A Python-based toolkit for extracting, analyzing, and visualizing clinical trial data from [ClinicalTrials.gov](https://clinicaltrials.gov/).

## Overview

This project provides tools to fetch study data via the ClinicalTrials.gov API (v2), perform exploratory data analysis (EDA), and prepare data for further reporting and visualization.

## Project Structure

- `scripts/`: Python scripts for data extraction and processing.
  - `extract_trials.py`: Fetches cancer-related trial data (NCT ID, Condition, Phase, etc.) and saves it for analysis.
- `notebooks/`: Jupyter Notebooks for interactive data exploration.
  - `exploration.ipynb`: EDA on extracted clinical trials.
- `data/`: (Local) Storage for raw and processed data (ignored by Git).

## Tech Stack

- **Python 3.x**
- **Data Handling:** `pandas`, `numpy`
- **Visualization:** `matplotlib`, `seaborn`
- **API Requests:** `requests`
- **Notebooks:** `jupyterlab`

## Getting Started

### Prerequisites

- Python 3.8+
- [Git](https://git-scm.com/)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Arefeh-Kardani/Clinical-Trials-Analysis.git
   cd Clinical-Trials-Analysis
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. **Extract Data:**
   Run the extraction script to fetch the latest trial data.
   ```bash
   python scripts/extract_trials.py
   ```

2. **Explore Data:**
   Launch Jupyter to view the exploration notebook.
   ```bash
   jupyter lab notebooks/exploration.ipynb
   ```

## License

This project is open-source and available under the MIT License.
