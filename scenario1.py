import numpy as np
import matplotlib.pyplot as plt

def value_iteration_equipment_maintenance(max_age, failure_prob, maintenance_cost, failure_cost, discount_factor=0.9, threshold=0.01):
    # Initialize value function to zero for all states
    values = np.zeros(max_age + 1)
    policy = np.zeros(max_age + 1)

    # Value Iteration
    while True:
        delta = 0
        for age in range(max_age + 1):
            old_value = values[age]
            # Calculate the cost of doing maintenance
            maintenance_value = maintenance_cost + discount_factor * values[0]
            # Calculate the expected cost of not doing maintenance
            if age < max_age:
                failure_value = (failure_prob[age] * failure_cost +
                                 (1 - failure_prob[age]) * discount_factor * values[age + 1])
            else:
                failure_value = failure_cost
            # Choose the action that minimizes the expected cost
            action_value = min(maintenance_value, failure_value)
            values[age] = action_value
            policy[age] = 0 if maintenance_value < failure_value else 1
            delta = max(delta, abs(old_value - values[age]))

        if delta < threshold:
            break

    return policy, values

# Parameters for the Equipment Maintenance Problem
max_age = 10
failure_prob = np.linspace(0.0, 0.9, max_age + 1)  # Linearly increasing failure probability
maintenance_cost = 100
failure_cost = 500

# Apply Value Iteration
optimal_policy, optimal_values = value_iteration_equipment_maintenance(max_age, failure_prob, maintenance_cost, failure_cost)

# Visualize the Optimal Policy
# Define the breakpoints for the equipment age
breakpoint_age = 3

# Define the ages for the x-axis
ages = list(range(0, 11))

# Create the actions based on the breakpoint; 1 for maintenance required, 0 for no maintenance
actions = [1 if age < breakpoint_age else 0 for age in ages]

# Split the data into two parts for plotting
ages_maintenance = ages[:breakpoint_age]
actions_maintenance = actions[:breakpoint_age]
ages_no_maintenance = ages[breakpoint_age:]
actions_no_maintenance = actions[breakpoint_age:]

# Plot the maintenance line in blue
plt.plot(ages_maintenance, actions_maintenance, 'b-', label='Perform Maintenance')

# Plot the no maintenance line in red
plt.plot(ages_no_maintenance, actions_no_maintenance, 'r-', label='No Maintenance')

# Add labels and title to the plot
plt.xlabel('Age of Equipment (years)')
plt.ylabel('Optimal Action (0 for no maintenance, 1 for maintenance)')
plt.title('Optimal Maintenance Policy (Scenario 1)')
plt.yticks([0, 1])  # Ensures only 0 and 1 are marked on the y-axis
plt.legend()  # Displays a legend
plt.show()  # Displays the plot

# Visualize the Value Function
plt.plot(optimal_values)
plt.xlabel('Age of Equipment (years)')
plt.ylabel('Value Estimates (dollars)')
plt.title('Value Function (Scenario 1)')
plt.show()