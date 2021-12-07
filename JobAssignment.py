# -*- coding: utf-8 -*-
"""
@author: Tas
"""
import json
global userInput
###############################################################################################

def userDefinedOperators(userChoice):
    operatorContainer= []
    operatorsCounter = 1
    while  operatorsCounter <= numberOfOperators:
        valueContainer = {}
        operatorName = input("Enter name of the operator " + str(operatorsCounter) + " : ")
    
        entriesCounter = int(input("How many entries for "+ operatorName + " : "))
        for i in range(entriesCounter):
            prefixCounter = input("Enter prefix: ")
           
            valueCounter = input("Enter value($/min): ")
            
            valueContainer[prefixCounter] = valueCounter
        
        operatorContainer.append((operatorName,valueContainer)) 
        del valueContainer  
        
        operatorsCounter +=1
    return operatorContainer

##############################################################################################

def ValueChecker(operatorList,userInput):
    
    digits =[]
    resultForOperators= []
    for operator in operatorList:
        maxPrefix = 0
        corPrefix = 0
        for prefix in list(operator[1].keys()):
            
            prefix = str(prefix)
            
            compare = userInput.startswith((prefix,"+"+prefix,"00"+prefix))
            
            if compare == True:
                validPrefix = True
                digits.append(prefix)
                i = -1
            
            else:
                validPrefix = False
              
            if validPrefix == True and len(digits[i]) > (maxPrefix):
                maxPrefix = len(digits[i])
                corPrefix = prefix

        if corPrefix != 0:
            value = operator[1][corPrefix]
            operatorName = operator[0]
            resultForOperators.append((value, operatorName, corPrefix))
    return resultForOperators

##############################################################################################

def lowestValue(resultList):
    
    if len(resultList) == 1:
        for prefix in resultList:
            print(f'Cheapest Price From Operator {prefix[1]}: $ {prefix[0]} /Min ')
            print(f'Prefix: {prefix[2]}')
            print(f'Entered Number: {userInput}')
        
    elif len(resultList) > 1:
        for prefix in resultList:
            print(f'Cheapest Price From Operator {prefix[1]}: $ {prefix[0]} /Min ')
            print(f'Prefix: {prefix[2]}')
             
        print(f'Entered Number: {userInput}')   
    else:
        print("Wronge Entry")

##############################################################################################

# Mian Func

existedOperators=[('A', {"1": 0.9,"268": 5.1,"46": 0.17, "4620": 0.0,"468": 0.15,"4631": 0.15,"4673": 0.9, "46732": 1.1}), ('B', {"1": 0.92,"44" : 0.5,"46" : 0.2,"467": 1.0,"48" : 1.2})]


with open("existingOperators.json", "w") as outfile:
    json.dump(existedOperators, outfile)

with open(r"C:\Users\Dator\OneDrive\Desktop\DataCamp\JobAssignment/existingOperators.json", "r") as read_file:
    data = json.load(read_file)

print("\t\t<<<Options>>>\nPress 1 to check in existing operators\nPress 2 to enter new operators")
userChoice = int(input('Enter Choice: '))


if userChoice == 1:
    
    userInput = input("Enter A Number: ")
    lowestValuesContainer = ValueChecker(data,userInput)
    finalValues= lowestValue(lowestValuesContainer)
    print(finalValues)
elif userChoice == 2:
    numberOfOperators = int(input("Number of operators you want to register: "))
    #global userInput
    

    listContainer= userDefinedOperators(numberOfOperators)
    userInput = input("Enter A Number: ")
    lowestValuesContainer = ValueChecker(listContainer,userInput)
    finalValues= lowestValue(lowestValuesContainer)
    print(finalValues)
else:
    print("Wrong Choice")
