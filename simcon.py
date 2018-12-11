import os

"""
SIMCOND automater
you can get I-V curve by just executing this python file
but if you wanna change the range of applied valtage,
you have to change a list, gate_voltage or drain_voltage

python simcon.py or python3 simcon.py

Note: you need to change outputfile name in your Monte carlo simulation program!!
"""

gate_valtage = [0.1, 0.0, -0.1, -0.2, -0.3, -0.4, -0.5]

drain_valtage = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]

for gate in gate_valtage:
    for drain in drain_valtage:
        f = open("SIMCOND.txt", "w")
        script = """
        5.0000000E-16
        1.500000E-12
        0.0000000E+00
        0.1000000E-12
        5.000000    
        200.0000   
        0.0000000E+00 """  + str(gate) + "000000E+00" + "  "+  str(drain)+ "000000E+00"  """ 
        0.0000000E+00  0.0000000E+00  0.0000000E+00
        1.000000   
        1.000000    
        0.7000000       2.000000       5.000000       15.00000"""
        f.write(script)
        f.close()
        # command = "ifortran a.out" + str(gate)
        # os.system((command))