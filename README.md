
# Project Name: Bailando: 3D Dance Generation by Actor-Critic GPT with Choreographic Memory

## Overview
This project involves generating dancing results using the VQ-VAE model. The setup includes creating a suitable environment, installing dependencies, and executing scripts for evaluation. The results of experiments are available for review in the `experiments` folder.

---

## Setup Instructions

### Step 1: Clone the Repository
```bash
git clone [repository-url]
cd [repository-folder]
```

---

### Step 2: Install WSL (if using Windows)
Follow the WSL installation guide:  
[https://learn.microsoft.com/en-us/windows/wsl/install](https://learn.microsoft.com/en-us/windows/wsl/install)

---

### Step 3: Set Up a Virtual Environment
```bash
# Create a Python virtual environment
python3 -m venv venv
source venv/bin/activate  # For Linux/macOS

# On Windows (if not using WSL)
# venv\Scripts\activate
```

---

### Step 4: Install Dependencies
```bash
# Install dependencies from requirements.txt
pip install -r requirements.txt
```

---

## Running the Evaluation

### Generate Dancing Results
```bash
# Run the evaluation script to test VQ-VAE
sh srun.sh configs/sep_vqvae.yaml eval [your node name] 1
```

Replace `[your node name]` with your actual node name.

---

## Viewing Experiment Results
```bash
# Navigate to the experiments folder
cd experiments

# View results (example for images, logs, etc.)
ls -l
```

---

## API Integration
```bash
# Extract the API folder
unzip API.zip -d ./API

# Follow the API folder's instructions to set it up (if additional steps are provided).
```

---

## Compatibility Checks
```bash
# Check Python version
python --version

# Check pip version
pip --version

# Check installed packages
pip list
```

---

## Notes
- Replace placeholders like `[repository-url]` and `[your node name]` with actual values.
- Ensure that the `srun.sh` script is executable:
  ```bash
  chmod +x srun.sh
  ```
- If issues arise, confirm dependencies in `requirements.txt` are correctly installed.
