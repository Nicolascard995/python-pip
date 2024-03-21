import random


# Función para elegir las opciones del juego
def choose_options():
  # Definimos las opciones del juego
  options = ('piedra', 'papel', 'tijera')
  # Pedimos al usuario que elija una opción
  user_option = input('Elige piedra, papel o tijera => ')
  # Convertimos la opción a minúscula para evitar errores
  user_option = user_option.lower()

  # Si el usuario no elige una opción válida, devolvemos None
  if not user_option in options:
    print('Esa opción no es válida')
    return None, None

  # Elegimos una opción aleatoria para la computadora
  computer_option = random.choice(options)

  # Mostramos las opciones elegidas
  print('Opción del usuario =>', user_option)
  print('Opción de la computadora =>', computer_option)
  return user_option, computer_option

# Función para revisar las reglas del juego y decidir quién gana
def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print('Empate!')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('Piedra gana a tijera')
      print('¡El usuario ganó! 🎉👏🏽')
      user_wins += 1
    else:
      print('Papel gana a piedra')
      print('¡La computadora ganó! 💻😔')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('Papel gana a piedra')
      print('¡El usuario ganó! 🎉👏🏽')
      user_wins += 1
    else:
      print('Tijera gana a papel')
      print('¡La computadora ganó! 💻😔')
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('Tijera gana a papel')
      print('¡El usuario ganó! 🎉👏🏽')
      user_wins += 1
    else:
      print('Piedra gana a tijera')
      print('¡La computadora ganó! 💻😔')
      computer_wins += 1
  return user_wins, computer_wins

# Función para revisar quién es el ganador del juego
def check_winner(user_wins, computer_wins):
  if computer_wins == 2:
    print('¡El ganador es la computadora! 💻🏆')
    exit()
  if user_wins == 2:
    print('¡El ganador es el usuario! 🎉🏆')
    exit()

# Función principal para ejecutar el juego
def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1

    # Comenzamos el juego
    while True:
        print('*' * 20)
        print(f'Round {rounds}')
        print('*' * 20)

        # Llamar a la función para elegir las opciones
        user_option, computer_option = choose_options()

        if user_option is None:
            continue

        # Llamar a la función para revisar las reglas del juego y decidir quién gana
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

        # Llamar a la función para revisar quién es el ganador del juego
        check_winner(user_wins, computer_wins)

        rounds += 1

        # Imprimir el contador de victorias
        print(f'Contador de victorias - Usuario: {user_wins}, Computadora: {computer_wins}')

# Llamar a la función principal para ejecutar el juego
run_game()