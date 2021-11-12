##############import modules needed#############

from tkinter import*#imports all tkinter modules

import os

import csv

import sys

import re


###############################################

window = Tk()

window.title("Banking Program")
window.configure(bg='blue')#sets the bg color of main window
window.geometry("500x500")#sets the size of the main window


def fin_sign():

        global name
        
        name = TempName.get()
        
        email = TempEmail.get()
        password = TempPw.get()
        accounts = os.listdir()#looks at everything in current dir

###########checks to see if user entered anything
        if name == "" or email == "" or password == "":
                notifications.config(fg='red',text="There must be an entry in every field * ")
                return
        ####################password validation
        if len(password) < 8:
                notifications.config(fg='red',text="password needs to be at least 8 characters long")
                return
        elif re.search('[0-9]',password) is None:
                notifications.config(fg='red',text="Make sure your password has a number in it")
                return
        elif re.search('[A-Z]',password) is None:
                notifications.config(fg='red',text="Make sure your password has a capital letter in it")
                return
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

        if(re.search(regex, email))is None:
                notifications.config(fg='red',text="not a valid email address")
                return
        
################################################       
                
#############checks to see if account exists####
        for check_name in accounts:
               newfile = name + '.csv'#adds csv extension onto name
               if newfile == check_name:
                        notifications.config(fg='red',text="sorry somebody already has that username")#if account already exists print "already exist note to user"
                        return
               
               else:#everything is correct
                        with open(newfile,"w",newline="") as File:
                                balance = 0
                                writer = csv.writer(File)
                                writer.writerow([name])
                                writer.writerow([email])
                                writer.writerow([password])
                                writer.writerow([balance])
                        File.close()
                        notifications.config(fg='green',text="Congratulations Your account was created")


################################################

def Sign_Up():

        #temp variables
        global TempName
        global TempEmail
        global TempPw
        global notifications
        TempName = StringVar()
        TempEmail = StringVar()
        TempPw = StringVar()
        ###########
        global SignUpScreen
        SignUpScreen = Toplevel(window)#sets mini pop out window on top level
        SignUpScreen.geometry("500x450")
        SignUpScreen.title("Sign Up")
        Label(SignUpScreen, text = "Setting up an account is easy as pie!\n *password needs a minimum \n of 8 characters, a capitol letter, & a number", font =(20)).grid(row=0,sticky=N,pady=10)
        #info needed
        Label(SignUpScreen, text = "Name", font =(20)).grid(row=2,sticky=W,pady=10)
        Label(SignUpScreen, text = "Email", font =(20)).grid(row=3,sticky=W,pady=10)
        Label(SignUpScreen, text = "Password", font =(20)).grid(row=4,sticky=W,pady=10)


        ##########
        Entry(SignUpScreen,textvar=TempName).grid(row=2,column=0)
        Entry(SignUpScreen,textvar=TempEmail).grid(row=3,column=0)
        Entry(SignUpScreen,textvar=TempPw, show="*").grid(row=4,column=0)

        ####confirm button
        Button(SignUpScreen, text="confirm",command = fin_sign, font=(20)).grid(row = 7, sticky=N, pady=10)
        Button(SignUpScreen, text="Show Password",command = showsign, font=(18)).grid(row = 6, sticky=W, pady=10)
        Button(SignUpScreen, text="Hide Password",command = hidesign, font=(18)).grid(row = 6, sticky=E, pady=10)
        ###Notifications
##
        notifications = Label(SignUpScreen,font=(20))
        notifications.grid(row=8,sticky=N,pady=10)




#################################################### 
####code to hide and show passwords for login and sign up####
##############################################
def showsign():#shows the password
        Entry(SignUpScreen,textvar=TempPw, show="").grid(row=4,column=0)


def hidesign():#hides the password
        Entry(SignUpScreen,textvar=TempPw, show="*").grid(row=4,column=0)


def showsignlog():#shows the password
        Entry(LogInScreen,textvar=TempLogPw, show="").grid(row=2,column=1)


def hidesignlog():#hides the password
        Entry(LogInScreen,textvar=TempLogPw, show="*").grid(row=2,column=1)

        
        
