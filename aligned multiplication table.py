"""
multiplication tables (aligned)

simple multiplication tables with a neater look
providing user to control the breadth and length of the table


Author:Arunachalam.V
@arunachalamcodes
"""

def main():                                            #main function for better control
    max=int(input("tables, upto which number?: "))
    entry=int(input("maximum length of the table?: "))
    for i in range(1,int(entry)):
        for j in range(1,int(limits)):
            print(f'{j}x{i}={i*j:3d}|',end=" ")        #formatting
        print("")
main()
