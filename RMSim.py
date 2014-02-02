def RM(initialRegConf, instrucList):
    """
    Simulates a Register Machine input as:
        Registers: list with initial contents (natural numbers aka non-negative
        integers of each register where the index of the list is the register
        number

            e.g. [0,5,7] means R0 = 0, R1 = 5, R2 = 7 initially
            result of a computable partial function should contain
            the answer in R0 for example [12,0,0] should be the result
            of the computation of a RM that adds two numbers
            
        Program: list of instructions as strings that are the bodies of the
        instructions; the labels correspond to the index in the list.

            L_x: R_y+ --> L_z would be written as "Ry Lz" and would be in the
                xth position in the list
            L_w: R_x- --> L_y,L_z would be similarly written as "Rx Ly Lz" in
                the wth position in the list
            L_x: HALT would written as "HALT" in the xth position in the list

    Assumes the input is properly formatted because I'm too lazy

    To execute do
        res = RM([r0,...,rn],[l0,...ln]) and res will be a list containing
        the contents of the registers after executing the RM
    """
    # copy initialRegConf
    reg = initialRegConf

    instruc = instrucList[0]
    while True:
        instruc = instruc.split()
        if len(instruc) == 3:
            if reg[int(instruc[0].strip('R'))] > 0:
                reg[int(instruc[0].strip('R'))] -= 1
                instruc = instrucList[int(instruc[1].strip('L'))]
                continue
            else:
                instruc = instrucList[int(instruc[2].strip('L'))]
                continue
        elif len(instruc) == 2:
            reg[int(instruc[0].strip('R'))] +=1
            instruc = instrucList[int(instruc[1].strip('L'))]
            continue
        else:
            return reg
            
                
                

    
