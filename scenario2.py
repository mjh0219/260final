import numpy as np
import matplotlib.pyplot as plt

def value_iteration_equipment_maintenance(max_age, failure_prob, maintenance_cost, failure_cost, discount_factor=0.9, threshold=0.01):
    values = np.zeros(max_age + 1)
    policy = np.zeros(max_age + 1)

    while True:
        delta = 0
        for age in range(max_age + 1):
            old_value = values[age]
            maintenance_value = maintenance_cost + discount_factor * values[0]
            failure_value = failure_cost if age == max_age else (failure_prob[age] * failure_cost + (1 - failure_prob[age]) * discount_factor * values[age + 1])
            action_value = min(maintenance_value, failure_value)
            values[age] = action_value
            policy[age] = 0 if maintenance_value <= failure_value else 1
            delta = max(delta, abs(old_value - values[age]))
        if delta < threshold:
            break
    
    return policy, values

# Parameters for Scenario 2
max_age = 10
failure_prob = np.linspace(0.0, 0.9, max_age + 1)
maintenance_cost = 150  # Increased maintenance cost
failure_cost = 300      # Reduced failure cost

# Apply Value Iteration for Scenario 2
optimal_policy_2, optimal_values_2 = value_iteration_equipment_maintenance(max_age, failure_prob, maintenance_cost, failure_cost)

# Plotting for Scenario 2
plt.plot(optimal_policy_2, label='Perform Maintenance')
plt.title('Optimal Maintenance Policy (Scenario 2)')
plt.xlabel('Age of Equipment (years)')
plt.ylabel('Optimal Action (0 for no maintenance, 1 for maintenance)')
plt.yticks([0, 1])
plt.legend()
plt.show()

plt.plot(optimal_values_2)
plt.title('Value Function (Scenario 2)')
plt.xlabel('Age of Equipment (years)')
plt.ylabel('Value Estimates (dollars)')
plt.show()