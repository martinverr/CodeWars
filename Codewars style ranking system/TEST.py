import UserClass


user = UserClass.User()

# Test case - Instruction test case
print("\nTest case - Instruction test case")
print(user.rank)  # => -8
print(user.progress)  # => 0
print(user.inc_progress(-7))
print(user.progress)  # => 10
print(user.inc_progress(-5))  # will add 90 progress
print(user.progress)  # => 0 # progress is now zero
print(user.rank)  # => -7 # rank was upgraded to -7

# Test case - Multipromotion, simple
print("\nTest case - Multipromotion, simple")
user.setRank(-8)
user.setProgress(0)
print(user)
user.inc_progress(-4)  # 4*4*10 progress = 160 progress
print(user)  # rank = -7, progress = 60
user.inc_progress(1)  # 7*7*10 + 60 progress = 550 progress
print(user)  # rank = -2, progress = 50
user.setRank(7)
user.setProgress(99)
user.inc_progress(8)  # 10 + 99 progress = 109 progress
print(user)  # rank = 8, progress = 0

# Test case - Error Handle (invalid ranks)
# No need, passed 255 test cases at this point
