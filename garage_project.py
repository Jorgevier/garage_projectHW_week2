# Your parking gargage class should have the following methods:
# - takeTicket    
# submit ticket


# #remove 1 spot

# #empty spot

# # pay rate

    

# - This should decrease the amount of tickets available by 1

#function to lower ticket capacity and spots 
        
        
#function to display rate and free up a spot and ticket
        
#a way to tell it we are at full capacity



# total_spot = Gargage(20)

# - This should decrease the amount of parkingSpaces available by 1

# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable


# - If the payment variable is not empty then 
 # (meaning the ticket has been paid) -> 
# display a message to the user that their ticket has been paid and they have 15mins to leave
        

# - This should update the "currentTicket" dictionary key "paid" to True
# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary
class Garage():
    def __init__(self, spaces, rate):
        self.tickets = [str(x) for x in range(spaces)]
        self.spots = [str(x) for x in range(spaces)]
        self.rate = rate

    def take_ticket(self):
        if self.tickets:
            ticket = self.tickets.pop()
            print(f"Your ticket is {ticket}, remember your space!")
            return ticket
        else:
            print('Sorry, lot is full!')
            return None

    def return_ticket(self, ticket):
        self.tickets.append(ticket)

    def remove_spot(self, spot):
        self.spots.remove(spot)

    def free_spot(self, spot):
        self.spots.append(spot)

    def rate_amount(self):
        print(self.rate)

# Creating an instance of the Garage class
ticket_machine = Garage(15, 10)

while True:
    user_choice = input('What would you like to do? Park or Pay? ').lower()

    if user_choice == 'park':
        spot = input('Enter parking spot: ')
        ticket_machine.remove_spot(spot)
        print(f'Parked in spot {spot}')

    elif user_choice == 'pay':
        ticket = input('Please enter your ticket number: ')
        ticket_machine.return_ticket(ticket)

        spot = input('Enter your parking spot: ')
        ticket_machine.free_spot(spot)
        print('Thank you! Please exit the lot.')

    else:
        print('Invalid choice! Please enter "Park" or "Pay".')







