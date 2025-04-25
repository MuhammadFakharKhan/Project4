def main():

    print("=== Pythagorean Theorem Calculator ===")
    AB = float(input("Please enter the length of side AB:"))
    AC = float(input("Please enter the length of side AC:"))
    BC = (AB**2 + AC**2) ** 0.5
    print(f"The length of the hypotenuse BC is: {BC}")
    print("Pythagorean theorem calculation complete.")






if __name__ =='__main__':
    main()