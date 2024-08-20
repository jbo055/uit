#write a program that reads the number of minutes, text messages, and 911 calls used in a month from the user, 
#and calculates the bill.

baseCharge = 15.00
additionalMinutesCharge = 0.25
additionalTextCharge = 0.15
additional911Charge = 0.44
tax = 0.05

totalMinutes =float(input('Minutes of air time used: '))
totalTextMessages = float(input('Number of text messages sent: '))
calls911 = float(input('Number of 911 calls made: '))

includedMinutes = 50
includedTextMessages = 50

additionalMinutes = totalMinutes - includedMinutes
additionalTextMessages = totalTextMessages - includedTextMessages

if additionalMinutes < 0:
    additionalMinutes = 0
additionalMinutesCost = additionalMinutes * additionalMinutesCharge
if additionalTextMessages < 0:
    additionalTextMessages = 0
additionalTextCost = additionalTextMessages * additionalTextCharge
if calls911 < 0:
    calls911 = 0
total911Charge = calls911 * additional911Charge

taxAmount = (baseCharge + additionalMinutesCost + additionalTextCost + total911Charge) * tax
totalBill = baseCharge + additionalMinutesCost + additionalTextCost + total911Charge + taxAmount

print(format('Base charge: $', baseCharge,))
print('Additional minutes charge: $', additionalMinutesCost)
print('Additional text message charge: $', additionalTextCost)  
print('911 charge: $', total911Charge)  
print('Tax: $', taxAmount)
print('Total bill: $', totalBill)






