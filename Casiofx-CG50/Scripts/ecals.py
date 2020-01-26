def voltDiv(vt,rt,rn):
    return vt * (rn / rt)

def curDiv(it,rt,rn):
    return it * (rt / rn)

def cTotalE(q1,q2):
    if q1[0] == "i":
        if q2[0] == "r":
            return ("Voltage", q1[1]*q2[1])
        elif q2[0] == "p":
            return ("Voltage", q2[1]/q1[1])
    elif q2[0] == "i":
        if q1[0] == "r":
            return ("Voltage", q1[1]*q2[1])
        elif q1[0] == "p":
            return ("Voltage", q1[1]/q2[1])

    elif q1[0] == "r":
        if q2[0] == "p":
            return ("Voltage", sqrt(q1[1]*q2[1]))
    elif q2[0] == "r":
        if q1[0] == "p":
            return ("Voltage", sqrt(q1[1]*q2[1]))
    # e = i * r
    # e = p / i
    # e = sqrt(p * r)

def cTotalR(q1,q2):
    if q1[0] == "i":
        if q2[0] == "e":
            return ("Resistence", q2[1]/q1[1])
        elif q2[0] == "p":
            return ("Resistence", q2[1]/(q1[1]**2))
    elif q2[0] == "i":
        if q1[0] == "e":
            return ("Resistence", q1[1]/q2[1])
        elif q1[0] == "p":
            return ("Resistence", q1[1]/(q2[1]**2))

    elif q1[0] == "e":
        if q2[0] == "p":
            return ("Resistence",(q1[1]**2)/q2[1]))
    elif q2[0] == "e":
        if q1[0] == "p":
            return ("Resistence",(q2[1]**2)/q1[1]))
    # r = e / i
    # r = p / (i * i)
    # r = (e * e) / p

def cTotalI(q1,q2):
    if q1[0] == "r":
        if q2[0] == "e":
            return ("Current", q2[1]/q1[1])
        elif q2[0] == "p":
            return ("Current", sqrt(q2[1]/q1[1]))
    elif q2[0] == "r":
        if q1[0] == "e":
            return ("Current", q1[1]/q2[1])
        elif q1[0] == "p":
            return ("Current", sqrt(q1[1]/q2[1]))

    elif q1[0] == "e":
        if q2[0] == "p":
            return ("Current", q2[1]/q1[1])
    elif q2[0] == "e":
        if q1[0] == "p":
            return ("Current",q1[1]/q2[1])
    # i = e / r
    # i = p / e
    # i = sqrt(p / r)

def cTotalP(q1,q2):
    if q1[0] == "e":
        if q2[0] == "r":
            return ("Power", (q1[1]**2)/q2[1])
        elif q2[0] == "i":
            return ("Power", q1[1] * q2[1])
    elif q2[0] == "e":
        if q1[0] == "r":
            return ("Power", (q2[1]**2)/q1[1])
        elif q1[0] == "i":
            return ("Power", q2[1]*q1[1])

    elif q1[0] == "r":
        if q2[0] == "i":
            return ("Power", q1[1]*(q2[1]**2))
    elif q2[0] == "r":
        if q1[0] == "i":
            return ("Power",q2[1]*(q1[1]**2))
#     p = e * i
#     p = (e * e) / r
#     p = r * (i * i)


# def inductance():
# def varsL():
# def reactL():

# def capacitance():
# def varsC():
# def reactC():

# def totalZ():
# def angleT():
# def va():

# def getVars():
#     print("Enter known values of component followed by a return(i.e. v=120). Enter q to stop. ")
#     while val != "q";
#         val = str(input(">"))
#
# def getValues(**eValue):
#     return eValue

# def inputValid():

# def seriesResistors():
# def parallelResistors():

# def seriesInductors():
# def parallelInductors():

# def seriesCapacitors():
# def parallelCapacitors():
