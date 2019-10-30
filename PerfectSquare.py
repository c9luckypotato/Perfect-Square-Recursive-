# Jordan An
# 10/18/2019
# Magic square program

# I think i figure it out. You told me to do recursive backtracking, and that
# really helps: https://brilliant.org/wiki/recursive-backtracking/
# I try it out on the [2,7,6],[9,5,1],[4,3,8] square and it works for 5 unknown
# when I try 6 it took really long


# Make the dimension global
n = int(input("Enter a positive integer for the dimension of the square: "))

# Please enter a positive integer 
while n <= 0:
    n = int(input("Enter the dimension of the square (POSITIVE INT): "))

# I read this on Wiki. To be a magic square the sum must equal this.
magic_const = n * (n**2 + 1) / 2

# Put the main program into a funcion so that I don't have to put the other
# function first

def main():    
    # Create an empty list
    l_dis = []

    # I was thinking the creating 1 list to display (string) and one list of
    # integers to calculate
    l_calc = []

    var_count = 0
    # Create another list to make sure the user doesn't repeat the number and
    # dob't enter 0
    do_better_user = [0]
    
    # Use a loop to make the list. Declare j = 0 to get the the first value of
    # each row
    for i in range(n):
        j = 0
        val = input("Enter a number for index[%i][%i]: " % (i, j))
        # Add the input, we need this to add the list into the list first
        if val == "*":
            l_dis.append([val])
            
            l_calc.append([0])
            var_count += 1

        else:
            # Don't enter the same number twice user! Do better
            while int(val) in do_better_user:
                val = input("Error! Enter a value for index[%i][%i]: " % (i, j))

            # Add the valid value into the list    
            do_better_user.append(int(val))
            
            # Add the list of the value in there
            l_dis.append([val])
            l_calc.append([int(val)])

        for j in range(1, n):
            val = input("Enter a number for index[%i][%i]: " % (i, j))
            
            if val == "*":
                # Add the '*' into the list
                l_dis[i].append(val)

                # Add 0 to the calculation square if the user enter '*'
                l_calc[i].append(0)
                var_count += 1

            else:
                # Don't enter the same number twice user! Do better
                while int(val) in do_better_user:
                    val = input("Error! Enter a value for index[%i][%i]: "
                                % (i, j))
                    
                # Add the valid value into the list     
                do_better_user.append(int(val))
                
                # Add the value into the list
                l_dis[i].append(val)
                l_calc[i].append(int(val))
    
    # Use a loop to print the list out prettily
    print("The intial list is: ", l_calc)
    for row in l_dis:
        for col in row:
            print("%4s" % col, end = ' ')
        print()

    # Print the calculation list out just to check
    #print("The square before solving is: ")
    #print(l_calc)

    # If there is no variable
    if var_count == 0:
        # Check to see if it's a magic square
        if mag_sqr(l_calc):
            print("MAGIC SQUARE")
        else:
            print("Not a Magic Square.")
    # If the function return false then there is no solution
    elif not solve(l_calc, var_count):
        print("No solution")
    # Else print the square
    else:
        #print(var_count)
        solve(l_calc, var_count)
        print("The solution is: ")
        # I don't even want to print it pretty anymore
        for i in l_calc:
            print(i)

            
# Create a function so we can call it when we need to check
def mag_sqr(lst):
    sumz1 = 0
    sumz2 = 0
    z = n -1
    
    # Get the sum of the row and collumn
    for i in range(n):            
        sumsx = 0
        sumsy = 0

        # Get the sum of the 2 diagonals
        sumz2 += lst[i][z]
        sumz1 += lst[i][i]

        # Decrease z by 1 every loop
        z-=1
        
        for j in range(n):
            sumsy += lst[j][i]
            sumsx += lst[i][j]
       # Return false if the sum doesn't equal the magic constant
        if sumsy != magic_const or sumsx != magic_const:
            return False

    # Return false if the sum doesn't equal the magic constant
    if sumz1 != magic_const or sumz2 != magic_const:
        return False

    # Return true if all the sum equal the magic constant
    return True

# Recursive Backtracking
def solve(sq, var):
    # After there is no variable left, check if the square if a magic square
    if var == 0:
        return mag_sqr(sq)

    # Go through all the cell
    for i in range(n):
        for j in range(n):
            # set cell as the value we want to examine
            cell = sq[i][j]

            # Skip the cell that is not 0 (not '*') (that already has value). 
            if cell != 0:
                continue

            # else: plug value to run it 
            for test in range(1, int(magic_const)):
                # Plug the value
                sq[i][j] = test
                
                # Uncomment to see the progress
                '''print("[%i][%i]" % (row, col))
                print ("test is: ", test)
                for i in sq:
                    print( i)'''
                # Return true only when the whole thing is filled in (the 1st
                # condition) and the thing that is fill in is a magic square.
                if solve(sq, var -1) and mag_sqr(sq):
                    return True

                # Reset the square to its original and try again
                sq[i][j] = 0
    # Return False if there is no solution
    return False

# Run the main program
main()


