
'''IMPORTANT'''
'''Q1'''
# a) aggregation with mapping
def is_all_has_a(words:list)->bool:
    '''Given a list of words check if "all" words has the letter a(case insensitive) in it.''' 
    return all(list(map(lambda x: 'a' in x.lower() ,words)))
    
words = ['that', 'apple' , 'was' , 'tasty']
print(is_all_has_a(words))


# b) zip 
def parallel_print(countries, capitals):
    '''
    Print the countries and capitals in multiple line seperated by a hyphen with space around it.'''
    zip_list = list(zip(countries,capitals))  # zip packed the countries list element and capital list element in a tuple.
    for el in zip_list:
        print(f"{el[0]}-{el[1]}")

countries = ["United States", "Brazil", "Nigeria", "India", "Australia"]
capitals = ["Washington D.C.","Brasilia", "Abuja", "New Delhi", "Canberra"]

parallel_print(countries , capitals)


'''VIEW'''
'''Q2 - '''
# enumerate with filtering and map
def indices_of_big_words(l) -> list:
    '''Given a list of words, find the indices of the big words(length greater than 5).
    '''
    # return [i for i in range(len(l)) if(len(l[i]) > 5)]
    result = list(filter(lambda x : len(x[1]) > 5 , enumerate(l)))   # enumerate return a tuple of el of l(index , value)
    res = list(map(lambda x : x[0], result))
    return res


print(indices_of_big_words(countries))


# zip with mapping and aggregation
def decode_rle(chars:str, repeats:list)->str:
    '''
    Create a string with i-th char from chars repeated i-th value of repeats number of times. 

    Note rle refers to Run-length encoding
    '''
    return "".join([chars[i]*repeats[i] for i in range(len(repeats))])

print(decode_rle('abcd',[1,2,3,4]))


#Grpa 5
'''Q3 - '''
# a)
def groupby(data:list, key:callable):
    '''
    Given a list of items, and a key, create a dictionary with the key as key function called 
    on item and the list of items with the same key as the corresponding value. 
    The order of items in the group should be the same order in the original list
    '''
    keys = sorted(set([key(item) for item in data]))
    d = {key : [] for key in keys}

    for el in data:
        for key in d:
            if(el[0] == key):
                d[key].append(el)
    return d

fruits = ["Apple","Banana","Avocado","Amla","Black berry","Blue berry"]
print(groupby(fruits , lambda x : x[0]))   # key is a function called on item and return the first letter of item


# b)
def apply_to_groups(groups , key_func):
    '''Apply a function to the list of items(values of dict) for each group.'''
    return {key : key_func(value) for key, value in groups.items()}


groups = {
"A":["Apple","Avocado"],
"B":["Banana","Blackberry","Blueberry"]
}

print(apply_to_groups(groups , "-".join))



'''Q4 - '''
import random
def generate_student_data(n_students, courses, cities, random_seed=42):
    '''
    Create a list of dict with dictionaries representing each attributes of each student.
    '''
    random.seed(random_seed)
    return [
      {
        "rollno": i, "city": random.choice(cities), 
        **{course: random.randint(1,100) for course in courses} 
      }
      for i in range(1,n_students+1)
    ]
'''sample'''
# [
# {'rollno': 1, 'city': 'delhi', 'CT': 4, 'python': 95, 'stats': 36, 'maths': 32}, 
# {'rollno': 2, 'city': 'chennai', 'CT': 18, 'python': 95, 'stats': 14, 'maths': 87}
# ]
student_data = generate_student_data(20, ['CT','python','stats','maths'],['delhi','chennai','mumbai','kolkata'])
# print(student_data)


'''a)'''
def min_course_marks(student_data, course):
    '''Return the min marks on a given course'''
    # return min([dictionary[key] for dictionary in student_data for key in dictionary if(key == course)])  # min return min marks in list of marks
    return min(student_data , key = lambda x : x[course])[course]  # min return dictionary from student_data with min marks in the course
    
    
print(min_course_marks(student_data , 'CT'))


'''b) '''
# IMPORTANT
def rollno_of_max_marks(student_data, course):
    '''Return the rollno of student with max marks in a course'''
    return max(student_data , key = lambda x: x[course])['rollno']
    

print(rollno_of_max_marks(student_data , 'stats'))



'''c ) IMPORTANT''' 
def sort_rollno_by_marks(student_data, course1, course2, course3):
    '''
    Return a sorted list of rollno sorted based on their marks on the three course marks. 
    course1 is compared first, then course2, then course3 to break ties.
    Hint: use tuples comparision
    '''
    # sort the dictionary of student_data list based on course1, course2, course3 marks
    sorted_student_data = sorted(student_data , key = lambda d : (d[course1],d[course2],d[course3]))
    return list(map(lambda x : x['rollno'] , sorted_student_data))

print(sort_rollno_by_marks(student_data , 'CT','maths','stats'))


'''d'''
def count_students_by_cities(student_data):
    '''Create a dictionary with city as key and number of students from each city as value.'''
    city_list = list(map(lambda x : x['city'], student_data))
    return {city : city_list.count(city) for city in city_list}
    

print(count_students_by_cities(student_data))



'''e'''
def city_with_max_no_of_students(student_data):
    '''Find the city with the maximum number of students.'''
    city_list = list(map(lambda x : x['city'], student_data))
    d = {city : city_list.count(city) for city in city_list}
    return max(d , key = d.get)    # imp : use of get
    

print(city_with_max_no_of_students(student_data))



'''f'''
def group_rollnos_by_cities(student_data):
    '''Create a dictionary with city as key and 
    a sorted list of rollno of students that belong to 
    that city as the value. '''
    empty_d = {d['city'] : [] for d in student_data}
    {empty_d[d['city']].append(d['rollno']) for d in student_data}
    return empty_d

print(group_rollnos_by_cities(student_data))



'''g'''
def city_with_max_avg_course_mark(student_data, course):
    '''
    Find the city with the maximum avg course marks.'''
    city_list = {d['city'] : [] for d in student_data}
    {city_list[d['city']].append(d['stats']) for d in student_data}
    output = {key : sum(value)/len(value) for key,value in city_list.items()}
    return max(output , key = output.get)  

print(city_with_max_avg_course_mark(student_data, 'stats'))

















