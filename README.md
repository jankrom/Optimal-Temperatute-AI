# Value Iteration Algorithm for Optimal Heating Policy

This Python script uses the value iteration algorithm to find the optimal policy for heating a space based on the temperature range between 16°C and 25°C. The cost of heating being on or off is factored into the calculation to determine the most cost-effective strategy.
## Features

- Calculates the optimal heating policy for each temperature between 16°C and 25°C (in 0.5 intervals).
- Costs for heating on and heating off are set at 20 and 10 respectively but can be easily adjusted.
- Outputs the optimal policy directly in the terminal.

## Model

The implemented algorithm follows this MDP model:
![alt text](https://github.com/jankrom/Optimal-Temperatute-AI/blob/main/mdp_model.png?raw=true)

There are some exceptions to the transition probabilities given in the model:
  - Heating on exceptions:
      - If CT == 16.0:
          - P(CT | CT, H) = 0.3
          - P(CT+0.5 | CT, H) = 0.5
          - P(CT+1 | CT, H) = 0.2
          - P(CT-0.5 | CT, H) = 0
      - If CT == 24.5:
          - P(CT | CT, H) = 0.2
          - P(CT+0.5 | CT, H) = 0.7
          - P(CT+1 | CT, H) = 0
          - P(CT-0.5 | CT, H) = 0.1
      - If CT == 25.0:
          - P(CT | CT, H) = 0.9
          - P(CT+0.5 | CT, H) = 0
          - P(CT+1 | CT, H) = 0
          - P(CT-0.5 | CT, H) = 0.1
    
  - Heating off exceptions:
    - If CT == 16.0:
      - P(CT | CT, HF) = 0.9
      - P(CT+0.5 | CT, HF) = 0.1
      - P(CT+1 | CT, HF) = 0
      - P(CT-0.5 | CT, HF) = 0
    - If CT == 25.0:
      - P(CT | CT, HF) = 0.3
      - P(CT+0.5 | CT, HF) = 0
      - P(CT+1 | CT, HF) = 0
      - P(CT-0.5 | CT, HF) = 0.7


## Requirements

- Python 3.x

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/jankrom/Optimal-Temperatute-AI.git
    ```

2. Run the script:
    ```bash
    python3 optimal-policy.py
    ```

3. The optimal heating policy for each temperature will be printed in the terminal.

## Customization

You can easily adjust the temperature range and the costs of heating on and off at the bottom of the script. Simply modify the values as needed:

```python
# Adjustable parameters at the bottom of the script
actions = { "heatingOn" : 20, "heatingOff" : 10} #actions with their costs
#goal state which must be within 16.0 and 25.0 and must end on 0.5
goalState = 22.0
```

## Example Output

```python
16.0 Turn Heat On
16.5 Turn Heat On
17.0 Turn Heat On
...
...
25.0 Turn Heat Off
```



