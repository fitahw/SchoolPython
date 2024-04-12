class AccessDeniedError(Exception):
    pass

class ToManyLoginError(Exception):
    pass

def login(user, password):
    curTry = 0

    while curTry < 3:
        curTry += 1
        inputUser = input("podaj nazwe uzytkownika: ")
        inputPassword = input("podaj haslo: ")
        try:
            if inputUser == user and inputPassword == password:
                print("Logowanie udane!")
                return
            else:
                raise AccessDeniedError(f"Bledna nazwa uzytkownika lub haslo.")
        except AccessDeniedError as e:
            print(f"Error: {e}")
            continue

    raise ToManyLoginError("Przekroczono limit prob logowania")

if __name__ == "__main__":
    try:
        login("admin", "hunter12")
    except ToManyLoginError as e:
        print(f"Error: {e}")
