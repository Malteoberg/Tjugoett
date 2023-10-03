import random # för att ge slumpmässiga tal eller operationer i spelet.

class Kortlek: #Här skapas en klass för att representera kortleken och egenskaper den har
    def __init__(self): #Den här metoden används för att initalisera objeketet när det skapas, i detta fall dict (kortlek)
        # Jag skapar en kortlek med class och dict där värden för varje kort finns.
        self.kortlek = {
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'Knäckt': 11,
            'Dam': 12,
            'Kung': 13,
            'Ess': 14,
        }

    def blanda(self): #Här blandas kortleken

        random.shuffle(list(self.kortlek.keys())) # Blandar ordningen på korten inför varje hand

class TjugoEtt: # Ny klass för sjävla spelet
    def __init__(self):
        # Skapa en instans av Kortlek för att kunna använda kortleken
        self.kortlek = Kortlek()
        # Spelaren får sina pengar att spela med
        self.total_kr = 100

    def blanda_kortlek(self):
        # Anropar Kortlekens blanda-metod för att blanda kortleken
        self.kortlek.blanda()

    def spela(self):
        # Presentation av spelet och dess regler för användaren
        print('|*******************************|')
        print('|       .:  TJUGOETT  :.       |')
        print('|*******************************|')
        print('Välkommen till tjugoett bordet!')
        print('Detta är reglerna:')
        print('Du ska komma så nära 21 som möjligt utan att gå över 21')
        print('Går du över 21 så förlorar du oavsett vad datorn har för kort')
        print('Knäcktar är värda 11, damer 12, kungar 13 och ess är värd antingen 14 eller 1')
        print('')

        # Huvudspelloop, upprepas så länge spelaren har tillräckligt med pengar
        while self.total_kr >= 10:
            print(f'Du har {self.total_kr} kr kvar.')

            # Loop för att hantera spelarens insats
            while True:
                try:
                    bet = int(input('Hur mycket vill du betta? (Minst 10kr) '))
                    if 10 <= bet <= self.total_kr:
                        print(f'Du har bettat {bet} kr. Lycka till!')
                        break
                    else:
                        print('Ogiltligt belopp, ange belopp mellan 10kr och', self.total_kr, '!')
                except ValueError:
                    print('Ogiltig inmatning. Ange ett heltal.')

            # Blanda kortleken innan varje hand
            self.blanda_kortlek()

            # Yttre loop för att börja om efter varje hand om värdet går över 21
            while True:
                # Dra två kort till spelaren
                första_handen = random.sample(list(self.kortlek.kortlek.keys()), 2)
                print('Din hand är: ', första_handen)

                # Beräkna värdet av spelarens hand
                första_handen_värden = [self.kortlek.kortlek[kort] for kort in första_handen]
                första_handen_värde = sum(första_handen_värden)
                print('Handens värde=', första_handen_värde)

                # Hantera Ess om spelaren går över 21
                if första_handen_värde > 21 and 'Ess' in första_handen:
                    val_ess = input('Vill du ha Ess som 14 eller 1? (14/1) ')
                    ess_värde = 14 if val_ess == '14' else 1
                    första_handen_värden = [ess_värde if kort == 'Ess' else self.kortlek.kortlek[kort] for kort in
                                            första_handen]
                    första_handen_värde = sum(första_handen_värden)

                # Avsluta nuvarande hand om värdet går över 21
                if första_handen_värde > 21:
                    print('Du blev tjock!')
                    break

                # Dra ett kort till datorn
                dator_hand = random.choice(list(self.kortlek.kortlek.keys()))
                print('Datorns hand är: ', dator_hand)

                dator_hand_värde = self.kortlek.kortlek[dator_hand]
                print('Datorns hand värde =', dator_hand_värde)

                # Inre loop för att låta spelaren dra fler kort om de vill
                while True:
                    val = input('Vill du dra ett till kort? (y/n) ')

                    if val == 'y':
                        nytt_kort = random.choice(list(self.kortlek.kortlek.keys()))
                        print('Du fick en:', nytt_kort)
                        ny_hand_värde = self.kortlek.kortlek[nytt_kort]

                        # Hantera Ess för det nya kortet om spelaren går över 21
                        if nytt_kort == 'Ess':
                            val_ess = input('Vill du ha Ess som 14 eller 1? (14/1) ')
                            ny_hand_värde = 14 if val_ess == '14' else 1

                        # Uppdatera värdet av spelarens hand
                        första_handen_värde += ny_hand_värde
                        print('Din hand är nu värd:', första_handen_värde)

                        # Hantera Ess för den nya handen om spelaren går över 21
                        if första_handen_värde > 21 and 'Ess' in första_handen:
                            ess_index = första_handen.index('Ess')
                            första_handen_värden[ess_index] = 1
                            första_handen_värde = sum(första_handen_värden)

                        # Avsluta om spelaren går över 21
                        if första_handen_värde > 21:
                            print('Du blev tjock!')
                            break

                    else:
                        break

                print('Din hand är slutgiltigt värd:', första_handen_värde)

                # Spela datorns hand
                if första_handen_värde <= 21:
                    while dator_hand_värde < första_handen_värde and dator_hand_värde <= 21:
                        nytt_kort = random.choice(list(self.kortlek.kortlek.keys()))
                        print('Datorn drog:', nytt_kort)
                        ny_hand_värde = self.kortlek.kortlek[nytt_kort]

                        # Hantera Ess för datorn om den går över 21
                        if nytt_kort == 'Ess':
                            val_ess = '14' if (dator_hand_värde + 14) <= 21 else '1'
                            ny_hand_värde = 14 if val_ess == '14' else 1

                        dator_hand_värde += ny_hand_värde

                print('Datorns hand =', dator_hand_värde)

                # Bedöm resultatet av handen och uppdatera spelarens pengar
                if första_handen_värde > dator_hand_värde and första_handen_värde <= 21:
                    self.total_kr += bet * 1
                    print(f'Grattis du vann {bet * 1}kr!')
                elif dator_hand_värde > 21:
                    self.total_kr += bet * 1
                    print(f'Datorn blev tjock, du vann {bet * 1}kr!')
                elif dator_hand_värde == första_handen_värde:
                    print('Det blev lika, alltså vann datorn!')
                    self.total_kr -= bet
                else:
                    self.total_kr -= bet
                    print('Datorn vann!')

                break  # Avsluta nuvarande hand och börja om om det inte finns mer pengar

            # Avsluta spelet om spelaren har inga pengar kvar
            if self.total_kr == 0:
                print('Du har förlorat alla pengar, programmet stängs nu ner!')
                break

# Skapa en instans av TjugoEtt och starta spelet
spel = TjugoEtt()
spel.spela()
