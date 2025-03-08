#!/usr/bin/env python3
# Created By: Volodymyr Kryzhanovskyi
# Date: 07/03/2025
# This program calculates the surface area and volume of cylinder
import math

def main():
    print("Hello, the user of this calculator. This calculator may be useful for you in order to find the surface area and volume of cylinder. ")
    welcome_message = str(input("If you want to continue calculating, type yes and if not then type no:"))
    if welcome_message() == "no":
        print("I will delete your operation system.")
    else:
            radius = float(input("Enter the radius value (cm): "))
            height = float(input("Ener the height value (cm): "))
if __name__ == "__main__":
    main()
