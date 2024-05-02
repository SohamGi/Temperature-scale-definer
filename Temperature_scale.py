print("CREATE YOUR OWN TEMPERATURE SCALE.")
mp=float(input("Enter the melting point of ice in your scale: "))
bp=float(input("Enter the boiling point of water in your scale: "))
r=bp-mp
print("YOUR TEMPERATURE SCALE IS SUCCESFULY MADE. THANK YOU")
t=int(input("Do you want to convert from your scale to other scales or other scales to your scale? mark your answer with 0 or 1:    "))
if (t==0):
    x=float(input("Enter value of temperature in your scale:    "))
    scale=int(input("To what scale do you want to convert? Mark 1 for celsius, Mark 2 for Fahrenheit, Mark 3 for Kelvin:    "))
    if(scale==1):
        c=100*(x-mp)/r
        print("It is calculated that ",x,"degree is equal to ",c,"degree celsius")
    if(scale==2):
        f=((x-mp)*180/r)+32
        print("It is calculated that ",x,"degree is equal to ",f,"degree fahrenheit")
    if(scale==3):
        k=c+273
        print("It is calculated that ",x,"degree is equal to ",k,"degree Kelvin")
else:
    scale=int(input("From which scale do you want to convert to your scale? Mark 1 for Celsius Mark 2 for fahrenheit, Mark 3 for Kelvin:    "))
    if(scale==1):
        c=float(input("Enter temperature in celcius:    "))
        x=((r*c)/100)+mp
        print("The value of ",c,"degree celsius in your scale is ",x,"degrees")
    if(scale==2):
        f=float(input("Enter temperature in fahrenheit: "))
        x=(r(f-32)/180)+mp
        print("The value of ",f,"degree fahrenheit in your scale is ",x,"degrees")
    if(scale==3):
        k=float(input("Enter temperature in kelvin: "))
        x=((r*k)/100)+mp+273
        print("The value of ",k,"degree kelvin in your scale is ",x,"degrees")

    



