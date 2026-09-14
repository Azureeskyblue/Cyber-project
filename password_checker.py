password = input("Enter your password: ")
has_upper = False
has_lower = False
has_digit = False
has_symbol = False
for char in password:
  if char.isupper():
      has_upper = True
  if char.islower():
      has_lower = True
  if char.isdigit():
      has_digit = True
  if not char.isalnum():
      has_symbol = True
if has_upper and has_lower and has_digit and has_symbol and len(password) >= 8:
  print("✅ Strong password!")
else:
  print("❌ Weak password. Make sure it has at least:")
  if not has_upper:
      print("- One uppercase letter")
  if not has_lower:
      print("- One lowercase letter")
  if not has_digit:
      print("- One number")
  if not has_symbol:
      print("- One symbol (like !, @, #)")
  if len(password) < 8:
      print("- At least 8 characters")
if not has_upper:
  print("❌ Missing an uppercase letter.")
if not has_lower:
  print("❌ Missing a lowercase letter.")
if not has_digit:
  print("❌ Missing a number.")
if not has_symbol:
  print("❌ Missing a symbol (like !, @, #, etc).")
if len(password) < 8:
  print("❌ Password is too short (minimum 8 characters).")
