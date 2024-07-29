# Mclip - This is  a multi-clipboard program
import sys
import pyperclip

text = {'agree': "Yes, I agree. That sounds fine to me",
             'busy': "Sorry, can we do this later this week or next week?",
             'upsell': "would you consider making this a monthly donation?"}

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyPhrase] - copy phrase text' )
    sys.exit()


keyPhrase = sys.argv[1] #first command line arg is the keyphrase


if keyPhrase in text:
    pyperclip.copy(text[keyPhrase])
    print('Text for ' + keyPhrase + 'copied in the keyboard')
else:
    print('No text for ' + keyPhrase)
    




