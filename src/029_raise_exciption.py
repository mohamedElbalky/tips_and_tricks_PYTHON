
user_input = 11

if user_input % 2 == 1:
    error = "Must be even number of players"
    raise Exception(error)

print(f"Team: {user_input/2} players")