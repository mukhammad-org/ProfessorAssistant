import random 

name = input("Please enter your name: ")
print("Hello  " + name)
b = input("Do you want to create a question bank? Yes/No: ")
if b.lower() in["Yes","yes","YES","yeah","Yeah","YEAH","Of course","yup","Yup","Why not","Sure","sure"]:
    print("Great! Can you please provide me a path for your question bank and number of questions to be provided and a place to be saved?")
    while True:
     path = input("Enter the path for your question bank: ")
     if path == "question_bank.txt" :
       print("Thank you for providing a valid path.")
       break
    while True:
     num_questions = int(input("Enter the number of questions: "))

     if num_questions > 0 and num_questions < 100:
        print("Thank you for providing a valid number of questions.")
        break
    save_path = input("Enter the path where you want to save the question bank: ")
    print("Your question bank is uploading please wait a little bit... Thank you for your patience. Your question bank path is " + path + " and number of questions are " + str(num_questions) + " and it will be saved to " + save_path)

else:
    print("No worries,i am here to help you anytime!")
    exit()


    

