# -*- coding: utf-8 -*-
"""
binary_count_up()
@author: methylDragon (github.com/methylDragon)

                           .     .
                        .  |\-^-/|  .    
                       /| } O.=.O { |\  
                      /´ \ \_ ~ _/ / `\
                    /´ |  \-/ ~ \-/  | `\
                    |   |  /\\ //\  |   | 
                     \|\|\/-""-""-\/|/|/
                             ______/ /
                             '------
                _   _        _  ___                         
      _ __  ___| |_| |_ _  _| ||   \ _ _ __ _ __ _ ___ _ _  
     | '  \/ -_)  _| ' \ || | || |) | '_/ _` / _` / _ \ ' \ 
     |_|_|_\___|\__|_||_\_, |_||___/|_| \__,_\__, \___/_||_|
                        |__/                 |___/          


Description: This script can be used as either a module, or standalone!

If used standalone, it can take user input (or you can configure it manually) 
to print all binary numbers leading up to a target binary number.

If used as a module, it can do the same, but it returns a list instead, just 
pass the number you want to count up to with binary_count_up()
"""

# =============================================================================
# EDITABLE PARAMETERS
# =============================================================================

target = 0
    
# =============================================================================
# FUNCTIONING CODE
# =============================================================================

# Binary addition function
def bin_add(*args): return bin(sum(int(str(x), 2) for x in args))[2:]

# Core function
def binary_count_up(target):
    current = 0 # Initialise initial value
    target = str(target) # Convert int to string

    # Check if run as standalone
    if __name__ == "__main__":
        count = 0

        # Ensure valid input
        while not all((i == "0" or i == "1") for i in str(target)) or target == None:
            print("ERROR: binary_count_up() received non-binary target!")
            target = input("Enter VALID target number, in binary: ") or None

        # Print binary numbers up to target
        print("\nOk! Fetching binary numbers:")

        # Print 0 to begin with
        print("{:0{slots}d}".format(0, slots = len(target)))
        count += 1
        
        while str(current).zfill(len(target)) < target:
            current = bin_add(current,1)
            print("{:0{slots}d}".format(int(current, 10), slots = len(target)))
            count += 1
            
        # Report summary
        print("\nTotal numbers printed: " + str(count))
    
    # Run as module otherwise
    else:
        # Ensure valid input
        if all((i == "0" or i == "1") for i in target):
    
            # Initialise binary list (starting with 0)
            number_list = ["{:0{slots}d".format(0, slots = len(target))]

            # Increment iterator until it reaches target

            # Append with zeroes to ensure it's the same as the target string
            while str(current).zfill(len(target)) < target:
                # Increment iterator
                current = bin_add(current, 1)
                current_str = ("{:0{slots}d}".format(int(current, 10), slots = len(target)))
                # Append iterator
                number_list.append(current_str)

        # If input is not valid
        else:
            # Print error and end function otherwise
            print("ERROR: binary_count_up() received non-binary target!")
            return

        # Return list of binary numbers leading up to and including target
        return #number_list

# =============================================================================
#  CHECK IF RUN STAND-ALONE
# =============================================================================
        
if __name__ == "__main__" and target == 0:
    print("This script takes user input to output all binary numbers leading up to a particular one.\n")

    # Call for user input
    target = input("Enter target number, in binary: ") or None
    # Run core function
    binary_count_up(target)

    # Prompt for exit
    exit = input('''\nPress [enter] twice to exit \n                            .     .
                         .  |\-^-/|  .    
                        /| } O.=.O { |\ ''') or None

    exit = input("Bye!") or None
