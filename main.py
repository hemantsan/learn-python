print('Main File')
# from Question import Question
#
# question_prompt = [
#     "What colors are apples?\n(a) Red\n(b) Green\n(c) Pink\n",
#     "What color is sky?\n(a) Red\n(b) Blue\n(c) Yellow\n",
#     "What colors are bananas?\n(a) Green\n(b) Blue\n(c) Yellow\n",
# ]
#
# questions = [
#     Question(question_prompt[0], "a"),
#     Question(question_prompt[1], "b"),
#     Question(question_prompt[2], "c"),
# ]
#
# def run_test(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompt)
#         if answer == question.answer:
#             score += 1
#
#     print("You got: " + str(score) + " out of " + str(len(questions)) + " correct.")
#
# run_test(questions)

# from Student import Student
#
# st = Student("Hemant", "Coding", 4.5, False)
# print(st.name)
# print(st.on_honor_roll())

from IndianChef_Inheritance import IndianChef

chef = IndianChef()
chef.makeBananaSurprise()
chef.makesSamosa()

