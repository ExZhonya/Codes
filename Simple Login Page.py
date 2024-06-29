#V3(Advanced Version)
def login():
    while True:
        name = input("Please Input Your Name: ")
        
        if name == "lua":
            while True:
                password = input("Please Input Your Password: ")
                
                if password == "12345":
                    print("Welcome home, lua")
                    return "Login Successful"
                else:
                    print("Access Denied. Please Retry")
        else:
            print("Access Denied. Please Retry")
if __name__ == "__main__":
    login_status = login()
    if login_status:
        print(login_status)
