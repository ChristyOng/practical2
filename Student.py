class Student:
   def __init__(self, name):
       self.name = name
       self.math = 0
       self.chinese = 0
       self.english = 0
       self.science = 0
       self.choices = []

   def get_score(self):
       return (self.math + self.chinese + self.english + self.science) / 4

   def __str__(self):
       return '{} scores {}, the choices are {}, {}, {}'.format(self.name, self.get_score(), self.choices[0], self.choices[1], self.choices[2])

def main():
   students = load_result()

   for s in students:
       s.choices.append('School A')
       s.choices.append('School B')
       s.choices.append('School C')
   for s in students:
       print('{} scores {}, the choices are {}, {}, {}'.format(s.name,s.get_score(), s.choices[0], s.choices[1], s.choices[2]))

def load_result():
   students = []
   # implement the load result logic here
   result_file = open('results.txt','r')
   for result in result_file:
       list = result.split(',')
       s = Student(list[0])
       s.math = float(list[1])
       s.chinese = float(list[2])
       s. english = float(list[3])
       s.science = float(list[4])
       students.append(s)

   return students

main()

