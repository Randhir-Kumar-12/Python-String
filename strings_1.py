
street=str(input("Enter street name:"))
city=str(input("Enter city name:"))
state=str(input("Enter state name:"))
address=street+' '+city+' '+state
print(address)
print(f"Street:{street} City:{city} State:{state}")
address=street+'\n'+city+'\n'+state
print(address)

#simple print() method
print("\nStreet:",city,"City:",state,"State:",state)
print("Street:",city,"\nCity:",state,"\nState:",state)
