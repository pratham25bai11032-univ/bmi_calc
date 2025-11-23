from datetime import datetime
File_Name = "bmi_history.txt"
def calculate_bmi():
    print("\n   BMI CALCULATOR   ")

    name = input ("Enter your name:  ")
    weight = float(input("Enter your weight (KG):  "))
    height_cm = float(input("Enter your Height  (cm)  "))


    height = height_cm / 100
    bmi = weight / (height **2)
    bmi = round(bmi , 2 )
    print(f"\n  {name} BMI is {bmi}")

    if bmi<18.5:
        category ="Underwight"
    elif 18.5<=bmi<=24.9:
        category = "normAL wEIGHT"
    elif 25<= bmi<=29.9:
        category= "Overweight"
    else:
        category = "Obese"
    print("Category:" , category)
    timestamp = datetime.now().strftime( "%Y-%m-%d %H:%M:%S"  )
    with open(File_Name,"a") as file:
        file.write(f"{name}|{bmi}|{category}|{timestamp}  \n")
    print ("\n Saved to bmi_history.txt")
    print("--                        --\n")

def view_history():
    print("\n    BMI HISTORY     ")
    try:
        with open(File_Name, "r" )as file:
            data = file.read()
            if data.strip() == "":
                print (" No history Found \n ")
            else:
                print(data)
    except FileNotFoundError:
        print(" No HistoryFound \n")
def main():
    while True:
        print("         BMI MENU             ")
        print("1. Calculate BMI")
        print("2> View Bmi History ")
        print("3. Exit ")
        choice = input(" Choose an Option ")
        if choice == "1":
            calculate_bmi()
        elif choice == "2":
            view_history()
        elif choice == " 3 ":
            print("Goodbye")
            break
        else:
            print("Invalid choice , TRy Again \n")

main()