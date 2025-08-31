def get_num_words(file):
    return file.split()

def sort_on(items):
    return items["num"]

def get_char_count(file):
    list_of_counts = []
    for c in file:
        if not c.isalpha():
            continue
        c = c.lower()
        found = False
        for i in list_of_counts:
            if i["name"] == c:
                found = True
                i.update({"num": i["num"]+1})
        if found == False:
            #make a new dictionary and add it
            new = {"name": c,"num":1}
            list_of_counts.append(new)




    list_of_counts.sort(reverse=True, key=sort_on)
    return list_of_counts

