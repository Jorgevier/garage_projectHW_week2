# Your parking gargage class should have the following methods:

class Gargage():
    def __init__(self, spaces, rate):
        self.tickets = [str(x) for x in range (spaces)]
        self.spots = [str(x) for x in range (spaces)]
        self.rate = rate
             
# - takeTicket
    def take_ticket(self):
        if self.tickets:
            ticket = self.tickets.pop()
            print(f"you're ticket is {ticket}, remember your space!")
            return ticket
        else:
            print('sorry, lot is full!')
            return None
        
    
# submit ticket
def return_ticket(self, ticket):
    self.tickets.append(ticket)

# #remove 1 spot
def remove_spot(self, spot):
    self.spots.pop(spot)
# #empty spot
def free_spot(self, spot):
    self.spots.append(spot)
# # pay rate
def rate_amount(self):
    print(self.rate)
    

# - This should decrease the amount of tickets available by 1
ticket_machine = Gargage(15)        

while True:
    user_choice = input('what would you like to do? park or pay? ').lower()
    if user_choice == 'park':
        spot = input('enter parking spot? ')
        ticket_machine.remove_spot(spot)
        print(f'parking spot {spot}')
#function to lower ticket capacity and spots 
        
    elif user_choice == 'pay':
        ticket = input('Please enter your ticket number? ')
        ticket_machine.return_ticket(ticket)
        spot = input('enter your parking spot ')
        ticket_machine.free_spot(spot)
        print('thank you please exit the lot')
    else:
        print('invalid choice! pls enter park or pay ')
        
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