def dashboard():#this function runs once user clicks logs in
        
        accounts = os.listdir()#looks at everything in current dir
        global LogName
        LogName = TempLogName.get()
        LogPw = TempLogPw.get()
        CheckLogName = LogName + '.csv'
        for check_name in accounts:
                if check_name == CheckLogName: 
                        file = open(check_name,"r")#functions works properly for name variable which opens a file without an extension
                        file_info = file.read()
                        file_info = file_info.split('\n')
                        CorrectPassword = file_info[2]
                        #Dashboard
                        if LogPw == CorrectPassword:
                                name = LogName
                                
                                LogInScreen.destroy()
                                dashboard = Toplevel(window)
                                dashboard.geometry("500x450")
                                dashboard.title("Dashboard")
                                #labels for dashboard
                                Label(dashboard,text="dashboard:",font=(20)).grid(row = 0, sticky=W, pady=5)
                                Label(dashboard,text="Welcome "+LogName,font=(20)).grid(row = 0, sticky=N, pady=5)
                                #buttons
                                Button(dashboard, text="account info",width=30, font=(20),command=account_info).grid(row = 2, sticky=N, pady=10)
                                Button(dashboard, text="Deposit",width=30,font=(20),command=deposit).grid(row = 5, sticky=N, padx=10,pady=10)
                                Button(dashboard, text="Withdraw",width=30,font=(20),command=withdraw).grid(row = 6, sticky=N, padx=10,pady=10)
                                Button(dashboard, text="See Balance",width=30,font=(20),command=balance).grid(row = 7, sticky=N, padx=10,pady=10)
                        
                                return

                        else:
                                LogNotifications.config(fg="red", text ="wrong password")
                                return

        LogNotifications.config(fg="red", text ="No account found")

        
############################################################

def account_info():
       #variables
        file = open(LogName + ".csv","r")
        data = file.read()
        info = data.split('\n')
        name_info = info[0]
        email_info = info[2]
        pw_info = info[1]
        

       #account info screen
        info = Toplevel(window)
        info.geometry("500x450")
        info.title("Account Info")
       #labels
        Label(info,bg='orange',text = "Account Info", font = (40)).grid(row=0,sticky=N,pady=10,padx=30)
        Label(info,bg='orange',text = "Name: " +name_info, font = (40)).grid(row=1,sticky=W,pady=10,padx=30)
        Label(info,bg='orange',text = "Password: " +email_info, font = (40)).grid(row=2,sticky=W,pady=10,padx=30)
        Label(info,bg='orange',text = "Email: " +pw_info, font = (40)).grid(row=3,sticky=W,pady=10,padx=30)
        
def deposit():#functions made to enter money into the account 
        #variables
        global dollars_to_enter
        global deposit_notifications
        global current_dollars_label
        dollars_to_enter = StringVar()
        file = open(LogName +".csv","r")
        data = file.read()
        details = data.split('\n')
        balance_details = details[3]
        #deposit screen
        deposit_display_screen = Toplevel(window)
        deposit_display_screen.geometry("500x450")
        deposit_display_screen.title("Deposit")
        #labels
        Label(deposit_display_screen, text="deposit ammount: ",font=(20)).grid(row=0,sticky=N,pady=10)
        
        current_dollars_label = Label(deposit_display_screen, text="You currently have:$ "+balance_details, font=(20))
        current_dollars_label.grid(row=0,sticky=N,pady=10)
        Label(deposit_display_screen, text="deposit: ",font=(20)).grid(row=2,sticky=W,pady=10)
        deposit_notifications = Label(deposit_display_screen,font=(20))
        deposit_notifications.grid(row=4,sticky=N,pady=5)
        #enter ammount
        Entry(deposit_display_screen, textvariable=dollars_to_enter).grid(row=2,column=1)
        #####Button
        Button(deposit_display_screen,text="Confirm",font=(20),command=fin_deposit).grid(row=3,sticky=W,pady=5)


def fin_deposit():

        if dollars_to_enter.get() == "":
                deposit_notifications.config(text = "Sorry...you must enter something into the bank",fg="red")
                return
        if float(dollars_to_enter.get()) <=0:
                deposit_notifications.config(text = "Sorry...you must enter a number greater than 0",fg="red")
                return
#####################################
        file = open(LogName + '.csv', 'r+')
        data = file.read()
        info = data.split('\n')
        old_balance = info[3]
        new_balance = old_balance
        new_balance = float(new_balance) + float(dollars_to_enter.get())
        new_balance = str(round(new_balance, 2))
        data        = data.replace(old_balance,str(new_balance))
        file.seek(0)
        file.truncate(0)
        file.write(data)
        file.close()
        current_dollars_label.config(text="current balance:$"+str(new_balance),fg="green")
        deposit_notifications.config(text = " deposit was a success",fg="green")
                
                

        
