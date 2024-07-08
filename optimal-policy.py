
## objective: print out the optimal policy at each temperature

##### extra functions #####

## this function allows us to iterate through floats
def drange2(start, stop, step):
    numelements = int((stop-start)/float(step))
    for i in range(numelements+1):
            yield start + i*step

# returns the value function at the given temperature by turning the heating on
def heatingOn(temp):
    # initialize parameters
    probIncreaseSmall = 0.5 # prob of going up 0.5 C
    probIncreaseBig = 0.2 # prob of going up 1 C
    probDecreaseSmall = 0.1 # prob of going down 0.5 C
    probStay = 0.2 # prob of staying at the same temp
    cost = actions["heatingOn"]
    #special cases
    if temp == 16.0:
        probStay = 0.3
        probDecreaseSmall = 0
    elif temp == 24.5:
        probIncreaseSmall = 0.7
        probIncreaseBig = 0
    elif temp == 25:
        probStay = 0.9
        probIncreaseSmall = 0
        probIncreaseBig = 0
    #find the value function
    value = cost + probIncreaseSmall*temperatures[temp+0.5][0] + probIncreaseBig*temperatures[temp+1.0][0] \
            + probDecreaseSmall*temperatures[temp-0.5][0] + probStay*temperatures[temp][0]
    return value

# returns the value function at the given temperature by turning the heating off
def heatingOff(temp):
    # initialize parameters
    probIncreaseSmall = 0.1 # prob of going up 0.5 C
    probDecreaseSmall = 0.7 # prob of going down 0.5 C
    probStay = 0.2 # prob of stating at the same temp
    cost = actions["heatingOff"]
    #special cases
    if temp == 16.0:
        probStay = 0.9
        probDecreaseSmall = 0
    elif temp == 25.0:
        probStay = 0.3
        probIncreaseSmall = 0
    #find the value function
    value = cost + probIncreaseSmall*temperatures[temp+0.5][0] \
            + probDecreaseSmall*temperatures[temp-0.5][0] + probStay*temperatures[temp][0]
    return value

##### actual algorithm #########

### calculates the value function for each temperature
def calculateValueFunction(temperatures, goalState):
    converged = False
    while not converged:
        converged = True
        #update new values
        for temp in temperatures:
            if temp == goalState or temp == 15.0 or temp == 15.5 or temp == 25.5 or temp == 26.0:
                continue
            heatingOnValue = heatingOn(temp) # returns the value function at the given temperature by turning the heating on
            heatingOffValue = heatingOff(temp) # # returns the value function at the given temperature by turning the heating off
            bestAction = min(heatingOnValue, heatingOffValue) # gives us the value of the best action to take
            temperatures[temp][1] = bestAction # update the new value of each temperature with the newly calculated value
        #update old values
        for temp in temperatures:
            if converged and temperatures[temp][0] != temperatures[temp][1]: converged = False # we know the function has not converged if the oldValue != newValue for all values, else we know it has converged
            temperatures[temp][0] = temperatures[temp][1] # update the old value with the new value

# finds the optimal policy for each temperature
def findOptimalPolicy(temperatures, goalState):
    calculateValueFunction(temperatures, goalState) #calcualte the value function for each temp
    for temp in temperatures:
        if temp == 15.0 or temp == 15.5 or temp == 25.5 or temp == 26.0: continue
        if temp == goalState:
            temperatures[temp][2] = "Goal State"
        else:
            heatingOnValue = heatingOn(temp) # returns the value function at the given temperature by turning the heating on
            heatingOffValue = heatingOff(temp) # # returns the value function at the given temperature by turning the heating off
            if heatingOnValue >= heatingOffValue:
                temperatures[temp][2] = "Turn Heat Off"
            else: # heatingOnValue < heatingOffValue
                temperatures[temp][2] = "Turn Heat On"
        print(temp, temperatures[temp][2])


##### initialize everything #######

#format --> temp : [old Value, new Value]
temperatures = { temp:[0,0,None] for temp in drange2(15.0, 26.0, 0.5) }  # a dictionary with all the temperatrues and their [oldValue, newValue] 
# actions
actions = { "heatingOn" : 20, "heatingOff" : 10} #actions with their costs
#goal state which must be within 16.0 and 25.0 and must end on 0.5
goalState = 22.0


#testing
findOptimalPolicy(temperatures, goalState)


