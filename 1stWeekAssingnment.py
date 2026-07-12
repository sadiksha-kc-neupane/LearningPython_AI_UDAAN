
courses =["Python with AI/ML","Javascript","Flutter","MERN Stack"]
# print(courses)
for course in courses:
    print(course)

studentname = input("enter your name:" )
email = input("enter your email:")
age = input("enter your age:")
selectedcourse = input("enter your selectedcourse:")

studentinfo ={
    'Name': studentname,
    'Email': email,
    'Age': age,
    'Selectedcourse': selectedcourse
}
print(studentinfo)


if selectedcourse in courses: {
    print("Registration sucessful")
    }
else:
        print('course not available')
    
print ("Student Name is:", studentinfo['Name'])
print ("Student age is:", studentinfo['Age'])
print ("Student Email is:", studentinfo['Email'])
print ("Student selected course is:", studentinfo['Selectedcourse'])


i=0
while i<=10:
    print(i)
    i= i+1
