# Your parking gargage class should have the following methods:

class Gargage():
    def __init__(self, tickets, spots, rate):
        self.tickets = tickets
        self.spots = spots
        self.rate = rate
             
# - takeTicket
    def take_ticket(self, ticket):
        self.tickets.remove(ticket)
    
# submit ticket
    def return_ticket(self, ticket):
        self.tickets.append(ticket)

# #remove 1 spot
    def remove_spot(self, spot):
        self.spots.remove(spot)
# #empty spot
    def free_spot(self, spot):
        self.spots.append(spot)
# # pay rate
    def rate_amount(self):
        print(self.rate)
    

# - This should decrease the amount of tickets available by 1
ticket_machine = Gargage([])        

while True:
    user_choice = input('what would you like to do? park or pay? ').lower()
    if user_choice in 'park':
        item = input('take ticket').lower()
        ticket_machine.take_ticket(ticket)
        ticket_machine.remove_spot(spot)

    elif user_choice in 'pay':
        item = ('Please pay.....')
        ticket_machine.return_ticket(ticket)
        ticket_machine.free_spot(spot)
        



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