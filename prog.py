msg = "the value entered is invalid"
def rgb_hex():
    red = int(input("enter red value:"))
    if red<0 or red>255:
        print(msg)
    blue = int(input("enter red value:"))
    if blue<0 or blue>255:
        print(msg)
    green = int(input("Please enter a value for green. "))
    if green < 0 or green > 255: 
        print(msg)
    
    #convert input to hex values
    val = (red << 16) +(green <<8)+blue
    print("%s" % (hex(val)[2:]).upper())
    
def hex_rgb():
    hex_val = input("enter hexadecimal value:")
    if len(hex_val) != 5:
        print(msg)
    else:
        hex_val=int(hex_val,16)
    
    twohexdigit = 2**8
    blue = hex_val % twohexdigit
    hex_val = hex_val >> 8
    green = hex_val % twohexdigit
    hex_val = hex_val >> 8
    red = hex_val % twohexdigit
    print("%s%s%s" %(red,green,blue))
    print("red: %s green: %s blue: %s" %(red,green,blue))
    
def control_fn():
    while True:
        option = input("enter 1 to convert RGB to HEX,2 to convert HEX to RGB, x to exit")
        if option == "1":
            rgb_hex()
        elif option == "2":
            hex_rgb()
        elif option == "x" or option == "X":
            break
        else:
            print("error")
            
control_fn()
# new change