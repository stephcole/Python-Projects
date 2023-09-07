#parent class
class Publishing_House:
    name = 'Grant Publishing House'
    username = 'GrantPH'
    website = 'Grantpublishinghouse.com'
    email = 'grant.publishing@gmail.com'
    address = 'Grant Way, Nowheresville, FL, 8675309'
    password = 'Worcestershire'

    def getLoginInfo(self):
        fname = input("Please enter your first name: ")
        lname = input("Please enter your last name: ")
        username = input("Insert user name: ")
        user_password = input("Insert user password: ")
        if (username == self.username and user_password == self.password) :
            print("Welcome back, {} {}!".format(fname, lname))
        else:
            print("The password or username is incorrect.")
    

#child class 1
class Author(Publishing_House):
    Name = 'Willow Woodberyy'
    Email = 'Willow_w@gmail.com'
    username = 'WillowW'
    private_pin = '7218'

    def getLoginInfo(self):
        fname = input("Please enter your first name: ")
        lname = input("Please enter your last name: ")
        username = input("Insert user name: ")
        user_pin = input("Enter pin: ")
        if (username == self.username and user_pin == self.private_pin) :
            print("Welcome back, {} {}!".format(fname, lname))
        else:
            print("The pin or username is incorrect.")       
    


#child class 2
class Genres(Publishing_House):
    History = 'The Facts that Caused the Legend of "The Bermuda Triangle"'
    Mystery = 'Who Framed Roger Rabbits Cousin?'
    Adult = '50 Shades of Crazy'
    Children = 'Babbitty Rabbitty and her Cackling Stump'
    Science = 'So You Wan to Live on Mars?'
    username = 'genrebaddy'
    access_code = 'sup'

    def getLoginInfo(self):
        fname = input("Please enter your first name: ")
        lname = input("Please enter your last name: ")
        username = input("Insert user name: ")
        access_code = input("Enter access code: ")
        if (username == self.username and access_code == self.access_code) :
            print("Access has been granted for {} {}!".format(fname, lname))
        else:
            print("The access code or username entered is incorrect.")       

publisher = Publishing_House()
publisher.getLoginInfo()

author = Author()
author.getLoginInfo()

security_clearance = Genres()
security_clearance.getLoginInfo()

    


    
