
# Project Name: Bailando: 3D Dance Generation by Actor-Critic GPT with Choreographic Memory

## Overview
This project involves generating dancing results using the VQ-VAE model. The setup includes creating a suitable environment, installing dependencies, and executing scripts for evaluation. The results of experiments are available for review in the `experiments` folder.

---

### Prerequisites
- Python 3.8 or higher
- PyTorch
- Librosa (for music feature extraction)
- Windows Subsystem for Linux (WSL2) or Linux-based system
- CUDA Toolkit (if GPU support is required)

## Data Preparation
In our experiments, we use AIST++ for evaluation. Please visit [here](https://google.github.io/aistplusplus_dataset/download.html) to download the AIST++ annotations and unzip them as './aist_plusplus_final/' folder, visit [here](https://aistdancedb.ongaaccel.jp/database_download/) to download all original music pieces (wav) into './aist_plusplus_final/all_musics'. And please set up the AIST++ API from [here](https://github.com/google/aistplusplus_api) and download the required SMPL models from [here](https://smpl.is.tue.mpg.de/). Please make a folder './smpl' and copy the downloaded 'male' SMPL model (with '_m' in name) to 'smpl/SMPL_MALE.pkl' and To download the preprocessed models download from [here](https://drive.google.com/file/d/1EGJeBE1fE59ByjxR_-ipwV6Dz-Cx-stT/view?usp=sharing) as ./data folder if you don't wish to process the data.

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
To test GPT:

    sh srun_gpt_all.sh configs/cc_motion_gpt.yaml eval [your node name] 1
   
To test final restuls:
    
    sh srun_actor_critic.sh configs/actor_critic.yaml eval [your node name] 1
---
### Step 1: Extract the (kinetic & manual) features of all AIST++ motions (ONLY do it by once):
    
    python extract_aist_features.py


### Step 2: compute the evaluation metrics:

    python utils/metrics_new.py

It will show exactly the same values reported in the paper. To fasten the computation, comment Line 184 of utils/metrics_new.py after computed the ground-truth feature once. To test another folder, change Line 182 to your destination, or kindly modify this code to a "non hard version" :)

1. To run the vis_pkl.py file:
   ```bash
   python vis_pkl.py
   ```
This runs a sample file and generates the output

## Usage
### Input
- Music file (e.g., .mp3 or .wav)
- Initial pose configuration (pose codes)

### Running the Framework
```bash
python bailando.py --input <music_file> --output <output_directory>
## Viewing Experiment Results
```bash
# Navigate to the experiments folder
cd experiments

# View results (example for images, logs, etc.)
ls -l
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
## Our results
https://drive.google.com/file/d/1WAMc0Jvob0cZn5FbFmOlfPUkj9jAPbe8/view?usp=sharing
