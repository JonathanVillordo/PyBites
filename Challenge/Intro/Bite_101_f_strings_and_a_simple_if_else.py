MIN_DRIVING_AGE = 18

def allowed_driving(name, age):
    """Print name is allowed / not allowed to drive based on MIN_DRIVING_AGE"""
    if age >= MIN_DRIVING_AGE:
        print("%s is allowed to drive"%name)

    else:
        print("%s is not allowed to drive"%name)


allowed_driving('Jonathan',18)
