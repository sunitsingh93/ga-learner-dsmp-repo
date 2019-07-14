# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
#path = "SUBSEET_1000.csv"
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data = np.genfromtxt(path,delimiter=",",skip_header =1)
print(data)
print(data.shape)
census = np.concatenate((data,new_record),axis =0)
print(census)
print(census.shape)


# --------------
#Code starts here
age = np.asarray(census[:,:1], dtype = 'int32')
print(age)
max_age = np.max(age)
print(max_age)
min_age = np.min(age)
print(min_age)
age_mean = np.mean(age)
print(age_mean)
age_std = np.std(age)
print(age_std)


# --------------
#Code starts here
race_0 = census[census[:,2] == 0]
#print(race_0)
race_1 = census[census[:,2] == 1]
#print(race_1)
race_2 = census[census[:,2] == 2]
#print(race_2)
race_3 = census[census[:,2] == 3]
#print(race_3)
race_4 = census[census[:,2] == 4]
#print(race_4)

len_0 = len(race_0)
print(len_0)
len_1 = len(race_1)
print(len_1)
len_2 = len(race_2)
print(len_2)
len_3 = len(race_3)
print(len_3)
len_4 = len(race_4)
print(len_4)

rec_list =[len_0, len_1, len_2, len_3, len_4]
minority_race = rec_list.index(min(rec_list))

#minority_race = min(len_0,len_1,len_2,len_3,len_4)
print(minority_race)


# --------------
#Code starts here
senior_citizens = np.array(census[census[:,0] > 60],dtype ='int32')
#print(senior_citizens)
working_hours_sum = senior_citizens.sum(axis=0)[6]
print(working_hours_sum)
senior_citizens_len = len(senior_citizens)
print(senior_citizens_len)
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high = census[census[:,1] > 10]
#print(high)
low = census[census[:,1] <= 10]
avg_pay_high = high.mean(axis=0)[7]
print(avg_pay_high)
avg_pay_low = low.mean(axis=0)[7]
print(avg_pay_low)


