def get_float_input(prompt="Skriv ett reelt tal: "):
    while True:
        try:
            user_input = input(prompt)
            float_value = float(user_input)
            return float_value
        except ValueError:#valueError function tests if the value input is not the asked for (in this case intager(int))
            print("inte ett reelt tal, prova igen.")

#make sure module doesnt run dubble output
if __name__ == "__main__":
    float_value = get_float_input()
    print(f"du skrev: {float_value}")
