#cost of ground shipping (cost per pound)
def ground_shipping(weight):
  flat_charge = 20.00
  if weight <= 2:
    cost = weight * 1.50
  elif weight <= 6:
    cost = weight * 3.00
  elif weight <= 10:
    cost = weight * 4.00
  else:
    cost = weight * 4.75
  return cost + flat_charge

#cost of premium ground shipping (flat rate)

premium_ground_shipping = 125.00

#cost of drone shipping (cost per pound)
def drone_shipping(weight):
  if weight <= 2:
    cost = weight * 4.50
  elif weight <=6:
    cost = weight * 9.00
  elif weight <=10:
    cost = weight * 12.00
  else:
    cost = weight * 14.25
  return cost 

#Finds the cheapest shipping method and prints cost. 
def cheapest_shipping(weight):
  if ground_shipping(weight) < drone_shipping(weight):
    return "Ground shipping is the cheapest method of shipping. It will cost: £" + str(ground_shipping(weight))
  elif drone_shipping(weight) < premium_ground_shipping:
    return "Drone shipping is the cheapest method of shipping. It will cost: £" + str(drone_shipping(weight)) 
  else:
    return "Premium ground shipping is the cheapest method of shipping. It will cost: £" + str(premium_ground_shipping)

print(cheapest_shipping(2.5))

