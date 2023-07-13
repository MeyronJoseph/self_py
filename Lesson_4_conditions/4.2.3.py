#


Degrees = input("Insert the temperature you would like to convert: ")
Degrees_float = float(Degrees[:-1])
if "c" in Degrees or "C" in Degrees:
    F_Degrees = (9 * Degrees_float + (32 * 5)) / 5
    print(str(F_Degrees) + "F")
elif "f" in Degrees or "F" in Degrees:
    C_Degrees = (5 * Degrees_float - 160) / 9
    print(str(C_Degrees) + "C")

# Course solution:
# source = input("Enter the temperature you would like to convert: ")
# if source[-1] == 'f' or source[-1] == 'F':
#     print((float(source[:-1]) * 5 - 160) / 9)
# if source[-1] == 'c' or source[-1] == 'C':
#     print((float(source[:-1]) * 9 + 160) / 5)
