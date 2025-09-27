# ================================
# Type Casting Examples in Python
# ================================

# 1. Integer → Character (ASCII)
num = 65
print(f"Integer {num} → Character: {chr(num)}")  # 'A'

# 2. Character → Integer (ASCII)
char = 'a'
print(f"Character '{char}' → Integer: {ord(char)}")  # 97

# 3. String → Integer
s_int = "10000"
try:
    print(f"String '{s_int}' → Integer: {int(s_int)}")
except ValueError:
    print(f"Cannot convert '{s_int}' to int")

# 4. String → Float
s_float = "3.1415"
try:
    print(f"String '{s_float}' → Float: {float(s_float)}")
except ValueError:
    print(f"Cannot convert '{s_float}' to float")

# 5. Float → Integer (truncates decimals)
f = 9.99
print(f"Float {f} → Integer: {int(f)}")  # 9

# 6. Integer → Float
i = 42
print(f"Integer {i} → Float: {float(i)}")  # 42.0

# 7. Number → String
n = 123
print(f"Number {n} → String: '{str(n)}'")

# 8. Boolean Conversions
print(f"bool(0) → {bool(0)}")       # False
print(f"bool(42) → {bool(42)}")     # True
print(f"bool('') → {bool('')}")     # False
print(f"bool('Python') → {bool('Python')}")  # True

# 9. Safe Conversion: String to Number with error handling
invalid_str = "hello"
try:
    print(int(invalid_str))
except ValueError:
    print(f"Cannot convert '{invalid_str}' to int")

# 10. Explicit type conversion summary
print("\nSummary:")
print("int(), float(), str(), bool(), chr(), ord() are the main type casting functions in Python.")