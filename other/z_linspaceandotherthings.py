import numpy as np

# Given method: Calculate dt from t using np.diff
t_given = np.linspace(0, 5, 100)
dt_given = np.concatenate((t_given[0:1], np.diff(t_given)))

# Method 2: Calculate dt using T and M
I = 10**3  # number of simulations

# Calculate T and M
T_calculated = t_given[-1]  # Total time is the last value of t_given
M_calculated = len(t_given) -1  # Number of time steps

# Calculate dt using Method 2
dt_calculated = T_calculated / M_calculated

# Compare dt_given and dt_calculated
matching = np.allclose(dt_given, dt_calculated)

# print("Given method dt values:", dt_given)
# print("Method 2 calculated dt:", dt_calculated)
# print("Matching values:", matching)
print("T:", T_calculated)
print("M:", M_calculated)
# print(type(dt_given))
mean_absolute_difference = np.mean(np.abs(dt_given - dt_calculated))
# print('EWA?')
print(f"mean_absolute_difference: {mean_absolute_difference}")



# 0.00050505050505
# 0.0009999999999999972