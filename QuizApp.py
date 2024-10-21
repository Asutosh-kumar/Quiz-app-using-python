from tkinter import *
from tkinter import messagebox

name_list = ["asutosh","ashima","veer","rahul","ankit","aseema"]
pass_list = ["asu","kumar","@asu","@123","whatever","1234"]
def starting_page():
    window = Tk()
    window.title("Login Page")
    window.geometry('600x330')
    window.configure(bg="cyan")
    
    def sign_up():
        window.destroy()
        root = Tk()
        root.title("SignUp Page")
        root.geometry("600x330")
        
        def signIn():
            var1 = entry1.get()
            var2 = entry3.get()
            var3 = entry2.get()
            
            if var3.endswith("@gmail.com"):
                with open("email.log", mode='a') as email_log:
                    email_log.write(var3)
        
            else:
                messagebox.showerror("SignUp Failed","Invalid Email Address!")
                
            if var1=='' or var2=='':
                messagebox.showerror("Error", "Please fill in all fields")
            else:
                name_list.append(var1)
                pass_list.append(var2)
                root.destroy()
                starting_page()
        
        SignUp_page = Label(root,text="Sign Up For Quiz",font=("Areal",20))
        SignUp_page.place(x = 185,y=10)
        
        Username = Label(root,text="User Name:",font=("Areal",15))
        Username.place(x = 60,y=80)
        
        emailid = Label(root,text="Email ID:",font=("Areal",15))
        emailid.place(x = 60,y=140)

        creat_pass = Label(root,text="Password:",font=("Areal",15))
        creat_pass.place(x = 60,y=200)
        
        
        entry1 = Entry(root,font=("Areal",15), width=30)
        entry1.place(y=80,x=180)
    
        entry2 = Entry(root,font=("Areal",15), width=30)
        entry2.place(y=140,x=180)
    
        entry3 = Entry(root,font=("Areal",15), width=30)
        entry3.place(y=200,x=180)
        
        creat_acc = Button(root,text = "Create Account",font=("Areal",11),command=signIn,width=50, bg="blue", fg="white")
        creat_acc.place(y=270,x=60)

    def login():
        var1 = User_name.get()
        var2 = Password.get()
        if var1 == "" or var2 == "":
            messagebox.showerror("Login Failed","Empty User Name or Password")
            return
        
        new_name_list = name_list
        new_pass_list = pass_list

        user_found = False
        for i in range(len(new_name_list)):
            if new_name_list[i]== var1 and new_pass_list[i] == var2:
                
                user_found = True
                window.destroy()
                top = Tk()
                top.configure(bg= "cyan")
                top.title("Quiz")
                
                top.geometry('600x330')
                
                questions = [
                            {"question": "1. What is the capital of France?", "options": ["Room", "Berlin", "Paris", "Madrid"], "answer": 3},
                            {"question": "2. Which planet is known as the Red Planet?", "options": ["Venus", "Mars", "Jupiter", "Saturn"], "answer": 2},
                            {"question": "3. Who developed the theory of relativity?", "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Nikola Tesla"], "answer": 2},
                            {"question": "4. What is the largest ocean on Earth?", "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "answer": 4},
                            {"question": "5. What is the boiling point of water?", "options": ["100°C", "212°F", "Both A and B", "None of the above"], "answer": 3},
                            {"question": "6. Which element has the chemical symbol 'O'?", "options": ["Oxygen", "Osmium", "Oxalate", "Ozone"], "answer": 1},
                            {"question": "7. What is the smallest prime number?", "options": ["0", "1", "2", "3"], "answer": 3},
                            {"question": "8. What is the longest river in the world?", "options": ["Amazon", "Nile", "Yangtze", "Mississippi"], "answer": 2},
                            {"question": "9. Which gas do plants absorb from the atmosphere?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": 2},
                            {"question": "10. What is the freezing point of water?", "options": ["0°C", "32°F", "Both A and B", "None of the above"], "answer": 3},
                            {"question": "11. What is the largest planet in our solar system?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": 3},
                            {"question": "12. Who wrote 'Romeo and Juliet'?", "options": ["Mark Twain", "Charles Dickens", "William Shakespeare", "Jane Austen"], "answer": 3},
                            {"question": "13. What is the hardest natural substance on Earth?", "options": ["Gold", "Iron", "Diamond", "Quartz"], "answer": 3},
                            {"question": "14. What is the main ingredient in guacamole?", "options": ["Tomato", "Avocado", "Pepper", "Onion"], "answer": 2},
                            {"question": "15. What is the largest mammal in the world?", "options": ["Elephant", "Blue Whale", "Great White Shark", "Giraffe"], "answer": 2},
                            {"question": "16. Which country is known as the Land of the Rising Sun?", "options": ["China", "Japan", "Thailand", "South Korea"], "answer": 2},
                            {"question": "17. What is the currency of the United Kingdom?", "options": ["Dollar", "Euro", "Pound Sterling", "Yen"], "answer": 3},
                            {"question": "18. What is the chemical formula for water?", "options": ["H2O", "CO2", "O2", "H2SO4"], "answer": 1},
                            {"question": "19. Which element is represented by the symbol 'Na'?", "options": ["Nitrogen", "Neon", "Sodium", "Nickel"], "answer": 3},
                            {"question": "20. What is the capital of Australia?", "options": ["Sydney", "Canberra", "Melbourne", "Brisbane"], "answer": 2},]
                
                cur_question = 0
                
                def show_question():
                    if cur_question>0:
                        pre_btn.config(state=NORMAL)
                    
                    q = questions[cur_question]
                    label5.config(text=q["question"])
                    btn1.config(text="(a). " + q["options"][0])
                    btn2.config(text="(b). " + q["options"][1])
                    btn3.config(text="(c). " + q["options"][2])
                    btn4.config(text="(d). " + q["options"][3])
            
                user_answer = [-1] * len(questions)
                def next_question():
                    nonlocal cur_question
                    user_answer[cur_question] = var1.get()
                                    
                    cur_question += 1
                    if cur_question < len(questions):
                        show_question()
                    else:
                        calculate_score()
                            
                def pre_question():
                    nonlocal cur_question
                    
                    if cur_question>0:
                        cur_question -= 1
                        show_question()
                        
                def calculate_score():
                    score = 0
                    for i, q in enumerate(questions):
                        if user_answer[i] == q["answer"]:
                            score += 1           
                    
                    messagebox.showinfo("Quiz Finished", f"You scored {score}/{len(questions)}") 
                    
                    next_btn.config(state= DISABLED)
                    pre_btn.config(state=DISABLED)
                    finish_btn.config(state=NORMAL)
                    
                def direc_to_start():
                    top.destroy()
                    starting_page()
                        
                var1 = IntVar()
                
                btn1 = Radiobutton(top,value=1,font=("Areal Bold",10),
                    variable=var1, indicatoron=False, width=20, height=2,bg="#98ff98", fg="black")

                btn2 = Radiobutton(top,value=2,font=("Areal Bold",10),variable=var1, 
                    indicatoron=False, width=20, height=2,bg="#98ff98",fg="black")

                btn3 = Radiobutton(top,value=3,font=("Areal Bold",10),variable=var1, 
                    indicatoron=False, width=20, height=2,bg="#98ff98",fg="black")
                
                btn4 = Radiobutton(top,value=4,font=("Areal Bold",10),variable=var1, 
                    indicatoron=False, width=20, height=2,bg="#98ff98",fg="black")
                
                btn1.place(x=23,y=120)
                btn2.place(x= 253,y=120)
                btn3.place(x= 23,y=170)
                btn4.place(x=253,y=170)
                
                label4 = Label(top,text="Question:",font=("Areal",15),bg="cyan")
                label4.place(x=10,y=20)
                
                label5 = Label(top,font=("Areal",17),bg="cyan")
                label5.place(x=10,y=70)
                
                next_btn = Button(top,text="Next Question >>",font=("Areal",15),width=17, command=next_question,bg='red',fg="white")
                next_btn.place(x = 400,y=270)
                
                pre_btn = Button(top,text="<< Previous Question",font=("Areal",15),width=17,state=DISABLED,command=pre_question,bg='red',fg="white")
                pre_btn.place(x = 6,y=270)
                
                finish_btn = Button(top, text="Finish", font=("Areal", 15), state= DISABLED,width=17, command=top.destroy,bg='orange',fg="white")
                finish_btn.place(x=203, y=270)
                
                back_to_login = Button(top, text="<<  Back to login", font=("Areal", 13),width=15, command=direc_to_start,bg='Green',fg="white")
                back_to_login.place(x=420, y=20)
                
                show_question()
                
                break
        if not user_found:
            messagebox.showerror("Login Failed","Invalid User Name or Password")

    User_name = Entry(window,font=("Areal",15),width=15)
    User_name.place(x = 270,y=80)

    Password = Entry(window,font=("Areal",15), width=15,show="*")
    Password.place(x = 270,y=130)

    label1 = Label(window,text="Login Page",font=("Areal",30),bg="cyan")
    label1.place(x = 200,y=10)

    label2 = Label(window,text="User Name:",font=("Areal",15),bg="cyan")
    label2.place(x = 150,y=80)

    label3 = Label(window,text="Password :",font=("Areal",15),bg="cyan")
    label3.place(x = 150,y=130)
    
    label4 = Label(window,text="---------------------- Or ----------------------",font=("Areal",8),bg="cyan")
    label4.place(x=205,y=230)

    btn1 = Button(window,text="Log In",font=("Areal",11), command=login,width=20, bg="blue", fg="white")
    btn1.place(x=210,y=190)
    
    btn2 = Button(window,text="Sign Up",font=("Areal",11), command=sign_up,width=20, bg="blue", fg="white")
    btn2.place(x=210,y=265)
    
    window.mainloop()

starting_page()