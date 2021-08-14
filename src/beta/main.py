from beta.tracker import Shot, Hole, Round

BOOL_CONVERTER = {'y': True, 'n': False}


# TODO:
#  - Dont ask about distance for driver/tee shots?
#  - Change connection for putting to be putter-specific?


def play_golf():
    print("Lets play golf!\n\nType 'end' at any time to end the round.\n")
    continue_playing = True

    print("What golf course are you playing?\n")
    user_input = input('Course: ')

    holes = []
    hole_number = 1

    shots = []
    shot_number = 1

    print(f"\nHole {hole_number}:\n"
          f"----------")

    while user_input.lower() != 'end':
        print(f"\nShot {shot_number}:\n")
        shot = record_shot(shot_number)
        shots.append(shot)
        shot_number += 1
        if shot.holed is True:
            hole = Hole(hole_number=hole_number, shots=shots)
            holes.append(hole)

            shots = []
            shot_number = 1

            if hole_number == 9:
                print('\n9 holes played, continue?:')
                continue_playing = BOOL_CONVERTER[input('Continue? y/n')]
                if continue_playing is False:
                    break

            if hole_number == 18:
                break

            hole_number += 1
            print(f"\nHole {hole_number}:\n"
                  f"----------")

    round_to_save = Round(holes=holes)
    save_round(round_to_save)

    return round_to_save


def record_shot(shot_number):
    print("What club did you use?")
    club = input('Club: ')
    print("\nDid it go in the hole?!")
    holed = BOOL_CONVERTER[input('Holed? y/n:')]
    if holed is False:
        print("\nHow was the distance?")
        distance = input('Long, Short or Correct?')
        print("\nHow was the direction?")
        direction = input('Left, Right or Centre?')

    else:
        if shot_number == 1:
            print('\nHole in One!')
        print('\nNailed it.')
        distance = 'correct'
        direction = 'correct'

    print('\nHow was the connection?')
    connection = input('Pure, Fat, Thin, Toe or Heel?')

    flight = None
    if club.lower() != 'putter':
        print('\nHow was the flight?')
        flight = input('Hook, Draw, Slice, Fade or Straight?')

    return Shot(club=club,
                distance=distance,
                direction=direction,
                connection=connection,
                flight=flight,
                holed=holed)


def save_round(round_to_save):
    number_of_holes = len(round_to_save.holes)
    print(f'\n{number_of_holes} holes played.')
    print('\nSaving Round...')
    # round_data = round_to_save.get_round_data()
    # now = datetime.now()
    # round_data.to_csv(f'round_{now.date()}')
