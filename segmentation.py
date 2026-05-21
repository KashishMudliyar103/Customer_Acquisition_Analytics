import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("Data/BankChurners.csv")

# -----------------------------
# RFM Analysis
# -----------------------------
# Recency proxy: Months_Inactive_12_mon
# Frequency: Total_Trans_Ct
# Monetary: Total_Trans_Amt

rfm = df[[
    "CLIENTNUM",
    "Months_Inactive_12_mon",
    "Total_Trans_Ct",
    "Total_Trans_Amt"
]].copy()

rfm.columns = [
    "customer_id",
    "recency_raw",
    "frequency",
    "monetary"
]

# -----------------------------
# RFM Scoring
# -----------------------------

# Recency Score
# duplicates='drop' prevents qcut errors
r_labels = range(5, 0, -1)

rfm["R"] = pd.qcut(
    rfm["recency_raw"].rank(method="first"),
    q=5,
    labels=r_labels
)

# Frequency Score
f_labels = range(1, 6)

rfm["F"] = pd.qcut(
    rfm["frequency"].rank(method="first"),
    q=5,
    labels=f_labels
)

# Monetary Score
m_labels = range(1, 6)

rfm["M"] = pd.qcut(
    rfm["monetary"].rank(method="first"),
    q=5,
    labels=m_labels
)

# Convert to integer
rfm["R"] = rfm["R"].astype(int)
rfm["F"] = rfm["F"].astype(int)
rfm["M"] = rfm["M"].astype(int)

# Final RFM Score
rfm["RFM_Score"] = rfm["R"] + rfm["F"] + rfm["M"]

# -----------------------------
# Segment Mapping
# -----------------------------
def segment_label(score):
    if score >= 13:
        return "Champions"
    elif score >= 10:
        return "Loyal Customers"
    elif score >= 7:
        return "Potential Loyalists"
    elif score >= 5:
        return "At Risk"
    else:
        return "Lost"

rfm["Segment"] = rfm["RFM_Score"].apply(segment_label)

# -----------------------------
# K-Means Clustering
# -----------------------------
features = df[[
    "Customer_Age",
    "Credit_Limit",
    "Total_Trans_Ct",
    "Total_Trans_Amt",
    "Avg_Utilization_Ratio"
]].dropna()

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# Train KMeans
kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

features = features.copy()

features["Cluster"] = kmeans.fit_predict(X_scaled)

# Cluster Labels
cluster_names = {
    0: "Low-Value Inactive",
    1: "High-Value Active",
    2: "Mid-Value Regular",
    3: "Young New Users"
}

features["Cluster_Label"] = features["Cluster"].map(cluster_names)

# -----------------------------
# Save Outputs
# -----------------------------
rfm_out = rfm[[
    "customer_id",
    "R",
    "F",
    "M",
    "RFM_Score",
    "Segment"
]]

cluster_out = features[[
    "Customer_Age",
    "Credit_Limit",
    "Total_Trans_Ct",
    "Total_Trans_Amt",
    "Avg_Utilization_Ratio",
    "Cluster_Label"
]]

with pd.ExcelWriter("Data/segmentation_output.xlsx") as writer:
    rfm_out.to_excel(
        writer,
        sheet_name="RFM_Segments",
        index=False
    )

    cluster_out.to_excel(
        writer,
        sheet_name="KMeans_Clusters",
        index=False
    )

# -----------------------------
# Visualization
# -----------------------------
seg_counts = rfm["Segment"].value_counts()

plt.figure(figsize=(8, 4))

sns.barplot(
    x=seg_counts.index,
    y=seg_counts.values,
    hue=seg_counts.index,
    palette="Blues_d",
    legend=False
)

plt.title("Customer Segments by RFM Score")
plt.xlabel("Segment")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig(
    "Data/segment_distribution.png",
    dpi=150
)

plt.show()

print("Segmentation complete.")
print("Files saved successfully in Data folder.")