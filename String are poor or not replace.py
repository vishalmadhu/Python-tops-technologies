string = "The weather is not poor today, but it was poor yesterday."
index_not = string.find("not")
index_poor = string.find("poor")

if index_not != -1 and index_poor != -1 and index_not < index_poor:
    string = string.replace(string[index_not:index_poor+4], "good")

print(string)