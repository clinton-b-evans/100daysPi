file1_list = [int(x.strip("\n")) for x in open("file1.txt", "r")]
file2_list = [int(x.strip("\n")) for x in open("file2.txt", "r")]
result = [number for number in file1_list if number in file2_list]

# Write your code above 👆
print(result)
