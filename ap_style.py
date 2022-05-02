
# the ultimate goal of this project is to create a bot capable of running an ap style check script whenever it is added via email to a google doc. This bot will also then update a database which 
# tallies the number of instances of each type of ap style violation to create a better picture of what the leadership at the review might need to educate reporters on during dukabi
# since this would purely be a minor quality of life script it should not require any extra effort on the part of reporters or editory to make it usable.

#first we need a dictionary mapping common ap style mistakes to their correct counterparts
# for instance

mistakes = {
        "Months":{
            "January":"Jan.",
            "February":"Feb.",
            "March":"Mar.",
            "August":"Aug.",
            "September":"Sep.",
            "November":"Nov.",
            "December":"Dec."
                },
        "Numbers":{
            "1":"one",
            "2":"two",
            "3":"three",
            "4":"four",
            "5":"five",
            '6':"six",
            '7':"seven",
            '8':"eight",
            '9':"nine",
            },
        }

# then we need a function which accepts a really long string as input and parses it by treating each word separated by a space as its own entity

def sentences(text):
    '''
    gets the sentences of a text
    '''
    return text.split(".")

def words(sentence):
    '''
    gets the words of sentence
    '''
    return sentence.split(" ")

# def report_error(keyword, errors):
#     if keyword not in errors:
#         errors[keyword] = 1
#     else:
#         errors[keyword] += 1

def check_usage(words):
    '''
    looks at the words in the text and replaces those which violate the ap style guide.
    '''
    for i, word in enumerate(words):
        for error in mistakes:
            if word in mistakes[error]:
                words[i] = mistakes[error][word]
                print(f'error type: {error}\n Correction {word} --> {mistakes[error][word]}\n')                
                #report_error(error)
    return words

def reconstruct(arr, c):
    '''
    recombines the split text into a sentence or paragraph
    '''
    new = ""
    for component in arr[:-1]:
        new = new + component + c

    new = new + arr[-1]
    return new

def check(par):
    '''
    entire process
    '''
    # break paragraph into sentences
    par = sentences(par)
    for i, sen in enumerate(par):
        # break each sentence into words, check the words used for errors and reconstruct the sentence for each sentence in the paragraph
        par[i] = reconstruct(check_usage(words(sen)), ' ')
    
    #reconstruct the entire paragraph
    par = reconstruct(par, '.')
    print(par)     

 
if __name__ == "__main__":
    par = input("\n") 
    check(par)

