# Equipment Maintenance Optimization

This repository contains two Python scripts that apply the Value Iteration algorithm, an reinforcement learning method, within Markov Decision Processes (MDPs) to optimize maintenance schedules.

## Files

- 'scenario1.py': Implements the Value Iteration algorithm for Scenario 1, focusing on a maintenance strategy that balances the costs and risks associated with equipment aging.
- 'scenario2.py': Adapts the Value Iteration algorithm for Scenario 2, where the costs of maintenance and risks of failure are adjusted to explore different strategic outcomes.

## Dependencies

To run these scripts, you need to have Python installed on your system along with the following libraries:
- numpy
- matplotlib

## Usage

To execute the scripts, navigate to the directory containing the scripts and run:

- python scenario1.py (or python3 scenario1.py)
- python scenario2.py (or python3 scenario2.py)

## Results

Running each script will generate plots that depict the optimal maintenance policy and value function for the respective scenario. These plots help in visualizing the decision-making process guided by the Value Iteration algorithm.
