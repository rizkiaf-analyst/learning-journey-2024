def panggil(*nama):
    print("daftar orang yang dipanggil:")
    for orang in nama:
        print(orang)

# pemanggilan fungsi
data = {
    "私": "I",
    "本": "a book",
    "読む":"read"
    }

from collections import Counter
c1 = Counter(data)
print(c1)
print(dict(c1))
print(data)

translated_words = [c1.get(word.lower(), word) for word in data]
print(translated_words)


def cek(*morethan2):
    result = []
    for i in morethan2:
        if(i>2):
            result.append(i)
    return result

def cek2(*morethan2):
    return [i for i in morethan2 if i>2]

def cek3(*morethan2):
    return list(filter(lambda x:x>2,morethan2))

my_list = [1, 2, 3, 4, 5]

print(cek(*my_list))
print(cek2(*my_list))
print(cek3(*my_list))