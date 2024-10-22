def draw_pyramid(height):
  
  for i in range(height):
        print(" " * (height - i - 1), end="")
        print("/", end="")
        print(" " * (2 * i), end="")
        print("\\")
  print("-" * (2 * height))

draw_pyramid(int(input("hauteur du triangle")))     