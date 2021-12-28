import argparse
import os

from golf_tracker.tracker import Shot, Hole, Round


class EndRound(Exception):
    pass


# TODO:
#  - Dont ask about distance for driver/tee shots?
#  - Change connection for putting to be putter-specific?


def validated_input(input_name: str):
    # Used instead of the built in input() function
    user_input = input(input_name)
    if user_input not in ('exit', 'quit', 'q'):
        return user_input
    else:
        raise EndRound()


def play_golf(save_path: str = None):
    save_path = save_path or f'{os.getcwd()}/rounds/'

    print("Lets play golf!\n\n"
          "Type 'exit', 'quit' or 'q' at any time to end the round.\n\n"
          "What golf course are you playing?\n")

    try:
        course_name = validated_input('Course: ')
    except EndRound:
        print('\n0 holes played.')
        print(f"\nSaving round in {save_path}...\n")
        round_to_save = Round(holes=[])
        round_to_save.save_round(save_path)
        print(f"Round saved.")
        return round_to_save

    holes = []
    hole_number = 1

    shots = []
    shot_number = 1

    try:
        # Record each hole until the user finishes their round
        while True:
            print(f"\nHole {hole_number}:\n"
                  f"-------\n"
                  f"\nShot {shot_number}:\n")
            shot = record_shot(shot_number)
            shots.append(shot)
            shot_number += 1
            if shot.holed is True:
                hole = Hole(hole_number=hole_number, shots=shots)
                holes.append(hole)

                shots = []
                shot_number = 1

                if hole_number % 9 == 0:
                    print(f'\n----------------------------'
                          f'\n{hole_number} holes played, continue?:'
                          f'\n----------------------------\n')
                    user_input = {'y': True, 'n': False}[validated_input('Continue? y/n: ')]
                    if user_input is False:
                        raise EndRound

                if hole_number == 18:
                    raise EndRound

                hole_number += 1

    except EndRound:
        number_of_holes = len(holes)
        print(f'\n{number_of_holes} holes played.')
        print(f'\nSaving round in {save_path}...\n')

        round_to_save = Round(holes=holes, course=course_name)
        round_to_save.save_round(save_path)

        print('Round saved.')
        return round_to_save


def record_shot(shot_number):
    print("What club did you use?")
    club = validated_input('Club: ')
    print("\nDid it go in the hole?!")
    holed = {'y': True, 'n': False}[validated_input('Holed? y/n: ')]
    if holed is False:
        print("\nHow was the distance?")
        distance = validated_input('Long, Short or Correct?: ')
        print("\nHow was the direction?")
        direction = validated_input('Left, Right or Centre?: ')

    else:
        if shot_number == 1:
            print('\nHole in One!')
        print('\nNailed it.')
        distance = 'correct'
        direction = 'correct'

    print('\nHow was the connection?')
    connection = validated_input('Pure, Fat, Thin, Toe or Heel?: ')

    flight = None
    if club.lower() != 'putter':
        print('\nHow was the flight?')
        flight = validated_input('Hook, Draw, Slice, Fade or Straight?: ')

    return Shot(club=club,
                distance=distance,
                direction=direction,
                connection=connection,
                flight=flight,
                holed=holed)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--save-dir')
    args = parser.parse_args()
    _round = play_golf(save_path=args.save_dir)
