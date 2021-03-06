from flask import Flask, render_template, request
import random
import time

app = Flask(__name__)


greetings = ['Hola!','Hey!','Hey, welcome!','Hello','Hi, how may I help you?','Hi, how are you?','Hey, how are you doing today?',"Yeah, what's up",'Hey','Hello','Hi']

questions = ['How are you?', 'How are you','How are you doing?']
responses = ['Perfect!', 'I feel good', 'I am fine']

verifications = ['Are you sure?', 'You sure?', 'Sure?']
validations = ['Lol, why not?', 'Yeah', 'Definitely','No!', 'Nah, I just guessed']

headache = ['Headache','Migraine']

stomach = ['Stomach ache','Stomach pain','Abdominal pain']

pregnant = ['Pregnant','Pregnancy','Miscarriage']

body = ['Body pain','Body pains','Body ache','Knee pain','Back pain','Waist pain','Muscle ache']

joint = ['Joint pain']

malaria = ['Malaria','Malaria and typhoid']

pain = ['Pain','Pains','Aches'] #what kind of pain?

typhoid = ['Typhoid','Typhoid and malaria','Typhoid fever']

cough = ['Cough','I am coughing']

fever = ['Fever','Cold','Catarrh']

dia = ['Diarrhea','Acute diarrhea'] 

infect = ['Infection'] #what kind of infection?

infection = ['Yeast infection','Vaginal','Yeast','Vaginal infection','Bacterial','Mouth infection','Urinary       tract infection','Kidney infection','Penis infection','Gonorhea','Syphilis','Staphylococcus'] #check spelling

incurable = ['Aids','Ebola','Bird flue']

cholera = ['Cholera']

hiv = ['Hiv', 'Hiv and Aids']

lol = ['Lols','Lol','Lolz','Haha']

you = ['You', 'You!']

cancer = ['Cancer','Breast cancer','Lungs cancer','Prostate cancer','Skin cancer','Leukemia','Malignancy']

hbp = ['Hbp','HPB','Hypertension','High blood pressure']

thanks = ['Thanks','Thank you','I appreciate',"I'm grateful"]


@app.route('/')
def home():
   return render_template("home.html")

@app.route('/doctorbot')
def doctorbot():
   return render_template('doctorbot.html')    


