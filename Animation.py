import os
import time

frames = [
    r"""
    .--.
   |~_~ |
   |\_/ |
   |    |
 """,
    r"""
     .--.
    |V_V |
    |\_/ |
    |    |
  """,
    r"""
   .--.
  |o_o |
  |/^\ |
  |    |
""",
    r"""
   .--.
  |x_x |
  |/^\ |
  |    |
"""

]

while True:
    for frame in frames:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(frame)
        time.sleep(0.5)
