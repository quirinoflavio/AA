from math import ceil
n, k = map(int, raw_input().split())

red = 2
green = 5
blue = 8

red_notes = n*red
red_notes /= (k*1.0)

green_notes = n*green
green_notes /= (k*1.0)

blue_notes = n*blue
blue_notes /= (k*1.0)

print int(ceil(red_notes)) + int(ceil(green_notes)) + int(ceil(blue_notes))