class checkbook:

    __user_id=0



    def __init__(self):
        self.__name='Default User'
        self.id=checkbook.__user_id
        checkbook.__user_id+=1
        self.__name="Default User"
        self.username=''
        self.password=''
        self.loggedin=False
        self.running=True
        # self.menu()

    @staticmethod
    def get_id():
        return checkbook.__user_id

    @staticmethod
    def set_id(val):
        checkbook.__user_id=val
        return checkbook.__user_id

    def get_name(self):
        return self.__name


    def set_name(self,value):
        self.__name=value





    def menu(self):
        user_input=input("""Welcome to checkbook ,how would you like to proceed?" \
        1.Press 1 to signup" \
        2.Press 2 to signin" \
        3.Press 3 to write a post" \
        4.Press 4 to message a friend" \
        5.Press anyother key to exit -->""")


        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            self.my_post()
        elif user_input=="4":
            self.sendmsg()
        else:
            print("Goodbye!")
            self.running = False

    def signup(self):
        email=input("Enter your email here->")
        pwd=input("Enter your password here->")
        self.username=email
        self.password=pwd
        print("You have signed up successfully!!")
        print("\n")
      


    def signin(self):
        if self.username=='' and self.password=='':
            print("Please signup first by pressing 1 in the main menu")
        else:
            uname=input("Enter your email/username here->")
            pwd=input("Enter your password here->")
            if self.username==uname and self.password==pwd:
                print("You have signed in successfully!!")
                self.loggedin=True
            else:
                print("Please input correct credentials...")

        print("\n")


    def my_post(self):
        if self.loggedin==True:
            txt=input("Enter you message here-->")
            print(f"following content has been posted-->{txt}")
        else:
            print("you need to signin first to post something...")
        print("\n")



    def sendmsg(self):
        if self.loggedin==True:
            txt=input("Enter your message here -->")
            frnd=input("whom to send the message?-->")

            print(f"your message send to {frnd}")
        else:
            print("you need to signin first to post something...")

            print("\n")






user15=checkbook()

