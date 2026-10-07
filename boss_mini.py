# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.

p_hp = 50
b_hp = 50
# SECURITY: This hardcoded credential enables a backdoor that bypasses combat.
# Remove SECRET_CODE and the associated cheat branch, including the cheat
# option advertised in the input prompt.
SECRET_CODE = "ADMIN_ACCESS_2025"
MAX_HP = 50

def attack():
    global b_hp
# ATTACK: The original function printed damage without reducing boss health.
# The required repair is b_hp -= 10 before reporting damage.
# Without that state update, attacks cannot progress toward defeating the boss.
    b_hp -= 10
    if b_hp < 0:
        b_hp = 0
    print("You deal 10 damage!")

def heal():
    global p_hp
    if p_hp <= 0:
        print("You cannot heal when defeated.")
        return
# HEALING: An unguarded addition can exceed 50 HP or revive a defeated player.
# Reject p_hp <= 0 before adding health, then cap the result at 50.
# For a living player, use p_hp = min(MAX_HP, p_hp + 20), with MAX_HP = 50.
    p_hp += 20
    if p_hp > MAX_HP:
        p_hp = MAX_HP
    print(f"Healed! HP is now {p_hp}")

# --- Simple Game Loop ---
# VICTORY: The loop condition alone does not announce a win.
# After the player's action, check b_hp <= 0, print("Victory!"),
# and break before boss retaliation or another input.
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
    else:
        print("Invalid choice! Please choose 'a', 'h', or 'c'.")

    if b_hp <= 0:
        print("Victory!")
        break

    if b_hp > 0:
        p_hp -= 10

print("Game Over!")
