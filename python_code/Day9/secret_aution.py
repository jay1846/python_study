bidder = {}

def return_max(bidder):
    max_value = 0
    winner_name =''

    for name,price in bidder.items():
         if price > max_value:
              max_value = price
              winner_name = name

    return winner_name, max_value


while True:
    name = input("Wwhat is your name? ")
    bid = int(input("What is your bid?: $"))
    
    bidder[name] = bid
   
    answer = input("Is there any other people who wants to bid? (y/n)").lower()
    if 'n' in answer:
            highest_name, highest_value = return_max(bidder)
            print(f"{highest_name} has called ${highest_value} as highest price")
            break
