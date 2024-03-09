# count = 0

# Name = input('Name: ')
# user = input('Registration number: ')
# print('''
# Are you ready to take this exam?
#   A.YES
#   B.NO
# ''')
# user = input('')
# if user.strip().capitalize() == 'A':
#  print('Read the questions carefully and select the correct option')      
# else:
#  exit()

 
# print('''
# 1.Zinc oxide is a?
#       A.Basic oxide 
#       B.Acidic oxide
#       C.Amphoteric oxide
#       D.Neutral oxide
#       E.Reactive oxide
# ''')
# user = input('Option: ')
# if user.strip().capitalize()== 'C':
#     # print('Correct')
#     count += 5
# # else:
# #     print('Incorrect')


# print('''
# 2.The periodic classification of elements is an arrangement of elements in order of their
#       A.Atomic weights
#       B.Isotopic weights
#       C.Molecular weights
#       D.Atomic numbers
#       E.Atomic masses
# ''')
# user = input('Option: ')
# if user.strip().capitalize()== 'D':
#     # print('Correct')
#     count += 5
# # else:
# #     print('Incorrect')


# print('''
# 3.A plant which grows on another plant without apparent harm to the host plant is called
#     A.a parasite
#     B.an epiphyte
#     C.a saprophyte
#     D.a predator
#     E.a hermaphrodite
# ''')
# user = input('Option: ')
# if user.strip().capitalize()== 'B':
#     # print('Correct')
#     count += 5
# # else:
# #     print('Incorrect')


# print('''
# 4.One of the function of xylem is
#      A.Strengthening the stem
#      B.manufacturing food
#      C.reducing loss of water
#      D.conducting manufactured food
#      E.storing unused sugar
# ''')
# user = input('Option: ')
# if user.strip().capitalize()== 'A':
#     # print('Correct')
#     count += 5
# # else:
# #     print('Incorrect')


# print('''
# 5.The inner diameter of a test tube can be measured accurately using a?
#         A.micrometer screw gauge
#         B.pair of dividers
#         C.metre rule
#         D.pair of vernier calipers
# ''')
# user = input('Option: ')
# if user.strip().capitalize()== 'D':
#     # print('Correct')
#     count += 5
# # else:
# #     print('Incorrect')


# print('''
# 6.When temperature of a liquid increases,its surface tension
#         A.Decreases
#         B.Increases
#         C.Remain constant
#         D.Increase then decreases

# ''')
# user = input('Option: ')
# if user.strip().capitalize()== 'A':
#     # print('Correct')
#     count += 5
# # else:
# #     print('Incorrect')


# print('''
# 7.A word processor can be used to
#       A.write text
#       B.edit text
#       C.print text
#       D. all of these
# ''')
# user = input('Option: ')
# if user.strip().capitalize()== 'D':
#     # print('Correct')
#     count += 5
# # else:
# #     print('Incorrect')


# print('''
# 8.Which of these application packages is mostly used by computer users?
#       A.Coreldraw
#       B.Ms access
#       C.Ms excel
#       D.Ms word

# ''')
# user = input('Option: ')
# if user.strip().capitalize()== 'D':
#     # print('Correct')
#     count += 5
# # else:
# #     print('Incorrect')
    

# print('''
# 9.A computer can not boot if it does not have .......?
#       A.Compiler
#       B.Loader
#       C.OS
#       D.Assembler

# ''')
# user = input('Option: ')
# if user.strip().capitalize()== 'C':
#     # print('Correct')
#     count += 5
# # else:
# #     print('Incorrect')


# print('''
# 10.Fire Fox is an example of ....
#       A.System software
#       B.Application package
#       C.Application software
#       D.Computer tools

# ''')  
# user = input('Option: ')
# if user.strip().capitalize()== 'C':
#      count += 5


# print( "Thanks for taking the test", Name,",your total score =", count)
   
# else:
#     print('Incorrect')  

# VERSION 2.O

# print(' SPARK INTERNATIONAL TEST FOR MIDDLE SCHOOLS.\n How many students wants to take this test?')
# user_number = int(input(''))
# Name_of_students = []
# for x in range (user_number):
#     Names = input('Name of student: ')
#     Name_of_students.append(Names)
# scores = []    
# # print(Name_of_students)
# for Name_of_student in Name_of_students:
#     print(f'{Name_of_student}, Are you ready to take this exam? \n A.YES\n B.NO')
#     user = input('')
#     if user.strip().capitalize() == 'A':
#       print('Read the questions carefully and select the correct option')      
#     else:
#       exit()

