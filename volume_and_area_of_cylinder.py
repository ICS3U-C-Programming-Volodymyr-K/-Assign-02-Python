#!/usr/bin/env python3
# Created By: Volodymyr Kryzhanovskyi
# Date: 07/03/2025
# This program calculates the surface area and volume of cylinder
import math

def main():
    print("Hello, the user of this calculator. This calculator may be useful for you in order to find the surface area and volume of cylinder. ")
    welcome_message = str(input("If you want to continue calculating, type yes and if not then type no:"))
    if welcome_message() == "no":
        print("\033[1m \033[91m \033[41m I will delete your operation system.")
    else:
            radius = float(input("Enter the radius value (cm): "))
            height = float(input("Ener the height value (cm): "))
             surface_area = 2 * math.pi * radius * height + 2 * math.pi * radius ** 2
             volume = math.pi * radius ** 2 * height
               print("The surface area of the cylinder is {:.2f} cm^2".format(surface_area))
                print("The volume of the cylinder is {:.2f} cm^3".format(volume))
                question_metrics = str(input("To what metrics do you want to convert your values? (m/mm/km), if you do not wish to have your values converted, say no: "))
                 if question_metrics == "m":
            metrical_surface_area = surface_area / 100  # cm² to m² (1m² = 10000cm²)
            metrical_volume = volume / 100 # cm³ to m³ (1m³ = 1000000cm³)
            print("The surface area of cylinder is {: .5f} meters squared".format(metrical_surface_area))
            print("The volume of cylinder is {: .5f} meters cubed".format(metrical_volume))

        elif question_metrics == "mm":
            milimetrical_surface_area = surface_area * 10  # cm² to mm² (1cm² = 100mm²)
            milimetrical_volume = volume * 10  # cm³ to mm³ (1cm³ = 1000mm³)
            print("The surface area of cylinder is {: .5f} millimeters squared".format(milimetrical_surface_area))
            print("The volume of cylinder is  {: .5f} millimeters cubed".format(milimetrical_volume))

        elif question_metrics == "km":
            kilometrical_surface_area = surface_area / 100000  
            kilometrical_volume = volume / 100000  
            print("The surface area of cylinder is {} kilometers squared".format(kilometrical_surface_area))
            print("The volume of cylinder is {} kilometers cubed".format(kilometrical_volume))
        elif question_metrics == "no":
            print("Alright, thank you very much for the use of calculator.")
if __name__ == "__main__":
    main()
