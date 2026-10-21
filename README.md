# Battery Solvent Recovery Optimization Using DWSIM

## Project Overview

This project studies the effect of cooling temperature on N-Methyl-2-pyrrolidone (NMP) recovery from a hypothetical lithium-ion battery electrode drying exhaust.

I built a steady-state process flowsheet in DWSIM using a cooler followed by a gas–liquid separator. The objective is to examine how changing the cooler outlet temperature affects NMP condensation and cooling duty. I also used Python to process the simulation results and generate graphs for comparing operating conditions.

## Process Flowsheet

**Feed → Cooler → Gas–liquid separator**

- **Feed:** A hypothetical exhaust stream containing NMP, nitrogen, and oxygen.
- **Cooler:** Lowers the stream temperature to promote NMP condensation.
- **Separator:** Separates the condensed liquid from the remaining exhaust gas.

The simulation uses the NRTL property method. The cooler outlet temperature is varied while the feed conditions are kept constant to study its effect on solvent recovery and cooling requirements.

## Feed Conditions

The feed conditions used in the DWSIM simulation are listed below. The composition and operating conditions are assumed for this preliminary study.

| Parameter | Value |
|---|---:|
| Feed temperature | 80 °C |
| Feed pressure | 101.325 kPa |
| Feed mass flow rate | 0.01 kg/s |
| NMP mass fraction | 0.05 |
| Nitrogen mass fraction | 0.76 |
| Oxygen mass fraction | 0.19 |
| Property method | NRTL |

## Python Analysis

Python, Pandas, and Matplotlib are used to organize the simulation results and generate three plots:

- **Recovery vs. temperature:** Shows how NMP recovery changes with cooler outlet temperature.
- **Cooling duty vs. temperature:** Compares the cooling requirement at different outlet temperatures.
- **Recovery–duty trade-off:** Examines the relationship between solvent recovery and cooling duty.

These comparisons help assess whether the additional cooling required at lower temperatures is justified by the improvement in solvent recovery.

## Tools Used

- DWSIM — Process simulation and flowsheet development
- Python — Data analysis
- Pandas — Data processing
- Matplotlib — Data visualization
- Microsoft Excel — Simulation results

## Project Files

- `battery-solvent-recovery-optimization-backup.dwxmz` — DWSIM simulation file
- `solvent_recovery_analysis.py` — Python analysis script
- `dwsim_results.xlsx` — Simulation results
- `solvent_recovery_analysis.csv` — Tabular analysis data
- `recovery_vs_temp.png` — Recovery versus temperature graph
- `cooling_duty_vs_temperature.png` — Cooling duty versus temperature graph
- `recovery-duty-tradwoff.png` — Recovery–duty trade-off graph


## Limitations and Further Work

The simulation provides stream flow rates and composition estimates for the recovered liquid and exhaust gas. Further validation is needed to confirm the NMP component mass flow in each outlet stream and verify overall material balance closure. The predicted phase equilibrium also depends on the selected thermodynamic model and its parameters.

Further work could include testing a wider temperature range, calculating energy consumption per unit of NMP recovered, and evaluating the economic trade-off between cooling requirements and solvent recovery.

## Disclaimer

This is an academic simulation using illustrative operating conditions. The results are not validated industrial performance data.



