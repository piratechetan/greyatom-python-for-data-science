# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
data = data.reshape(1000,8)
census = np.concatenate((new_record,data))
census = census.reshape(1001,8)

age = np.array(census[:,0])
max_age = max(age)
print(max_age)
min_age = min(age)
print(min_age)
age_mean = np.mean(age)
age_mean = np.round(age_mean,2)
print(age_mean)
age_std = np.std(age)
age_std = np.round(age_std,2)
print(age_std)
race =np.array(census[:,2])
race_0 = census[census[:,2]==0]
race_1 = census[census[:,2]==1]
race_2 = census[census[:,2]==2]
race_3 = census[census[:,2]==3]
race_4 = census[census[:,2]==4]

len_0 = len(race_0)       
len_1 = len(race_1) 
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
if len_0 < len_1 and len_0 < len_2 and len_0 < len_3 and len_0 < len_4:
    minority_race = 0

elif len_1 < len_2 and len_1 < len_3 and len_1 < len_4 and len_1 < len_0:
    minority_race = 1

elif len_2 < len_3 and len_2 < len_4 and len_2 < len_0 and len_2 < len_1:
    minority_race = 2

elif len_3 < len_4 and len_3 < len_0 and len_3 < len_1 and len_3 < len_2:
    minority_race = 3

elif len_4 < len_0 and len_4 < len_1 and len_4 < len_2 and len_4 < len_3:
    minority_race = 4
print(minority_race)

senior_citizens = census[census[:,0] > 60]
working_hours_sum = senior_citizens.sum(axis=0)[6]
senior_citizens_len = len(senior_citizens)
avg_working_hours = np.round(working_hours_sum/senior_citizens_len,2)
print(working_hours_sum)
print(avg_working_hours)

high = census[census[:,1]>10]
low =  census[census[:,1]<=10]
avg_pay_high = np.round(high.mean(axis=0)[7],2)
avg_pay_low= np.round(low.mean(axis=0)[7],2)

print(avg_pay_high)
print(avg_pay_low)
 



