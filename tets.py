import sys

# for line in sys.stdin:
#     print(line.rstrip('\n'))

stdin = sys.stdin.read()
# for line in stdin.split('\n'):
#     if len(line.strip()) != 0:
#         print(line)
stdin = [line for line in stdin.split('\n') if len(line.strip()) != 0]

print(stdin)