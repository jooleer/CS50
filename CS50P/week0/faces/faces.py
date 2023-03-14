text = input()
text_smile = text.replace(":)", "🙂")
text_sad = text_smile.replace(":(", "🙁")
print(text_sad)
