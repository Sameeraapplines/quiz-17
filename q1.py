#program for password
pwd =input("enter password\n")
for i in range(0,len(pwd)):
    if pwd[i]==['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
      break
    elif pwd[i]==[1,2,3,4,5,6,7,8,9,0]:
       break
    elif pwd[i]==['$','#','@']:
        break
    elif (len(pwd)>6 and len(pwd)<16):
     print("password is valid")
     break
else:
    print("password is not valid")

    
