name = "elene"
#name არის ცვლადი
# = არის ცვლადისთვის მნიშვნელობის მიმნიჭებელი სიმბოლო
# "elene" არის ცვლადისთვის მნიშვნელობა

surname = "lashauri"

# print(name)
#პრინტ ფუნქციას გადაეცემა ეკრანზე გამოსატანი ცვლადი ან სტრინგი ობიექტი

name = "elene"  #ეს არის str (string) ტიპის ცვლადი
age = 10 # ეს არის int ( integer ) მთელი რიცხვი
height = 120.5 #ეს არის float ტიპის ცვლადი( ათწილადი )
#boolean (bool) ტიპის ცვლადი

knows_programming = True  #True ან Folse
is_ugly = False  #snakecase (უბრალოდ წერის სტილი სტანდარტულად )

isUgly = False   # ჯავასკრიპტული camelcase


print(name + " " + surname)

#სტრინგი არის ბრჭყალებში მოქცეული სიმბოლო
# print(name + age)

print(type(age))
print(type(name))
print(type(surname))
print(type(height))
print(type(knows_programming))

print(name + " " + str(age))

print("I am" + " " + name + " " + surname + " " + str(age) + " " + "years old" + " " + "my height is" + " " + str(height))