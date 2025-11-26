print("Hello I am Chatbot...type exit for exit from the chat")
while True:
    user=input('user:')
    if user=="hello":
        print("Chatbot: hello, Good morning")
    elif user=="good morning":
        print("Chatbot: how can i help you")
    elif user=="how are you":
        print("Chatbot: i am fine")
    elif user=="exit":
        print("Chatbot: thanks you")
        break
    else:
        print("sorry,i can't understand that thing")
