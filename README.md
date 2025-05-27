# ATAC-seq Signal Processing 

This part of the project focuses on:

- Wrangling ATAC-seq signal data 
- Analyzing signal variability across samples 

The goal is to transform the raw ATAC-seq signal matrix into a tidy format and then assess per-sample variability (mean, median, standard deviation, CV).

---

## Part 1 – ATAC-seq Wrangling 

### Input
- **Folder:** `ATAC-seq/`
- Contains all raw and intermediate ATAC-seq files used for wrangling: 

- `ATAC-seq data.csv`: Original wide-format signal matrix (rows = peaks, columns = all samples). Not modified to avoid accidental deletion.
- `filtered_ATAC_abT_Tact_Stem.csv`: Subset of the original matrix, keeping only columns related to abT and T.act cell types.
- `refined_ATAC.csv`: Tidy-format table with selected samples and peaks reshaped into three columns: `peakID`, `SampleID`, and `Signal`.

### Method
1. **Filter for abT and T.act samples**
   - File used: `filtered_ATAC_abT_Tact_Stem.csv`
   - Only keeps columns corresponding to abT and T.act cell types.

2. **Refine and reshape**
   - File: `refined_ATAC.csv`
   - Reformats the data to include:
     - `peakID`
     - `SampleID`
     - `Signal`
   - Puts sample type (abT or T.act) and signal values into two columns (long format).

### Output
- **Final output:** `refined_ATAC.csv`  
- This tidy-format file will be used for variability analysis in the next step. 

---

---

## Part 2 – Signal Variability Analysis 

### Input
- **File:** `refined_ATAC.csv`  
  - Output from Part 1's wrangling step, containing tidy ATAC-seq signal values.

### Method
1. **Library Imports:**
   - Used `pandas`, `numpy`, `matplotlib`, `seaborn`, and `scanpy` for analysis and visualization.

2. **Data Loading:**
   - Loaded `refined_ATAC.csv` as a DataFrame for downstream analysis.

3. **Descriptive Statistics:**

Performed basic descriptive statistics to assess the distribution and variability of chromatin accessibility signals across all 29 samples (cell types). The minimum and maximum signal values in the dataset were found to be:

- **Min Signal:** 0.1  
- **Max Signal:** 727.42  

   - Computed per-sample statistics for the `Signal` column:
     - **Mean**
     - **Median**
     - **Standard Deviation (SD)**
     - **Coefficient of Variation (CV)** (calculated as `SD / Mean`)
     






- **Plots:**
  - `cv_distribution_density.png`: Overlaid density plot of CV for `abT` and `T.act`
  - `cv_boxplot.png`: Boxplot comparing signal variability across the two sample groups

### Summary
This step evaluates the overall consistency and variability of chromatin accessibility signals across all samples. Coefficient of Variation (CV) is used as the main metric to identify which samples are more stable or variable, which helps guide downstream quality filtering.


