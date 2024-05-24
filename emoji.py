def emoji_converter(input):
    emoji={
  ":)":"😁",
  ":(":"😔"
 }
    word=input.split(' ')
    output=""
    for ch in word:
     output+=emoji.get(ch,ch) + " "
    return output 
    
input=input(">")
print(emoji_converter(input))
