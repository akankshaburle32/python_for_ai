sentence = "I Love    python  toooooooo   much"

raw_data = sentence.split(" ")

words = []
for text in raw_data:
    if text:
     words.append(text)


     clean_data = " ".join(words)
     print("Raw_data:", raw_data)
     print("clean_data:, clean_data")