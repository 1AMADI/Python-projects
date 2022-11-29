import os
z=True
bidders={}
while z== True:
    # while loop is used to make the bidding happen until z is true.
    name=input("enter your name: \n")
    os.system("cls")
    bid= int(input("enter your bid: \n"))
    os.system("cls")
    bidders[name]=bid
    ask=input("IS THERE ANY MORE BIDDERS Y/N").lower()
    os.system("cls")
    # this line clears the screen so that other bidders dont see the others peoples bids.
    if ask=="n":
        z=False
        highest_bid=0
        highest_bidder=""
        for bidder in bidders:
            current_bid=bidders[bidder]
            if current_bid>highest_bid:
                highest_bid=current_bid
                highest_bidder=bidder
        print(f"HIGHEST BIDDER {highest_bidder} AND HIGHEST BID IS {highest_bid}")
        # this  prints the highest bidder along with the highest bid placed.