@app.route("/get")
def get_bot_response():
   userText = request.args.get('msg')
   userInput = userText.capitalize()

   while True:

      if userInput in greetings:
         random_greeting = random.choice(greetings)
         time.sleep(.3)
         return random_greeting

      elif userInput in questions:
         random_response = random.choice(responses)
         time.sleep(.3)
         return random_response
            
      elif userInput in verifications:
         random_response = random.choice(validations)
         time.sleep(.3)
         return random_response

      elif userInput in ['Sure','Fine','Not fine','I am fine',"I'm not fine",'Not well','I am not well','I      am not feeling fine','Not feeling fine','I am okay','Okay','Not okay','Alright','Cool','Dope','Great','Awesome','Splendid','Beautiful']:
         response = "Alright, kindly give me a keyword of any medical condition you want to know about"
         time.sleep(.3)
         return response

      elif userInput in headache:
         time.sleep(.3)
         return "I've got some good info about migraines and headaches, please go <a style='color:red' target='_blank' href='https://www.mayoclinic.org/diseases-conditions/chronic-daily-headaches/in-depth/headaches/art-20047375'>here</a>"

      elif userInput in stomach:
         time.sleep(.3)
         return "You're in luck! Check <a style='color:red' target='_blank' href='https://www.webmd.com/first-aid/abdominal-pain-in-adults-treatment'>this</a> out for abdominal pains."

      elif userInput in pregnant:
         time.sleep(.3)
         return "Wow! Congratulations on your pregnancy.. <a style='color:blue' target='_blank' href='https://www.healthline.com/health/pregnancy'>Here</a> is all you need to know about preganancy"

      elif userInput in body:
         time.sleep(.3)
         return "It must have been hard for you, <a style='color:red' target='_blank' href='https://www.healthline.com/health/body-aches#cold-or-flu'>this</a> should help"

      elif userInput in joint:
         time.sleep(.3)
         return "You're in luck! Go <a style='color:red' target='_blank' href='https://www.msdmanuals.com/home/bone,-joint,-and-muscle-disorders/symptoms-of-musculoskeletal-disorders/joint-pain-many-joints'>here</a> for all kinds of joint pains"

      elif userInput in malaria:
         time.sleep(.3)
         return "That malaria must go! Kindly visit <a style='color:red' target='_blank' href='https://www.mayoclinic.org/diseases-conditions/malaria/diagnosis-treatment/drc-20351190'>this</a> resource immediately"

      elif userInput in pain:
         time.sleep(.3)
         return "I'm so sorry about that.. What kind of pain are going through?"

      elif userInput in thanks:
         time.sleep(.3)
         return "You welcome, Always!"  

      elif userInput in typhoid:
         time.sleep(.3)
         return "Typhoid? You are in the right place! kindly go <a style='color:blue' target='_blank' href='https://www.mayoclinic.org/diseases-conditions/typhoid-fever/diagnosis-treatment/drc-20378665'>here</a> for more information"

      elif userInput in infect:
         time.sleep(.3)
         return "What kind of infection are you interested in?" 

      elif userInput in cough:
         time.sleep(.3)
         return "You're in luck! I've got some good info about cough for you. Check <a style='color:red' target='_blank' href='https://www.nhsinform.scot/illnesses-and-conditions/lungs-and-airways/cough'>here</a> " 


      elif userInput in fever:
         time.sleep(.3)
         return "Fever can be frustrating! Visit <a style='color:red' target='_blank' href='https://www.medicalnewstoday.com/articles/168266.php'>this</a> resource for everything about fever and cold" 

      elif userInput in dia:
         time.sleep(.3)
         return "You're very lucky! I have something for you.. Check <a style='color:green' target='_blank' href='https://www.mayoclinic.org/diseases-conditions/diarrhea/diagnosis-treatment/drc-20352246'>this</a> out for diarrhea treatments" 

      elif userInput in infection:
         time.sleep(.3)
         return "Lucky you! I just searched the whole internet for you.. <a style='color:red' target='_blank' href='https://www.healthline.com/health/infections'>See</a> what I found about infections."
      elif userInput in incurable:
         time.sleep(.3)
         return "I thought it doesn't have a cure.. Lol! Have you manufactured one?" 

      elif userInput in cholera:
         time.sleep(.3)
         return "Cholera is a bad one! Don't hesistate to see a doctor. Before then, <a style='color:red' target='_blank' href='https://www.medicalnewstoday.com/articles/189269.php'>see</a> what I pulled out for you!"
#
      elif userInput in cancer:
         time.sleep(.3)
         return "Today is a good day. I can assure you that! I found a resource that can help you with cancer, Kingly go <a style='color:blue' target='_blank' href='https://www.medicinenet.com/cancer/article.htm'>here</a> Good luck!"

      elif userInput in hbp:
         time.sleep(.3)
         return "Today is a good day. I can assure you that! I found a resource that can help you with Hypertension, Kingly go <a style='color:blue' target='_blank' href='https://www.healthline.com/health/high-blood-pressure-hypertension#home-remedies-for-hypertension'>here</a> Good luck!"
#
      elif userInput in lol:
         time.sleep(.3)
         return "Hey! What's funny?"

      elif userInput in you:
         time.sleep(.3)
         return "Right? I think I'm in a good mood today!"

      elif userInput in hiv:
         time.sleep(.3)
         return "Hey! You're really lucky to know me.. Guess what? I've got something for you <a style='color:red' target='_blank' href='https://www.healthline.com/health/hiv-aids'>here</a>"

      else:
         advice = random.choice([" I'm sorry, I don't understand you. Use words like: 'joint pain', 'vaginal infection', 'bird flu', 'hypertension', 'cholera', 'syphilis', and more..",
         "Please use a keyword or a short phrase like: 'Hello', 'Hi', 'Hey!', 'Hola!'",
         "Ooops! Was that Latin?",
         "No! That's not right, try this: 'sure?', 'alright', 'cool', etc. As well as: 'how are you?', 'how are you doing?'",
         "I wasn't expecting that, please type a keyword of the medical condition you want to know about","Come on. I'm just a Bot! Use a keyword please",
         "kindly use keywords like: 'stomach ache', 'pregnancy', 'headache', 'typhoid', 'malaria', 'hiv', or 'ebola'. Thank you."])
         time.sleep(.3)
         return advice
           

if __name__ == "__main__":
   app.run(debug=True)