#     Questions = [
#     '1.Zinc oxide is a? \n A.Basic oxide  \n B.Acidic oxide \n C.Amphoteric oxide \n D.Neutral oxide \n E.Reactive oxide', 
#     '2.The periodic classification of elements is an arrangement of elements in order of their \n A.Atomic weights \n B.Isotopic weights \n C.Molecular weights \n D.Atomic numbers \n E.Atomic masses',
#     '3.A plant which grows on another plant without apparent harm to the host plant is called \n A.a parasite \n B.an epiphyte \n C.a saprophyte \n D.a predator \n E.a hermaphrodite',
#     '4.One of the function of xylem is \n A.Strengthening the stem \n B.manufacturing food \n C.reducing loss of water \n D.conducting manufactured food \n E.storing unused sugar',
#     '5.The inner diameter of a test tube can be measured accurately using a?\n A.micrometer screw gauge \n B.pair of dividers \n C.metre rule \n D.pair of vernier calipers',
#     '6.When temperature of a liquid increases,its surface tension\n A.Decreases \n B.Increases \n C.Remain constant \n D.Increase then decreases',
#     '7.A word processor can be used to \n A.write text \n B.edit text \n C.print text \n D. all of these ',  
#     '8.Which of these application packages is mostly used by computer users? \n A.Coreldraw \n B.Ms access \n C.Ms excel \n D.Ms word ',
#     '9.A computer can not boot if it does not have .......? \n A.Compiler \n B.Loader \n C.OS \n D.Assembler',
#     '10.Fire Fox is an example of .... \n A.System software \n B.Application package \n C.Application software \n D.Computer tools '                
#     ]
#     Answer = ['C','D','B','A','D','A','D','D','C','C']

#     score = 0
#     for ques, answer in zip(Questions,Answer):
#       print (ques)
#       user = input("Option: ")
#       if user.strip().capitalize() == answer :
#         score += 5
#     print ("Thanks for taking the test.", Name_of_student,",you scored",score,"out of 50.")
#     scores.append(score)  
# max_score = scores.index(max(scores))
# print( Name_of_students[max_score],'got the highest score.')
# # x =  (sum(scores))/user_number 
# # print("The mean score for this test is ", x) 
# mean_score = sum(scores)/len(scores)
# print(mean_score)    
                                          #  using dictionary
# score = 0
# Questions = {
#    '1.Zinc oxide is a? \n A.Basic oxide  \n B.Acidic oxide \n C.Amphoteric oxide \n D.Neutral oxide \n E.Reactive oxide': 'C',
#   ' 2.The periodic classification of elements is an arrangement of elements in order of their \n A.Atomic weights \n B.Isotopic weights \n C.Molecular weights \n D.Atomic numbers \n E.Atomic masses' : 'D'
# }
# for que,val in Questions.items():
#   print(que)
#   user = input("Option: ")
#   if user.strip().capitalize() == val :
#     score += 5
#     print('corect',score)
                                            # using function

# print(' SPARK INTERNATIONAL TEST FOR MIDDLE SCHOOLS.\n How many students wants to take this test?')
# user_number = int(input(''))
# Name_of_students = []
# for x in range (user_number):
#     Names = input('Name of student: ')
#     Name_of_students.append(Names)
# scores = []    
# # print(Name_of_students)
# for Name_of_student in Name_of_students:
#     print(f'{Name_of_student}, Are you ready to take this exam? \n A.YES\n B.NO')
#     user = input('')
#     if user.strip().capitalize() == 'A':
#       print('Read the questions carefully and select the correct option')      
    # else:
  #       exit()
    
  #   def Questions():
  #     global Quest
  #     Quest = {
  #  '1.Zinc oxide is a? \n A.Basic oxide  \n B.Acidic oxide \n C.Amphoteric oxide \n D.Neutral oxide \n E.Reactive oxide': 'C',
  # ' 2.The periodic classification of elements is an arrangement of elements in order of their \n A.Atomic weights \n B.Isotopic weights \n C.Molecular weights \n D.Atomic numbers \n E.Atomic masses' : 'D'
  #   }
  #   Questions()
  #   global score
  #   score = 0  
  #   for que,val in Quest.items():
  #       print(que)
  #       user = input("Option: ")
  #   if user.strip().capitalize() == val :
  #         score += 5
  #         print('correct',score)
     


        # USING CLASS
scores = []  
class exam:
  def _init_(self):
      self.score = 0
      print('SPARK INTERNATIONAL TEST FOR MIDDLE SCHOOLS.')
      print('How many students wants to take this test?')
      user_number = int(input('')) 
      Name_of_students = []
                            
# print(Name_of_students)
      for x in range(user_number):
          Names = input('Name of student: ')
          Name_of_students.append(Names)
      
      for Name_of_student in Name_of_students:
            print(f'{Name_of_student}, Are you ready to take this exam? \n A.YES\n B.NO')
            user = input('')
            if user.strip().capitalize() == 'A' or user.strip().upper() == 'YES':
              print('Read the questions carefully and select the correct option')
              Questions = {
               '1.Zinc oxide is a? \n A.Basic oxide  \n B.Acidic oxide \n C.Amphoteric oxide \n D.Neutral oxide \n E.Reactive oxide': 'C',
                ' 2.The periodic classification of elements is an arrangement of elements in order of their \n A.Atomic weights \n B.Isotopic weights \n C.Molecular weights \n D.Atomic numbers \n E.Atomic masses' : 'D'}
              for que, val in Questions.items():
                  print(que) 
                  user_ans = input("Option: ")
                  if user_ans.strip().capitalize() == val:
                    self.score += 5
              print('Score:', self.score)    
            else:
                exit()           
  
cbt=exam()
cbt._init_()



   
 
   