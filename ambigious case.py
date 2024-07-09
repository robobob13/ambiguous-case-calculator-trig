import math
print("You are given side a and b, with angle A and are trying to find angle B. This calculator will tell you how many possible triangles and the value of the angle of B for each.")
while True:
    valerror = False
    ## Error testing incase input value is not a number
    try:
        sid_a = float(input("Enter the value of side a: "))
        sid_b = float(input("Enter the value of side b: "))
        ang_A = float(input("Enter the value of angle A: "))
    except ValueError:
        valerror = True
    
 
    ## Response to input value not being number
    if valerror == True:
        print("You need to input a number!")

    else:
        print("\n")
        h = round((round(math.sin(math.radians(ang_A)),3) * sid_b),3)

        ## Acute Angle
        if ang_A<90:
            if sid_a==h:
                print("1 Triangle Possible.")
                print("Angle B is 90 Degrees.")
                
            elif sid_a>=sid_b:
                print("1 Triangle Possible")
                angB = round(math.degrees(math.asin(round((h/sid_a),3))),2)
                print("Angle B is: "+str(angB))
            elif sid_a<h and sid_a<sid_b:
                print("No Triangles Possible")
            elif sid_a>h and sid_a<sid_b:
                print("2 Triangles Possible")
                ans1 = round(math.degrees(math.asin(round(h/sid_a,100))),3)
                print("Angle for First Triangle is: "+str(ans1))
                ans2 = 180-ans1
                print("Angle for Second Triangle is: "+str(ans2))
            print("h = "+str(h)+"\n")

        ## Obtuse Angle
        elif ang_A>90 and ang_A<180:
            if sid_b>=sid_a:
                print("No Triangles Possible")
            elif sid_a>sid_b:
                print("1 Triangle Possible")
                temp_value = sid_b * (math.sin(math.radians(ang_A))/sid_a)
                asin_value = math.asin(temp_value)
                angB = round(math.degrees(asin_value), 2)
                print("Angle B is: "+str(angB))
            print("h = "+str(h)+"\n")

        ## Right Angle
        elif ang_A==90 and sid_a>sid_b:
            print("Right Angled Triangle")
            angB = round(math.degrees(math.asin(round((sid_b/sid_a),3))),2)
            print("Angle B is: "+str(angB))
            print("h = "+str(h)+"\n")

        ## Right Angle but hypotenuse is < or = to side. 
        elif ang_A==90 and not sid_a>sid_b:
            print("No Possible Triangles with Right Angle, Hypotenuse is < or = the sides.\n")

        ## Angle Exeeding 180 degree error
        elif ang_A>180:
            print("Triangle cannot have angle exceeding 180 Degrees\n")

        ## Invalid values given
        else:
            print("No Triangles Possible (Invalid Triangle)\n")
        





        
        
