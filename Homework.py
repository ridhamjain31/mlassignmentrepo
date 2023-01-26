ages=[19,22,19,24,20,25,26,24,25,24]
x=min(ages)
y=max(ages)
ages.sort()
print(ages)
print('Minimum age is',x)
print('Maximum age is',y)
ages.insert(10,x)
ages.insert(11,y)
print(ages)
z=(sum(ages))/(len(ages))
print('Average is',z)
a=(y-x)
print('Range is',a)

#Create an empty dictionary called dog

dog={}
print(dog)
#Add name, color, breed, legs, age to the dog dictionary
dog['name']=''
dog['age']=''
dog['breed']=''
dog['legs']=''
dog['color']=''
print(dog)
#Create a student dictionary and add first_name, last_name, gender, age, marital status,
#skills, country, city and address as keys for the dictionary
student_dictionary={"first_name":"","last_name":"","gender":"","age":"","marital_status":"","skills":[''],"country":"","city":"","address":""}
print(student_dictionary)
length=(len(student_dictionary))
print("length of dictionary is ",length)
skills_value=(student_dictionary["skills"])
print("value of skills is ",skills_value)
data_type=(type(student_dictionary["skills"]))
print(data_type)
student_dictionary['skills']=['dance','sing']
print(student_dictionary)
values=student_dictionary.values()
print(values)
keys=student_dictionary.keys()
print(keys)

brothers=("Abhi","Shubham","Ricky")
sisters=("Mansi","Aarzoo")
siblings=brothers+sisters
print(siblings)
num=len(siblings)
print("Number of siblings are",num)
family_members=siblings+("Asha","Ghanshyam")
print(family_members)




it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#Find the length of the set it_companies
print("Length of set it companies is", len(it_companies))
#Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)
#Insert multiple IT companies at once to the set it_companies
it_companies2={"Sony","LG","Samsung"}
it_companies.update(it_companies2)
print(it_companies)
#Remove one of the companies from the set it_companies
it_companies.remove("LG")
print(it_companies)
#What is the difference between remove and discard
it_companies.discard("LG")
print(it_companies)
#Join A and B
A2=A.union(B)
print(A2)
#Find A intersection B
A1=A.intersection(B)
print(A1)
#Is A subset of B
subset=(A.issubset(B))
print("Is A subset of B: ",subset)
#Are A and B disjoint sets
disjoint=A.isdisjoint(B)
print("Are A and B disjoint:",disjoint)
#Join A with B and B with A
A2=A.union(B)
print(A2)
B2=B.union(A)
print(B2)
#What is the symmetric difference between A and B
sym_diff=A.symmetric_difference(B)
print("Symm Difference is", sym_diff)
#del the sets completely
del(A)
del(B)
#Convert the ages to a set and compare the length of the list and the set
len_age=len(age)
print("length of age list is:",len_age)
age_set=set(age)
print("length of age set is:",len(age_set))










Radius=30
import math
_area_of_circle_=(math.pi*Radius*Radius)
print('Area of circle is',_area_of_circle_,'m2')
_circum_of_circle_=(2*math.pi*Radius)
print('Circumference of a circle is',_circum_of_circle_,'m')


"""“I am a teacher and I love to inspire and teach people”
• How many unique words have been used in the sentence? Use the split methods and set
to get the unique words"""
statement="I am a teacher and I love to inspire and teach people"
unique_words = set(statement.split())
print(unique_words) 

length = len(unique_words)
print(length)


"""Use a tab escape sequence to get the following lines.
Name Age Country City
Asabeneh 250 Finland Helsinki"""
print("Name\t       Age\t    Country\t    City  \nAsabeneh\t250\t  Finland\t   Helsinki")


"""Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
“The area of a circle with radius 10 is 314 meters square.”"""
print('radius = 10\narea = 3.14 * radius ** 2\n"The area of a circle with radius 10 is 314 meters square."')


number_of_students=input("Enter the students: ")
list_of_weigth_kg=[]
for x in  range(int(number_of_students)):
    weight=input("Enter the weight(lbs) of student " + str((x+1)) +': ')
    list_of_weigth_kg.append(round(int(weight) * .45352,2))

print(list_of_weigth_kg)