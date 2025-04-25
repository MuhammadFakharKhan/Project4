def main():
    voting_age_of_Peturksbouipo:int = 16
    voting_age_of_Stanlau :int = 25
    voting_age_of_Mayengua :int = 48

    print("THis program shows the international vote limit age")
    user = int(input("What is your age?"))
    
    if user >= voting_age_of_Peturksbouipo:
        print(f"You can vote in Peturksbouipo where voting age is {voting_age_of_Peturksbouipo}")
    else:
        print(f"You cannot vote in Peturksbouipowhere voting age is {voting_age_of_Peturksbouipo}")

        if user >= voting_age_of_Stanlau:
            print(f"You can vote in Stanlau where voting age is {voting_age_of_Stanlau}")
        else:
            print(f"You cannot vote in Stanlau where voting age is {voting_age_of_Stanlau}")

            if user >= voting_age_of_Mayengua:
                print(f"You can vote in Mayengua where voting age is {voting_age_of_Mayengua}")
            else:
                print(f"You cannot vote in Mayengua where voting age is {voting_age_of_Mayengua}")







if __name__ =="__main__":
    main()