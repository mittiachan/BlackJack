from blackjack_rules import *

while True:
    print('Welcome to BLACKJACK ==21==')

    # Create & shuffle the deck, deal two cards to each player
    current_deck = Deck(suits, ranks)
    current_deck.shuffle()

    # Set up the Player's chips
    balance = int(input('How many chips do you have? -> '))

    # Prompt the Player for their bet
    bet = take_bet(balance)

    # Show cards (but keep one dealer card hidden)
    player = Hand()
    dealer = Hand()
    player.add_card(current_deck.deal())
    player.add_card(current_deck.deal())
    dealer.add_card(current_deck.deal())
    dealer.add_card(current_deck.deal())
    show_some(player, dealer)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_stand = hit_or_stand(current_deck, player)
        if not hit_stand:
            playing = False

        # Show cards (but keep one dealer card hidden)
        show_some(player, dealer)
        player.adjust_for_ace()

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_busts(player.value):
            balance = Chips(balance, bet)
            balance.lose_bet()
            show_all(player, dealer)
            print('BUSTED!!......BETTER LUCK NEXT TYMMEEE   :((  ')
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if not player_busts(player.value):

        # Show all cards
        show_all(player, dealer)

        # Run different winning scenarios
        if dealer_wins(player.value, dealer.value):
            balance = Chips(balance, bet)
            balance.lose_bet()
            print('DEALER WINS!!......BETTER LUCK NEXT TIME  :(')

        else:
            while dealer.value < 17:
                dealer.add_card(current_deck.deal())
                show_all(player, dealer)

            if player_wins(player.value, dealer.value):
                balance = Chips(balance, bet)
                balance.win_bet()
                if player.value == 21:
                    print('BLACKJACKKKKKKK')
                print('PLAYER WINS........CONGRATULATIONS   :))')

            if dealer_wins(player.value, dealer.value):
                balance = Chips(balance, bet)
                balance.lose_bet()
                print('THE DEALER HAS WON........:(((')

            if player.value == dealer.value:
                balance = Chips(balance, bet)
                print('ITS a TIE TIE FISHHHH')

    # Inform Player of their chips total
    print("\nYour remaining chip balance is {}\n".format(balance))

    # Ask to play again
    if not play_again():
        break
