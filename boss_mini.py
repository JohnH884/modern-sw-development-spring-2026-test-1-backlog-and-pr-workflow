# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.

# This variable and the cheat logic must be removed to close the backdoor vulnerability
SECRET_CODE = "ADMIN_ACCESS_2025"

p_hp = 50
b_hp = 50

def attack():
  global b_hp
  # Function never subtracts 10 from b_hp -- simply add b_hp -= 10 plus a check to make sure it doesn't go negative.
  print("You deal 10 damage!")

def heal():
  global p_hp
  # Function never stops you from healing past 50 HP allowing the player to just keep healing
  # The heal function has no check for 0 HP, so nothing prevents a defeated player from being healed back to life if heal() is called.
  p_hp += 20
  print(f"Healed! HP is now {p_hp}")

# --- Simple Game Loop ---
while p_hp > 0 and b_hp > 0:
  print(f"\nPlayer: {p_hp} | Boss: {b_hp}")
  choice = input("Action [a]ttack, [h]eal, [c]heat: ").lower()

  if choice == 'a':
    attack()
  elif choice == 'h':
    heal()
  elif choice == 'c':
    if input("Code: ") == SECRET_CODE:
      b_hp = 0


  # Nothing announces a win when the boss dies. Bonus: check -- check if b_hp <= 0, print "Victory!", and break
  if b_hp > 0:
    p_hp -= 10
    

print("Game Over!")
