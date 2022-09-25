def string_case_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0, "neither_upper_nor_lower":0}
    for i in s:
        if i.isupper():
           d["UPPER_CASE"]+=1
        elif i.islower():
           d["LOWER_CASE"]+=1
        else:
           d["neither_upper_nor_lower"] += 1
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])
    print ("No. of non alpha characters  : ", d["neither_upper_nor_lower"])

string_case_test('Python Is Easy')