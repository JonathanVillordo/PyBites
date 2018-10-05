workout_schedule = {'Friday': 'Shoulders',
                    'Monday': 'Chest+biceps',
                    'Saturday': 'Rest',
                    'Sunday': 'Rest',
                    'Thursday': 'Legs',
                    'Tuesday': 'Back+triceps',
                    'Wednesday': 'Core'}

rest, chill, go_train = 'Rest', 'Chill out!', 'Go train {}'


def get_workout_motd(day):
    """Title case passed in day argument (monday or MONDAY -> Monday)
       and check if it is in the given workout_schedule dict.

       If it is there retrieve the workout, if not raise a KeyError.

       Return the chill or go_train variable depending the retrieved
       workout value ('Rest' or workout bla)

       Trivia: /etc/motd is a file on Unix-like systems that contains
       a 'message of the day'""" 
    day = day[0].upper()+''+day[1:].lower() 
    try:
        value = workout_schedule[day]

    except KeyError:
        raise 
    if value == 'Rest':
        return chill
    else:
        return go_train.format(value)  
#otrasolucion
    day = day.title()

    if day not in workout_schedule:
        raise KeyError(f'{day} is not a valid day')

    workout = workout_schedule.get(day)

    return chill if workout == rest else go_train.format(workout)        


print(get_workout_motd('not-a-day'))
