
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# --------------------------------------------------
# 1. READ DWSIM RESULTS
# --------------------------------------------------

# Save all output files in the same folder as this script
OUTPUT_DIR = Path(__file__).resolve().parent

df = pd.read_excel(OUTPUT_DIR / "dwsim_results.xlsx")

# Check that required columns exist
required_columns = ["T", "Recovery", "Duty", "Recovered NMP"]
missing_columns = [
    col for col in required_columns if col not in df.columns
]

if missing_columns:
    raise ValueError(f"Missing columns in Excel file: {missing_columns}")

print("\nDWSIM Results:")
print(df.to_string(index=False))


# --------------------------------------------------
# GRAPH 1: TEMPERATURE VS SOLVENT RECOVERY
# --------------------------------------------------

fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(df["T"], df["Recovery"], marker="o")

ax.set_xlabel("Condenser Temperature (°C)")
ax.set_ylabel("Solvent Recovery (%)")
ax.set_title("Effect of Condenser Temperature on Solvent Recovery")
ax.grid(True, alpha=0.3)

fig.tight_layout()
fig.savefig(
    OUTPUT_DIR / "recovery_vs_temperature.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()
plt.close(fig)


# --------------------------------------------------
# GRAPH 2: TEMPERATURE VS COOLING DUTY
# --------------------------------------------------

fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(df["T"], df["Duty"], marker="o")

ax.set_xlabel("Condenser Temperature (°C)")
ax.set_ylabel("Cooling Duty (kW)")
ax.set_title("Effect of Condenser Temperature on Cooling Duty")
ax.grid(True, alpha=0.3)

fig.tight_layout()
fig.savefig(
    OUTPUT_DIR / "cooling_duty_vs_temperature.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()
plt.close(fig)


# --------------------------------------------------
# GRAPH 3: SOLVENT RECOVERY VS COOLING DUTY
# --------------------------------------------------

fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(df["Duty"], df["Recovery"], marker="o")

ax.set_xlabel("Cooling Duty (kW)")
ax.set_ylabel("Solvent Recovery (%)")
ax.set_title("Trade-off Between Solvent Recovery and Cooling Duty")
ax.grid(True, alpha=0.3)

# Label each point with its condenser temperature
for _, row in df.iterrows():
    ax.annotate(
        f'{row["T"]}°C',
        (row["Duty"], row["Recovery"]),
        xytext=(5, 5),
        textcoords="offset points",
        fontsize=8
    )

fig.tight_layout()
fig.savefig(
    OUTPUT_DIR / "recovery_duty_tradeoff.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()
plt.close(fig)


# --------------------------------------------------
# TRADE-OFF ANALYSIS
# --------------------------------------------------

# Sort by temperature descending so changes follow
# the sequence 50, 40, 30, 20, 10 °C
df = df.sort_values("T", ascending=False).reset_index(drop=True)

df["Recovery Improvement (percentage points)"] = (
    df["Recovery"].diff()
)

df["Duty Increase (kW)"] = df["Duty"].diff()

print("\nTrade-off Analysis:")
print(
    df[
        [
            "T",
            "Recovery",
            "Duty",
            "Recovery Improvement (percentage points)",
            "Duty Increase (kW)"
        ]
    ].round(4).to_string(index=False)
)


# --------------------------------------------------
# MATERIAL BALANCE VALIDATION
# --------------------------------------------------

# Feed NMP = total feed flow * feed NMP mass fraction
NMP_feed = 0.01 * 0.05  # kg/s

print("\nMaterial Balance Validation:")
print(f"Assumed NMP feed: {NMP_feed:.8f} kg/s")

# Recovered NMP should represent the NMP component mass
# flow in the recovered liquid, not total liquid flow.
# This calculation is only valid if the Excel column
# "Recovered NMP" contains that component mass flow.
if (df["Recovered NMP"] < 0).any():
    raise ValueError("Recovered NMP values cannot be negative.")

df["NMP Recovery Recalculated (%)"] = (
    df["Recovered NMP"] / NMP_feed * 100
)

# Do not calculate NMP loss as feed minus recovery and
# then claim the resulting balance error is zero.
# Obtain NMP component mass flow in the exhaust gas
# directly from DWSIM to independently close the balance.

print(
    "\nNMP recovery recalculated from the supplied "
    "'Recovered NMP' column:"
)
print(
    df[["T", "Recovered NMP", "NMP Recovery Recalculated (%)"]]
    .round(6)
    .to_string(index=False)
)

print(
    "\nIndependent balance check is pending: add the NMP "
    "component mass flow in the exhaust-gas stream from DWSIM."
)


# --------------------------------------------------
# SAVE ANALYSIS TABLES
# --------------------------------------------------

df.to_csv(OUTPUT_DIR / "solvent_recovery_analysis.csv", index=False)
df.to_excel(OUTPUT_DIR / "solvent_recovery_analysis.xlsx", index=False)

print("\nAnalysis files saved in:")
print(OUTPUT_DIR)

print("\nGenerated files:")
print("- recovery_vs_temperature.png")
print("- cooling_duty_vs_temperature.png")
print("- recovery_duty_tradeoff.png")
print("- solvent_recovery_analysis.csv")
print("- solvent_recovery_analysis.xlsx")
