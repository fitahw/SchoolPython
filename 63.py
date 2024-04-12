import random
from collections import Counter

def roll():
    return [random.randint(1,6) for _ in range(5)]

def setCheck(kosci):
    n = set(kosci)
    
    remaining = Counter(n)
    liczby = []
    for val in kosci:
        if remaining[val]:
            remaining[val] -= 1
        else:
            liczby.append(val)
    set(liczby)

    if len(n) == 1:
        print("Poker")
        return {8: liczby}
    
    if len(n) == 2:
        if kosci.count(kosci[0]) == 4 or kosci.count(kosci[1]) == 4: #jesli pierwsza lub druga cyfra powtarza sie 4 razy
            print("Kareta")
            return {7: liczby}
        else:
            print("Full")
            return {6: liczby}

    if len(n) == 5:
        if sorted(kosci) == list(range(max(kosci)+1)):
            if 6 in kosci:
                print("Duzy Street")
                return {5: liczby}
            else:
                print("Maly Street")
                return {4: liczby}

    if len(n) == 3:
        if kosci.count(max(n, key=kosci.count)) == 3:
            print("Trojka")
            return {3: liczby}
        else:
            print("Dwie Pary")
            return {2: liczby}
    
    if len(n) == 4:
        print("Para")
        return {1: liczby}

    print("Nic")
    return{0: liczby}

def game():
    print("Witaj w grze w kości z komputerem!")
    
    playerRoll = roll()
    dealerRoll = roll()

    print("\nTwoje kosci:", playerRoll)
    print("Komputerowe kosci:", dealerRoll)
    
    print("\nTwój układ:")
    playerSet = setCheck(playerRoll)
    print("Układ komputera:")
    dealerSet = setCheck(dealerRoll)
    
    playerPoints = list(playerSet.keys())[0]
    dealerPoints = list(dealerSet.keys())[0]
    if playerPoints > dealerPoints:
        print("\nWygrana :-)")
    elif playerPoints < dealerPoints:
        print("\nPrzegrana :-(.")
    else:
        #W razie remisu, dodaje liczby z par/trojek (np. 3 3 3 2 2 = 3 + 2 = 5 | 5 5 5 1 1 = 5 + 1 = 6, 6 wygrywa)
        playerSum = 0
        dealerSum = 0
        playerValues = list(playerSet.values())
        dealerValues = list(dealerSet.values())
        for num in playerValues:
            for i in num:
                playerSum = playerSum + i

        for num in dealerValues:
            for i in num:
                dealerSum = dealerSum + i

        if playerSum > dealerSum:
            print("\nWygrana :-)")
        else:
            print("\nPrzegrana :-(")

if __name__ == "__main__":
    game()