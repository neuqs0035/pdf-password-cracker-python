import PyPDF2

def chars_4_place(pdf_loc):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    with open(pdf_loc, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

    if pdf_reader.is_encrypted:
        for i in chars:
            for j in chars:
                for k in chars:
                    for l in chars:
                        combination = i + j + k + l
                        print("Trying ...." + combination)
                        if pdf_reader.decrypt(combination):
                            print("Password Is : " + combination)
                            return
                        
    else:
        return "Pdf Has No Password"
    
def chars_6_place(pdf_loc):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    with open(pdf_loc, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

    if pdf_reader.is_encrypted:
        for i in chars:
            for j in chars:
                for k in chars:
                    for l in chars:
                        for m in chars:
                            for n in chars:
                                combination = i + j + k + l + m + n
                                print("Trying ...." + combination)
                                if pdf_reader.decrypt(combination):
                                    print("Password Is : " + combination)
                                    return
                        
    else:
        return "Pdf Has No Password"
    
def nums_4_place(pdf_loc):
    nums = '0123456789'

    with open(pdf_loc, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

    if pdf_reader.is_encrypted:
        for i in nums:
            for j in nums:
                for k in nums:
                    for l in nums:
                        combination = i + j + k + l
                        print("Trying ...." + combination)
                        if pdf_reader.decrypt(combination):
                            print("Password Is : " + combination)
                            return
                        
    else:
        return "Pdf Has No Password"

def nums_6_place(pdf_loc):
    nums = '0123456789'

    with open(pdf_loc, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

    if pdf_reader.is_encrypted:
        for i in nums:
            for j in nums:
                for k in nums:
                    for l in nums:
                        for m in nums:
                            for n in nums:
                                combination = i + j + k + l + m + n
                                print("Trying ...." + combination)
                                if pdf_reader.decrypt(combination):
                                    print("Password Is : " + combination)
                                    return
                        
    else:
        return "Pdf Has No Password"
print("PDF Password Cracker")

print("\n1) 4 place Characters")
print("2) 4 PLace Numbers")
print("3) 6 Place Numbers")
print("4) 6 PLace Characters")

choice = int(input("\nEnter Choice : "))

if(choice == 1):
    print("\nCharacters 4 PLace")

    pdf_location = input("\nEnter Your Pdf Location : ")

    chars_4_place(pdf_location)

elif(choice == 2):
    print("\nNumbers 4 PLace")

    pdf_location = input("\nEnter Your Pdf Location : ")

    nums_4_place(pdf_location)

elif(choice == 3):
    print("\nNumbers 6 PLace")

    pdf_location = input("\nEnter Your Pdf Location : ")

    nums_6_place(pdf_location)

elif(choice == 4):
    print("\nCharacters 6 PLace")

    pdf_location = input("\nEnter Your Pdf Location : ")

    chars_6_place(pdf_location)

else:
    print("\nEnter Valid Choice")