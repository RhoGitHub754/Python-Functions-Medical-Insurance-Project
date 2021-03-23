# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  output_message = "The estimated insurance cost for {} is £{}".format(name, estimated_cost)
  print(output_message)
  return output_message, estimated_cost

# DIfferences function to calculate differences between two insurance costs

def calculate_differences(insurance_cost1, insurance_cost2):
  if insurance_cost1 >= insurance_cost2:
    print("The difference in insurance cost is £{}".format(insurance_cost1[1] - insurance_cost2[1]))
  else:
    print("The difference in insurance cost is £{}".format(insurance_cost2[1] - insurance_cost1[1]))


# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost('Maria', 28, 0, 26.2, 3, 0)
 

# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost('Omar', 35, 1, 22.2, 0, 1)

rhoan_insurance_cost = calculate_insurance_cost('Rhoan', 36, 1, 20, 2, 0)

calculate_differences(maria_insurance_cost, omar_insurance_cost)
