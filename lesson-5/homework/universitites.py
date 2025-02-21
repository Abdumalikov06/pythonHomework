def enrollment_stats(universities):
    enrollment_values = []
    tuition_fees = []
    for university in universities:
        enrollment_values.append(university[1])
        tuition_fees.append(university[2])
    return enrollment_values, tuition_fees
def mean(value):
    if value:
        return round(sum(value)/len(value),2)
    else:
        return 0
def median(value):
    value.sort()
    l_values=len(value)
    if l_values%2==0:
        middle_value1=value//2-1
        middle_value2=value//2
        middle_value=(middle_value1+middle_value2)/2
        return middle_value
    else:
        return value[l_values//2]

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
enrollment, tuition_fee =enrollment_stats(universities)
#sum of students and tuition fee
sum_enrollment=sum(enrollment)
sum_tuition=sum(tuition_fee)

#mean of students and tuition fee
mean_students=mean(enrollment)
mean_tuition=mean(tuition_fee)

#median of students and tuition fee
median_students=median(enrollment)
median_tuition=median(tuition_fee)
print('*'*30)
print("Total students:",sum_enrollment)
print("Total tuition: $",sum_tuition,'\n')

print("Students mean:", mean_students)
print("Student median:",median_students,'\n')

print("Tuition mean: $",mean_tuition)
print("Tuition median: $", median_tuition)
print('*'*30)



        