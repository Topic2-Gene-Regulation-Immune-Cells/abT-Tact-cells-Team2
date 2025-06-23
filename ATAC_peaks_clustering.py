#!/usr/bin/env python3

#!/usr/bin/env python3
"""
run_kmeans.py

Performs K-Means clustering on your ATAC-seq peak matrix,
then visualizes the clusters with PCA, UMAP and t-SNE.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from umap import UMAP

def main():
    # 1) LOAD YOUR DATA
    # Replace these paths with wherever you have your CSVs:
    peak_matrix = pd.read_csv("ATAC-seq/filtered_ATAC_abT_Tact_Stem.csv", index_col=0).T
    
    
    # 2) STANDARDIZE
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(peak_matrix)
    
    # 3) K-MEANS CLUSTERING
    kmeans = KMeans(n_clusters=3, random_state=42, n_init="auto")
    cluster_labels = kmeans.fit_predict(scaled_data)
    
    # 4) BUILD A DATAFRAME OF RESULTS
    cluster_df = pd.DataFrame(
        scaled_data,
        index=peak_matrix.index,
        columns=peak_matrix.columns
    )
    cluster_df["Cluster"] = cluster_labels.astype(str)
    # If pca_df["Group"] exists and lines up index-wise:
    cluster_df["Group"]   = pca_df["Group"]
    
    # 5) DIMENSIONALITY REDUCTIONS
    # PCA
    pca = PCA(n_components=2, random_state=42)
    cluster_df[["PC1", "PC2"]] = pca.fit_transform(scaled_data)
    
    # UMAP
    umap_result = UMAP(n_components=2, random_state=42).fit_transform(scaled_data)
    cluster_df[["UMAP1", "UMAP2"]] = umap_result
    
    # t-SNE (ensure perplexity < n_samples)
    tsne = TSNE(n_components=2, random_state=42, perplexity=5)
    tsne_result = tsne.fit_transform(scaled_data)
    cluster_df[["tSNE1", "tSNE2"]] = tsne_result
    
    # 6) PLOT SIDE-BY-SIDE
    sns.set(style="whitegrid")
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    sns.scatterplot(
        data=cluster_df, x="PC1", y="PC2",
        hue="Cluster", palette="tab10", ax=axes[0], s=60
    )
    axes[0].set_title("PCA - KMeans Clusters")
    
    sns.scatterplot(
        data=cluster_df, x="UMAP1", y="UMAP2",
        hue="Cluster", palette="tab10", ax=axes[1], s=60
    )
    axes[1].set_title("UMAP - KMeans Clusters")
    
    sns.scatterplot(
        data=cluster_df, x="tSNE1", y="tSNE2",
        hue="Cluster", palette="tab10", ax=axes[2], s=60
    )
    axes[2].set_title("t-SNE - KMeans Clusters")
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()


