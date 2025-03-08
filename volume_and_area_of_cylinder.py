#!/usr/bin/env python3
# Created By: Volodymyr Kryzhanovskyi
# Date: 07/03/2025
# This program calculates the surface area and volume of cylinder
import math

def main():
    #Welcomes the user.
    print("Hello, the user of this calculator. This calculator may be useful for you in order to find the surface area and volume of cylinder. ")
    #Asks user about their next action.
    welcome_message = str(input("If you want to continue calculating, type yes and if not then type no:"))
    #If statement and else statement defines a string variable and based on it, executes the specific part of the code. the brackets and .lower help the code to see each variable.
    if welcome_message.lower() == "no":
        print("\033[1m \033[91m \033[41m I will delete your operation system.")
    else:
        #Gets the radius and height from the user
            radius = float(input("Enter the radius value (cm): "))
            height = float(input("Ener the height value (cm): "))
            #Applies the formulas in order to find volume and surface area
             surface_area = 2 * math.pi * radius * height + 2 * math.pi * radius ** 2
             volume = math.pi * radius ** 2 * height
             #Displays the final outcome based on these two formulas in two significant digit format.
               print("The surface area of the cylinder is {:.2f} cm^2".format(surface_area))
                print("The volume of the cylinder is {:.2f} cm^3".format(volume))
                #Asks user if they want to convert the centimeter value into any other metric value given.
                question_metrics = str(input("To what metrics do you want to convert your values? (m/mm/km), if you do not wish to have your values converted, say no: "))
                #If user chooses m which is meters, then the code will convert it to meters by dividing by hundred
                 if question_metrics == "m":
            metrical_surface_area = surface_area / 100
            metrical_volume = volume / 100 
            #Displays the converted surface are and volume in meters
            print("The surface area of cylinder is {: .5f} meters squared".format(metrical_surface_area))
            print("The volume of cylinder is {: .5f} meters cubed".format(metrical_volume))
#If user chooses to convert to mm, the code multiplies the volume and surface area by 10
        elif question_metrics == "mm":
            milimetrical_surface_area = surface_area * 10
            milimetrical_volume = volume * 10
            #Displays the converted values in millimeters
            print("The surface area of cylinder is {: .5f} millimeters squared".format(milimetrical_surface_area))
            print("The volume of cylinder is  {: .5f} millimeters cubed".format(milimetrical_volume))
#If the user decides to convert the values into kilometers, the program will divide it by a hundred thousand
        elif question_metrics == "km":
            kilometrical_surface_area = surface_area / 100000  
            kilometrical_volume = volume / 100000  
            #Displays the values in kilometers form
            print("The surface area of cylinder is {} kilometers squared".format(kilometrical_surface_area))
            print("The volume of cylinder is {} kilometers cubed".format(kilometrical_volume))
            #Ignores the code sections mentioned higher and makes a warm message.
        elif question_metrics == "no":
            print("Alright, thank you very much for the use of calculator.")
if __name__ == "__main__":
    main()
