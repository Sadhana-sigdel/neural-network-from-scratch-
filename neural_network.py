import math
study_hours = 0.4
attendance = 0.7

weight_study = 0.5
weight_attendance = 0.3

bias = 1

weighted_sum = (study_hours * weight_study) + (attendance * weight_attendance) + bias
print(weighted_sum)

output = 1 / (1 + math.exp(-weighted_sum))

print(output)