def withdraw():
         #variables
         global withdraw_dollars
         global withdraw_notifications
         global withdraw_dollars_label
         global dollars_to_enter
         global withdraw_display_screen
         withdraw_dollars = StringVar()
         file = open(LogName +".csv","r")
         data = file.read()
         details = data.split('\n')
         balance_details = details[3]
         #deposit screen
         withdraw_display_screen = Toplevel(window)
         withdraw_display_screen.geometry("500x450")
         withdraw_display_screen.title("Withdraw")
         #labels
         current_dollars_label = Label(withdraw_display_screen, text="deposit ammount: ",font=(20))
         current_dollars_label.grid(row=0,sticky=N,pady=10)
         Label(withdraw_display_screen, text="withdraw: ",font=(20)).grid(row=2,sticky=W,pady=10)
         withdraw_dollars_label = Label(withdraw_display_screen, text="You currently have:$ "+balance_details, font=(20))
         withdraw_dollars_label.grid(row=0,sticky=N,pady=5)
         
         withdraw_notifications = Label(withdraw_display_screen,font=(20))
         withdraw_notifications.grid(row=4,sticky=N,pady=5)
         #enter ammount
         Entry(withdraw_display_screen, text=withdraw_dollars).grid(row=2,column=1)
         #####Button
         Button(withdraw_display_screen,text="Confirm",font=(20),command=fin_withdraw).grid(row=3,sticky=W,pady=5)

         

def fin_withdraw():
         if withdraw_dollars.get() == "":
                 withdraw_notifications.config(text = "Sorry...you must enter something into the bank",fg="red")
                 return
         if float(withdraw_dollars.get()) <=0:
                 withdraw_notifications.config(text = "Sorry...you must enter a number greater than 0",fg="red")
                 return
#####################################
         file = open(LogName + '.csv', 'r+')
         data = file.read()
         info = data.split('\n')
         old_balance = info[3]
         new_balance = old_balance
         new_balance = float(new_balance) - float(withdraw_dollars.get())
         new_balance = str(round(new_balance, 2))
         if float(new_balance) <0:
                 withdraw_notifications.config(text = "Sorry...you can not withdraw more than you have",fg="red")
                 return
         data        = data.replace(old_balance,str(new_balance))
         file.seek(0)
         file.truncate(0)
         file.write(data)
         file.close()
         withdraw_dollars_label.config(text="You currently have:$ "+str(new_balance),fg="green")
         withdraw_notifications.config(text = "The withdraw was a success",fg="green")

def balance():
        #variables
         file = open(LogName +".csv","r")
         data = file.read()
         info = data.split('\n')
         global balance_info
         balance_info = info[3]
        #balance info screen
         balance = Toplevel(window)
         balance.geometry("500x450")
         balance.title("Ammount of money in the bank")
         Label(balance,bg='green',text = "Balance:$ " +balance_info, font = (40)).grid(row=3,sticky=W,pady=10,padx=30)
        
        

def log_in():#login into account
        #variables
        global TempLogName
        global TempLogPw
        global LogNotifications
        global LogInScreen
        TempLogName = StringVar()
        TempLogPw = StringVar()
        #login screen
        LogInScreen = Toplevel(window)#sets mini pop out window on top level
        LogInScreen.title("Log In")
        LogInScreen.geometry("500x450")
        #Labels
        Label(LogInScreen, text = "Welcome Back! Log into your account!", font =(20)).grid(row=0,sticky = N)
        Label(LogInScreen, text = "Username", font =(20)).grid(row=1,sticky =W)
        Label(LogInScreen, text = "Password", font =(20)).grid(row=2,sticky = W)
        LogNotifications = Label(LogInScreen,font=(20))
        LogNotifications.grid(row=4,sticky=N)
        ########Entry feilds
        Entry(LogInScreen,textvar=TempLogName).grid(row=1,column=1,padx=5)
        Entry(LogInScreen,textvar=TempLogPw, show="*").grid(row=2,column=1,padx=5)
        #####Button Login Confirm
        Button(LogInScreen, text = "Login", command = dashboard, width = 20, font=(20)).grid(row=7,sticky=W,pady=5,padx=5)
        Button(LogInScreen, text="Show Password",command = showsignlog, font=(18)).grid(row = 6, sticky=W, pady=10)
        Button(LogInScreen, text="Hide Password",command = hidesignlog, font=(18)).grid(row = 6, sticky=E, pady=10)

##############main function##########
        
        
#Labels
Label(window,bg='orange',text = "Welcome to the Banking Program", font = (40)).grid(row=0,sticky=N,pady=50,padx=30)

#Buttons

Button(window,bg='yellow',text = "Sign Up" ,font=(30), width=25,height =2 ,command = Sign_Up).grid(row = 4,sticky=N,pady=10,padx=120)

Button(window,bg='yellow',text = "Login" ,font=(30), width=25,height =2,command = log_in).grid(row = 5,sticky=N,pady=10,padx=120)

window.mainloop()

        

