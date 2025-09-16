# def profile(name,age,lang1,lang2,lang3,lang4,lang5):
#     print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")
#     print(lang1,lang2,lang3,lang4,lang5)
def profile(name,age,*language):
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


profile("전현준",20,"Python","Java","C","C++","C#","JavaSript")
profile("박서린",25, "Kotlin","Swift")