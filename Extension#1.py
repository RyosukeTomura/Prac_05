NAME_LISTS = {"Jack": "12,4,1999",
              "Jill": "1,1,2000",
              "Harry": "27,3,1982"}

date_of_birth = input("Enter date of birth:")
date = date_of_birth.split()

for i in range(5):
        if date in NAME_LISTS:
                print(date_of_birth, "is", NAME_LISTS[date_of_birth])
        else:
                print("Invalid")
        date_of_birth = input("Enter data of birth")

