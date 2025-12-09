"""
Correlation Analysis for Delivery Proposal Acceptance
-----------------------------------------------------

This script analyzes driver acceptance behavior before and after
two major operational policy changes:

1. Updated propose-deadline windows (effective Dec 1, 2025)
2. Increased pickup price (effective Dec 3, 2025)

Goal:
    Identify whether the interventions improved acceptance rate,
    and determine which variables actually influence acceptance.

Author: Nafise Ghahremani Gol
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# -------------------------------------------
# Load Dataset
# -------------------------------------------
file_path = r"D:\Docs\QURIES\Changeon Proposed.xlsx"
df = pd.read_excel(file_path)

# -------------------------------------------
# Correlation Plotting Function
# -------------------------------------------
def plot_corr_for_subset(df_subset, title_suffix=""):
    """
    Computes and visualizes correlations between key operational
    variables and delivery acceptance for a given time window.
    """
    
    df_sub = df_subset.copy()

    # --------------------------
    # Vendor Mapping
    # --------------------------
    vendor_map = {
        37: "Supermarket_Okala",
        41: "TosiFood",
        726: "TapsiGrocery"
    }
    df_sub["VendorGroup"] = df_sub["VendorId"].map(vendor_map).fillna("Other")
    vendor_dummies = pd.get_dummies(df_sub["VendorGroup"], prefix="Vendor")

    # --------------------------
    # NotApproved Mappings (removed from correlation)
    # --------------------------
    not_approved_map = {
        70: "DeclineByDriver",
        75: "DeclineByReminder"
    }
    df_sub["NotApprovedLabel"] = df_sub["NotApprovedby"].map(not_approved_map).fillna("OtherOrApproved")
    not_approved_dummies = pd.get_dummies(df_sub["NotApprovedLabel"], prefix="NA")

    # Remove NA_* (to avoid trivial correlation)
    cols_to_drop = ["NA_DeclineByDriver", "NA_DeclineByReminder", "NA_OtherOrApproved"]
    not_approved_dummies = not_approved_dummies.drop(columns=[c for c in cols_to_drop if c in not_approved_dummies])

    # --------------------------
    # Numeric Variables
    # --------------------------
    base_numeric_cols = [
        "Accepted",
        "Pickup_Cost",
        "Delivery_Cost",
        "TotalCost",
        "Pickup_Distance",
        "Delivery_Distance",
        "TotalDistance",
        "StartProposeToDeadlineMinutes"
    ]
    base_numeric_cols = [c for c in base_numeric_cols if c in df_sub.columns]

    df_numeric = df_sub[base_numeric_cols]

    if df_numeric.shape[0] < 2:
        print(f"[WARNING] Not enough rows to compute correlation for {title_suffix}")
        return

    # --------------------------
    # Combine variables
    # --------------------------
    df_corr_input = pd.concat(
        [df_numeric, vendor_dummies, not_approved_dummies],
        axis=1
    ).dropna(how="all")

    correlation_matrix = df_corr_input.corr()
    print(f"\nCorrelation Matrix — {title_suffix}:\n", correlation_matrix)

    # --------------------------
    # Custom red–white–green colormap
    # --------------------------
    colors = [
        (0.8, 0.0, 0.0),  # Dark red for strong negative correlation
        (1.0, 1.0, 1.0),  # White for neutral correlation
        (0.0, 0.5, 0.0)   # Dark green for strong positive correlation
    ]
    cmap = LinearSegmentedColormap.from_list("red_white_green", colors)

    # --------------------------
    # Plot Heatmap
    # --------------------------
    plt.figure(figsize=(12, 8))
    sns.heatmap(
        correlation_matrix,
        annot=True,
        fmt=".2f",
        cmap=cmap,
        vmin=-1,
        vmax=1,
        center=0
    )
    plt.title(f"Correlation Analysis — {title_suffix}", fontsize=16)
    plt.tight_layout()
    plt.show()


# -------------------------------------------
# Time Windows (Gregorian ↔ Persian)
# -------------------------------------------
# 1 Azar 1404 → 22 Nov 2025
# 9 Azar 1404 → 30 Nov 2025
# 10 Azar 1404 → 1 Dec 2025
# 15 Azar 1404 → 6 Dec 2025

mask_1_to_9_azar = (df["Date_Key"] >= 20251122) & (df["Date_Key"] <= 20251130)
mask_10_to_15_azar = (df["Date_Key"] >= 20251201) & (df["Date_Key"] <= 20251206)
mask_1_to_15_azar = (df["Date_Key"] >= 20251122) & (df["Date_Key"] <= 20251206)

df_1_to_9_azar = df.loc[mask_1_to_9_azar]
df_10_to_15_azar = df.loc[mask_10_to_15_azar]
df_1_to_15_azar = df.loc[mask_1_to_15_azar]

# -------------------------------------------
# Generate Heatmaps
# -------------------------------------------
plot_corr_for_subset(df_1_to_9_azar,  "Nov 22–30 (Before Changes)")
plot_corr_for_subset(df_10_to_15_azar, "Dec 1–6 (After Changes)")
plot_corr_for_subset(df_1_to_15_azar, "Nov 22–Dec 6 (Full Window)")
