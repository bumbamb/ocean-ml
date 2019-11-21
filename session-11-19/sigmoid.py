import numpy as np

# Pick a decision you want to make. Pick a binary decision meaning
# you are chosing between two things
# Example: "Should I buy white sneakers instead of black sneakers?"
# or "Should I take AP chemistry?"  
decision = "Should i dye my hair"

# Pick three factors that affect your decision and write them as strings
factor_1 = "how long of a break"
factor_2 = "how much damage it has"
factor_3 = "what color"

# think about how much each of these factors matter
# create a numpy array of length 3 where the first
# value is how much the first factor matters, the 
# second value is how much the second factor matters
# etc:
weights = np.array([8,6,3])#your code here

# pick a value for the bias: explain to your partner what this means
bias = -7 # change this
# keep your weights and biases on the same scale
# for example if your weights are 6, 7, 9 don't make your bias 100

# now create a numpy array that says how likely you think each factor is.
# Pick values between 0 and 1:
# for example, if your fist factor is "my shoes will get dirty", 
# but you think that probably won't happen, the first value in  
# your array might be 0.10, meaning you think you are 10% likely to 
# get your shoes dirty
factor_values = np.array([1.20, 0.05, 0.40])# your code here

# now the perceptron is going to calculate the outcome. This is
# basically the same as the perceptron example except for the 
# line with the sigmoid_output variable

output_1 = np.dot(weights,factor_values) + bias
sigmoid_output = 1/(1+np.exp(-output_1))
out = sigmoid_output*100

# the rest of the code just prints this to output:
test_dict = {0 : "no", 1:"yes"}#{ 0 : "no",1 : "yes" }
print(decision)
print("*************************")
print(factor_1+": "+str(factor_values[0]*100)+"% | weight: "+ str(weights[0]))
print(factor_2+": "+str(factor_values[1]*100)+ "%| weight: "+ str(weights[1]))
print(factor_3+": "+str(factor_values[2]*100)+"% | weight: "+ str(weights[2]))
print("bias = "+str(bias))
print("*************************")
print("calculating decision ...")
print("*************************")
print("weighted sum = "+str(output_1))
print("sigma(weighted sum) = "+ str(sigmoid_output))
print("final decision: it is %.2f%% a good idea"%out)