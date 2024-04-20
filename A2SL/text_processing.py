from nltk.tokenize import word_tokenize
import nltk
from nltk.stem import WordNetLemmatizer
import os

def Text_processing(text):
	
    # text = "My name is Jalaj"
    #tokenizing the sentence
    text.lower()
    #tokenizing the sentence
    words = word_tokenize(text)

    tagged = nltk.pos_tag(words)
    tense = {}
    tense["future"] = len([word for word in tagged if word[1] == "MD"])
    tense["present"] = len([word for word in tagged if word[1] in ["VBP", "VBZ","VBG"]])
    tense["past"] = len([word for word in tagged if word[1] in ["VBD", "VBN"]])
    tense["present_continuous"] = len([word for word in tagged if word[1] in ["VBG"]])



    #stopwords that will be removed
    stop_words = set(["mightn't", 're', 'wasn', 'wouldn', 'be', 'has', 'that', 'does', 'shouldn', 'do', "you've",'off', 'for', "didn't", 'm', 'ain', 'haven', "weren't", 'are', "she's", "wasn't", 'its', "haven't", "wouldn't", 'don', 'weren', 's', "you'd", "don't", 'doesn', "hadn't", 'is', 'was', "that'll", "should've", 'a', 'then', 'the', 'mustn', 'i', 'nor', 'as', "it's", "needn't", 'd', 'am', 'have',  'hasn', 'o', "aren't", "you'll", "couldn't", "you're", "mustn't", 'didn', "doesn't", 'll', 'an', 'hadn', 'whom', 'y', "hasn't", 'itself', 'couldn', 'needn', "shan't", 'isn', 'been', 'such', 'shan', "shouldn't", 'aren', 'being', 'were', 'did', 'ma', 't', 'having', 'mightn', 've', "isn't", "won't"])



    #removing stopwords and applying lemmatizing nlp process to words
    lr = WordNetLemmatizer()
    filtered_text = []
    for w,p in zip(words,tagged):
        if w not in stop_words:
            if p[1]=='VBG' or p[1]=='VBD' or p[1]=='VBZ' or p[1]=='VBN' or p[1]=='NN':
                filtered_text.append(lr.lemmatize(w,pos='v'))
            elif p[1]=='JJ' or p[1]=='JJR' or p[1]=='JJS'or p[1]=='RBR' or p[1]=='RBS':
                filtered_text.append(lr.lemmatize(w,pos='a'))

            else:
                filtered_text.append(lr.lemmatize(w))


    #adding the specific word to specify tense
    words = filtered_text
    temp=[]
    for w in words:
        if w=='I':
            temp.append('Me')
        else:
            temp.append(w)
    words = temp
    probable_tense = max(tense,key=tense.get)

    if probable_tense == "past" and tense["past"]>=1:
        temp = ["Before"]
        temp = temp + words
        words = temp
    elif probable_tense == "future" and tense["future"]>=1:
        if "Will" not in words:
                temp = ["Will"]
                temp = temp + words
                words = temp
        else:
            pass
    elif probable_tense == "present":
        if tense["present_continuous"]>=1:
            temp = ["Now"]
            temp = temp + words
            words = temp

    pre_vid = ['0.mp4', '1.mp4', '2.mp4', '3.mp4', '4.mp4', '5.mp4', '6.mp4', '7.mp4', '8.mp4', '9.mp4', 'A.mp4', 'After.mp4', 'Again.mp4', 'Against.mp4', 'Age.mp4', 'All.mp4', 'Alone.mp4', 'Also.mp4', 'And.mp4', 'Ask.mp4', 'At.mp4', 'B.mp4', 'Be.mp4', 'Beautiful.mp4', 'Before.mp4', 'Best.mp4', 'Better.mp4', 'Busy.mp4', 'But.mp4', 'Bye.mp4', 'C.mp4', 'Can.mp4', 'Cannot.mp4', 'Change.mp4', 'College.mp4', 'Come.mp4', 'Computer.mp4', 'D.mp4', 'Day.mp4', 'Distance.mp4', 'Do Not.mp4', 'Do.mp4', 'Does Not.mp4', 'E.mp4', 'Eat.mp4', 'Engineer.mp4', 'F.mp4', 'Fight.mp4', 'Finish.mp4', 'From.mp4', 'G.mp4', 'Glitter.mp4', 'Go.mp4', 'God.mp4', 'Gold.mp4', 'Good.mp4', 'Great.mp4', 'H.mp4', 'Hand.mp4', 'Hands.mp4', 'Happy.mp4', 'Hello.mp4', 'Help.mp4', 'Her.mp4', 'Here.mp4', 'His.mp4', 'Home.mp4', 'Homepage.mp4', 'How.mp4', 'I.mp4', 'Invent.mp4', 'It.mp4', 'J.mp4', 'K.mp4', 'Keep.mp4', 'L.mp4', 'Language.mp4', 'Laugh.mp4', 'Learn.mp4', 'M.mp4', 'ME.mp4', 'mic3.png', 'More.mp4', 'My.mp4', 'N.mp4', 'Name.mp4', 'Next.mp4', 'Not.mp4', 'Now.mp4', 'O.mp4', 'Of.mp4', 'On.mp4', 'Our.mp4', 'Out.mp4', 'P.mp4', 'Pretty.mp4', 'Q.mp4', 'R.mp4', 'Right.mp4', 'S.mp4', 'Sad.mp4', 'Safe.mp4', 'See.mp4', 'Self.mp4', 'Sign.mp4', 'Sing.mp4', 'So.mp4', 'Sound.mp4', 'Stay.mp4', 'Study.mp4', 'T.mp4', 'Talk.mp4', 'Television.mp4', 'Thank You.mp4', 'Thank.mp4', 'That.mp4', 'They.mp4', 'This.mp4', 'Those.mp4', 'Time.mp4', 'To.mp4', 'Type.mp4', 'U.mp4', 'Us.mp4', 'V.mp4', 'W.mp4', 'Walk.mp4', 'Wash.mp4', 'Way.mp4', 'We.mp4', 'Welcome.mp4', 'What.mp4', 'When.mp4', 'Where.mp4', 'Which.mp4', 'Who.mp4', 'Whole.mp4', 'Whose.mp4', 'Why.mp4', 'Will.mp4', 'With.mp4', 'Without.mp4', 'Words.mp4', 'Work.mp4', 'World.mp4', 'Wrong.mp4', 'X.mp4', 'Y.mp4', 'You.mp4', 'Your.mp4', 'Yourself.mp4', 'Z.mp4']
    pre_vid_lower = [x.lower() for x in pre_vid]

    # print(pre_vid)
    # file_dir=""
    filtered_text = []
    for w in words:
        flag=False
        path = w + ".mp4"
        # file_dir = os.listdir("{}/assets/".format(os.getcwd()))
        for i in pre_vid_lower:
            if i==path:
                filtered_text.append(w)
                flag=True
        
        #splitting the word if its animation is not present in database
        if not flag:
            for c in w:
                filtered_text.append(c)
        #otherwise animation of word
        # else:
        #     filtered_text.append(w)
    # print(file_dir)        
    words = filtered_text;
    # print("filtered text:",words)
    return words

