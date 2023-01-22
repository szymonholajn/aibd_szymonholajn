from textblob import TextBlob


def hello(name):
    output = f'Hello {name}'
    return output


def extract_sentiment(text):
    text = TextBlob(text)

    return text.sentiment.polarity

def text_contain_word(word: str, text: str):
    
    return word in text


def bubblesort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]    
        
    return arr


list1 = [5, 3, 8, 6, 7, 2]  
print("The unsorted list is: ", list1)  
# Calling the bubble sort function  
print("The sorted list is: ", bubblesort(list1))  

         


 
