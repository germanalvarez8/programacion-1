# Posicional obligatorio
def cheers(name, age):
    print(f"cheers {name}, you have {age} yo")

cheers('ger', 24)

# Posicional no obligatorio
def cheersToFriends(*args):
    for arg in args:
        print(f"cheers {arg}")

cheersToFriends('ger', 'lucas', 'luis')

# Keyword con posicional obligatorio
# Parametro con valor por defecto (forma 3)
def cheersToFriendFrom(name, city="Ucacha"):
    print(f"cheers {name}, you are from {city}")

cheersToFriendFrom('ger', city = 'Rio cuarto')

def cheersToFriendsFrom(*args, city="Ucacha", **kwargs):
    for arg in args:
        for kwarg in kwargs:
            print(f"cheers {arg}, you are from {city} and do you like {kwarg}")

cheersToFriendsFrom('ger', 'lucas', 'luis', city = 'Rio cuarto', def1='def1', def2='def2', def3='def3')

#La cuarta forma es qargs