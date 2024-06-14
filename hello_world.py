if __name__ == '__main__':
  for name in ['Helen', 'Wenli', 'Yi']:
    print('The value of the variable "name" is %s' % name)
    # TODO (blouielou): fix the line below so that it will print out different names each time
    print('Hello name!')
    print('      ')


print (3.14 + 2.2)
print('3.14' + 'oier')

print('%i' % (3.14))


print('-----------')




for (x, y, z) in [(2, 0, 1), (30, 100, 2.2), (-2, 3.14, 100000000)]:
  print(z, y, x)



num_apples = 300
num_oranges = 2 * num_apples
comment = "great"
if num_apples > 100:
  comment = "fantastic"

print('there are %i apples, and %i oranges. %s!' % (num_apples, num_oranges, comment))

'''
max_time_steps = 5
for time in range(max_time_steps):
  if time == 0:
    pass
  else:
    print("time = %s" % time)
'''

max_time_steps = 5
for time in range(max_time_steps - 1):
  print("time = %s" % (time + 1))
print("ok")

CURSOR_UP = "\033[1A"
CLEAR = "\x1b[2K"
print("apple")
print("orange")
print("pear")
# clears TWO lines
print(CURSOR_UP + CLEAR + CURSOR_UP + CLEAR, end="")
print("pineapple")