def user_info(name,age=10,city='Macau'):
    '''here in function we have provided the arguments,
    this function prints name, age and city from an argument provided to a city'''

    print("{} is {} years old, living in {} city".format(name, age, city))

user_info("giridhar",26,"pune")
user_info("hrithik")
user_info(age=25,city="NewYork",name="rajesh")


