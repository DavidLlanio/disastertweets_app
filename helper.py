import os
import re
import pickle

# Static file path
static = os.path.join(os.getcwd(), "static")

# Get the Count Vectorizer
with open(os.path.join(static, "disasterNLPcountvec.pkl"), "rb") as f:
    cvec = pickle.load(f)

# Get the model
with open(os.path.join(static, "disasterNLPmodel.pkl"), "rb") as q:
    classifier = pickle.load(q)

def get_prediction(strin):
    strin_p = preprocess_text(strin)
    strin_t = cvec.transform([strin_p]).toarray()

    prediction = classifier.predict(strin_t)

    return prediction

# Grammar cleaning function, credit: https://www.kaggle.com/hritikchaturvedi/disaster-prediction-roberta-large
def gcleaner(tweet):
  # Acronyms and miswritten words
  tweet = re.sub(r"Typhoon-Devastated", "typhoon devastated", tweet)
  tweet = re.sub(r"TyphoonDevastated", "typhoon devastated", tweet)
  tweet = re.sub(r"typhoondevastated", "typhoon devastated", tweet)
  tweet = re.sub(r"MH370", "Malaysia Airlines Flight", tweet)
  tweet = re.sub(r"MH", "Malaysia Airlines Flight", tweet)
  tweet = re.sub(r"mh370", "Malaysia Airlines Flight", tweet)
  tweet = re.sub(r"year-old", "years old", tweet)
  tweet = re.sub(r"yearold", "years old", tweet)
  tweet = re.sub(r"yr old", "years old", tweet)
  tweet = re.sub(r"PKK", "Kurdistan Workers Party", tweet)
  tweet = re.sub(r"MP", "madhya pradesh", tweet)
  tweet = re.sub(r"rly", "railway", tweet)
  tweet = re.sub(r"CDT", "Central Daylight Time", tweet)
  tweet = re.sub(r"sensorsenso", "sensor senso", tweet)
  tweet = re.sub(r"pm", "", tweet)
  tweet = re.sub(r"PM", "", tweet)
  tweet = re.sub(r"nan", " ", tweet)
  tweet = re.sub(r"terrorismturn", "terrorism turn", tweet)
  tweet = re.sub(r"epicente", "epicenter", tweet)
  tweet = re.sub(r"epicenterr", "epicenter", tweet)
  tweet = re.sub(r"WAwildfire", "Washington Wildfire", tweet)
  tweet = re.sub(r"prebreak", "pre break", tweet)
  tweet = re.sub(r"nowplaying", "now playing", tweet)
  tweet = re.sub(r"RT", "retweet", tweet)
  tweet = re.sub(r"EbolaOutbreak", "Ebola Outbreak", tweet)
  tweet = re.sub(r"LondonFire", "London Fire", tweet)
  tweet = re.sub(r"IDFire", "Idaho Fire", tweet)
  tweet = re.sub(r"withBioterrorism&use", "with Bioterrorism & use", tweet)
  tweet = re.sub(r"NASAHurricane", "NASA Hurricane", tweet)
  tweet = re.sub(r"withweapons", "with weapons", tweet)
  tweet = re.sub(r"NuclearPower", "Nuclear Power", tweet)
  tweet = re.sub(r"WhiteTerrorism", "White Terrorism", tweet)
  tweet = re.sub(r"MyanmarFlood", "Myanmar Flood", tweet)
  tweet = re.sub(r"ExtremeWeather", "Extreme Weather", tweet)

  # Special characters
  tweet = re.sub(r"%20", " ", tweet)
  tweet = re.sub(r"%", " ", tweet)
  tweet = re.sub(r"@", " ", tweet)
  tweet = re.sub(r"#", " ", tweet)
  tweet = re.sub(r"'", " ", tweet)
  tweet = re.sub(r"\x89û_", " ", tweet)
  tweet = re.sub(r"\x89ûò", " ", tweet)
  tweet = re.sub(r"16yr", "16 year", tweet)
  tweet = re.sub(r"re\x89û_", " ", tweet)
  tweet = re.sub(r"\x89û", " ", tweet)
  tweet = re.sub(r"\x89Û", " ", tweet)
  tweet = re.sub(r"re\x89Û", "re ", tweet)
  tweet = re.sub(r"re\x89û", "re ", tweet)
  tweet = re.sub(r"\x89ûª", "'", tweet)
  tweet = re.sub(r"\x89û", " ", tweet)
  tweet = re.sub(r"\x89ûò", " ", tweet)
  tweet = re.sub(r"\x89Û_", "", tweet)
  tweet = re.sub(r"\x89ÛÒ", "", tweet)
  tweet = re.sub(r"\x89ÛÓ", "", tweet)
  tweet = re.sub(r"\x89ÛÏWhen", "When", tweet)
  tweet = re.sub(r"\x89ÛÏ", "", tweet)
  tweet = re.sub(r"China\x89Ûªs", "China's", tweet)
  tweet = re.sub(r"let\x89Ûªs", "let's", tweet)
  tweet = re.sub(r"\x89Û÷", "", tweet)
  tweet = re.sub(r"\x89Ûª", "", tweet)
  tweet = re.sub(r"\x89Û\x9d", "", tweet)
  tweet = re.sub(r"å_", "", tweet)
  tweet = re.sub(r"\x89Û¢", "", tweet)
  tweet = re.sub(r"\x89Û¢åÊ", "", tweet)
  tweet = re.sub(r"fromåÊwounds", "from wounds", tweet)
  tweet = re.sub(r"åÊ", "", tweet)
  tweet = re.sub(r"åÈ", "", tweet)
  tweet = re.sub(r"JapÌ_n", "Japan", tweet)    
  tweet = re.sub(r"Ì©", "e", tweet)
  tweet = re.sub(r"å¨", "", tweet)
  tweet = re.sub(r"SuruÌ¤", "Suruc", tweet)
  tweet = re.sub(r"åÇ", "", tweet)
  tweet = re.sub(r"å£3million", "3 million", tweet)
  tweet = re.sub(r"åÀ", "", tweet)

  # Contractions
  tweet = re.sub(r"he's", "he is", tweet)
  tweet = re.sub(r"there's", "there is", tweet)
  tweet = re.sub(r"We're", "We are", tweet)
  tweet = re.sub(r"That's", "That is", tweet)
  tweet = re.sub(r"won't", "will not", tweet)
  tweet = re.sub(r"they're", "they are", tweet)
  tweet = re.sub(r"Can't", "Cannot", tweet)
  tweet = re.sub(r"wasn't", "was not", tweet)
  tweet = re.sub(r"don\x89Ûªt", "do not", tweet)
  tweet = re.sub(r"aren't", "are not", tweet)
  tweet = re.sub(r"isn't", "is not", tweet)
  tweet = re.sub(r"What's", "What is", tweet)
  tweet = re.sub(r"haven't", "have not", tweet)
  tweet = re.sub(r"hasn't", "has not", tweet)
  tweet = re.sub(r"There's", "There is", tweet)
  tweet = re.sub(r"He's", "He is", tweet)
  tweet = re.sub(r"It's", "It is", tweet)
  tweet = re.sub(r"You're", "You are", tweet)
  tweet = re.sub(r"I'M", "I am", tweet)
  tweet = re.sub(r"Im", "I am", tweet)
  tweet = re.sub(r"shouldn't", "should not", tweet)
  tweet = re.sub(r"wouldn't", "would not", tweet)
  tweet = re.sub(r"i'm", "I am", tweet)
  tweet = re.sub(r"I\x89Ûªm", "I am", tweet)
  tweet = re.sub(r"I'm", "I am", tweet)
  tweet = re.sub(r"Isn't", "is not", tweet)
  tweet = re.sub(r"Here's", "Here is", tweet)
  tweet = re.sub(r"you've", "you have", tweet)
  tweet = re.sub(r"you\x89Ûªve", "you have", tweet)
  tweet = re.sub(r"we're", "we are", tweet)
  tweet = re.sub(r"what's", "what is", tweet)
  tweet = re.sub(r"couldn't", "could not", tweet)
  tweet = re.sub(r"we've", "we have", tweet)
  tweet = re.sub(r"it\x89Ûªs", "it is", tweet)
  tweet = re.sub(r"doesn\x89Ûªt", "does not", tweet)
  tweet = re.sub(r"It\x89Ûªs", "It is", tweet)
  tweet = re.sub(r"Here\x89Ûªs", "Here is", tweet)
  tweet = re.sub(r"who's", "who is", tweet)
  tweet = re.sub(r"I\x89Ûªve", "I have", tweet)
  tweet = re.sub(r"y'all", "you all", tweet)
  tweet = re.sub(r"can\x89Ûªt", "cannot", tweet)
  tweet = re.sub(r"would've", "would have", tweet)
  tweet = re.sub(r"it'll", "it will", tweet)
  tweet = re.sub(r"we'll", "we will", tweet)
  tweet = re.sub(r"wouldn\x89Ûªt", "would not", tweet)
  tweet = re.sub(r"We've", "We have", tweet)
  tweet = re.sub(r"he'll", "he will", tweet)
  tweet = re.sub(r"Y'all", "You all", tweet)
  tweet = re.sub(r"Weren't", "Were not", tweet)
  tweet = re.sub(r"Didn't", "Did not", tweet)
  tweet = re.sub(r"they'll", "they will", tweet)
  tweet = re.sub(r"they'd", "they would", tweet)
  tweet = re.sub(r"DON'T", "DO NOT", tweet)
  tweet = re.sub(r"That\x89Ûªs", "That is", tweet)
  tweet = re.sub(r"they've", "they have", tweet)
  tweet = re.sub(r"i'd", "I would", tweet)
  tweet = re.sub(r"should've", "should have", tweet)
  tweet = re.sub(r"You\x89Ûªre", "You are", tweet)
  tweet = re.sub(r"where's", "where is", tweet)
  tweet = re.sub(r"Don\x89Ûªt", "Do not", tweet)
  tweet = re.sub(r"we'd", "we would", tweet)
  tweet = re.sub(r"i'll", "I will", tweet)
  tweet = re.sub(r"weren't", "were not", tweet)
  tweet = re.sub(r"They're", "They are", tweet)
  tweet = re.sub(r"Can\x89Ûªt", "Cannot", tweet)
  tweet = re.sub(r"you\x89Ûªll", "you will", tweet)
  tweet = re.sub(r"I\x89Ûªd", "I would", tweet)
  tweet = re.sub(r"let's", "let us", tweet)
  tweet = re.sub(r"it's", "it is", tweet)
  tweet = re.sub(r"can't", "can not", tweet)
  tweet = re.sub(r"cant", "can not", tweet)
  tweet = re.sub(r"don't", "do not", tweet)
  tweet = re.sub(r"dont", "do not", tweet)
  tweet = re.sub(r"you're", "you are", tweet)
  tweet = re.sub(r"i've", "I have", tweet)
  tweet = re.sub(r"that's", "that is", tweet)
  tweet = re.sub(r"i'll", "I will", tweet)
  tweet = re.sub(r"doesn't", "does not", tweet)
  tweet = re.sub(r"i'd", "I would", tweet)
  tweet = re.sub(r"didn't", "did not", tweet)
  tweet = re.sub(r"ain't", "am not", tweet)
  tweet = re.sub(r"you'll", "you will", tweet)
  tweet = re.sub(r"I've", "I have", tweet)
  tweet = re.sub(r"Don't", "do not", tweet)
  tweet = re.sub(r"I'll", "I will", tweet)
  tweet = re.sub(r"I'd", "I would", tweet)
  tweet = re.sub(r"Let's", "Let us", tweet)
  tweet = re.sub(r"you'd", "You would", tweet)
  tweet = re.sub(r"It's", "It is", tweet)
  tweet = re.sub(r"Ain't", "am not", tweet)
  tweet = re.sub(r"Haven't", "Have not", tweet)
  tweet = re.sub(r"Could've", "Could have", tweet)
  tweet = re.sub(r"youve", "you have", tweet)  
  tweet = re.sub(r"donå«t", "do not", tweet)

  return tweet

# Remove residual non-alphabetic characters
def remove_nonalpha(s):
    return re.sub('[^A-Za-z]', ' ', s)

# Lower case the string
def lowercase_string(s):
    return s.lower()

# Remove Urls
def remove_urls(s):
    url = re.compile(r'https?://\S+|www\.\S+')
    return url.sub(r'',s)

def preprocess_text(s):
    s = remove_urls(s)
    s = gcleaner(s)
    s = remove_nonalpha(s)
    s = lowercase_string(s)
    
    return s