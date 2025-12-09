**📦 Delivery Acceptance Correlation Analysis**

Analyzing the impact of SLA and pricing policy changes on delivery acceptance rates (Nov–Dec 2025)

**📌 Project Overview**
This project evaluates how two major operational and pricing interventions impacted driver acceptance behavior in a delivery platform.

**🔧 Policy Changes Introduced**

1️⃣ Updated Propose-Deadline Windows
Effective: December 1, 2025 (10 Azar 1404)
Objective: Provide more reasonable SLA windows to increase acceptance likelihood.

2️⃣ Pickup Price Increase
Effective: December 3, 2025 (12 Azar 1404)
Objective: Improve economic incentive for drivers to accept proposals.

**🎯 Goal:**
Improve delivery acceptance rate → improve SLA performance

**📊 Method:**
Correlation analysis before/after policy changes

**📊 Dataset**


The dataset includes operational-level features:

Accepted (target variable)

Pickup_Distance, Delivery_Distance, TotalDistance

Pickup_Cost, Delivery_Cost, TotalCost

VendorId and mapped vendor groups

StartProposeToDeadlineMinutes

Date_Key, Hour_Key

Vendor groups:

VendorId	Group Name
37	Supermarket_Okala
41	TosiFood
726	TapsiGrocery
Other	Other Vendors

**⚠️ Data Confidentiality Notice**

<span style="color:red; font-weight:bold;">Raw operational data is NOT included in this repository due to confidentiality restrictions.</span>

**🧪 Methodology**
Three correlation heatmaps were generated to analyze changes over time:

1️⃣ Pre-Change Window
📅 Nov 22–30 (1–9 Azar)

Baseline performance before SLA and pricing adjustments.

2️⃣ Post-Change Window
📅 Dec 1–6 (10–15 Azar)

After the propose-deadline modification and pickup cost increase.

3️⃣ Full Analysis Window
📅 Nov 22–Dec 6 (1–15 Azar)

Combined view to detect broader structural patterns.

**🎛 Preprocessing Notes**

NotApprovedBy dummy variables removed (they trivially correlate with acceptance = 0).

Features normalized for comparability.

Colormap: Red–White–Green

Dark Red: strong negative correlation

White: no correlation

Dark Green: strong positive correlation

**🔍 Key Insights**

⭐ 1. Pickup Price Increase Did Not Improve Acceptance

Across all time windows:
Pickup_Cost correlation with acceptance remained near zero (0.02–0.09).

➡️ Flat monetary incentives alone did not meaningfully change behavior.

⭐ 2. Delivery Distance Is the Main Driver of Rejection

Negative correlation remained stable:
Feature	Correlation (approx.)
Delivery_Distance	–0.30
TotalDistance	–0.29

➡️ Longer travel distance reduces willingness to accept—high predictive value.

⭐ 3. Vendor-Level SLA Rules Impact Acceptance More Than Pricing

TosiFood showed:
Extremely limited deadline minutes
Correlation ≈ –0.99 with StartProposeToDeadlineMinutes

➡️ The vendor’s SLA constraints strongly suppress acceptance regardless of pricing.

⭐ 4. Propose-Deadline Adjustments Had Limited Measurable Effect

Correlation between deadline minutes and acceptance:
Stayed weak (≈ 0.07–0.09) before vs. after the change.

➡️ Vendor-specific structural issues overshadow global SLA adjustments.


**📈 Visual Outputs**
Heatmaps (pre-change, post-change, and full window) are stored in:

reports/
└── figures/
    ├── heatmap_pre_change.png
    ├── heatmap_post_change.png
    └── heatmap_full_window.png

**🧠 Summary of Findings**

Operational changes alone were not enough to significantly impact acceptance.

Pricing incentives had minimal behavioral impact.

Distance remains the strongest predictor of acceptance.

Vendor-specific SLA constraints (e.g., TosiFood) have outsized influence compared to global SLA or pricing changes.

Future initiatives should focus on vendor-level SLA redesign, not generic global adjustments.

**📝 License**

MIT License

**👤 Author**

Nafise Ghahremani Gol

Product Data Analytics & Data Science

<span style="color:red; font-weight:bold;">📬 Contact available through GitHub profile
