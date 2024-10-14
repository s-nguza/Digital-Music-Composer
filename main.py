def user_input():
  print("Welcome to our Digital Music Composer")
  temp = int(input("What temp do you want(BPM): ")
  mood = input("What mood would you like(sad,happy,love): ")
  key = input("Choose a key (C, D, E, F, G, A, B): ").strip().upper()
  return temp,mood,key

def main():
  temp,mood,key = user_input()

  compose_music(mood, tempo, key)


if __name__ == "__main__":
    main()
