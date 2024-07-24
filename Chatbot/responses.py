import random

# Dictionary to store responses for symptoms and corresponding conditions
symptom_responses = {
    "fever": [
        "Fever is a common symptom of various illnesses and infections.",
        "It is typically a sign that the body is fighting off an infection.",
        "Rest, hydration, and fever-reducing medication can help manage fever."
    ],
    "headache": [
        "Headaches can have various causes, including stress, dehydration, or underlying health conditions.",
        "Taking a break, staying hydrated, and managing stress can sometimes alleviate headaches.",
        "Persistent or severe headaches may require consultation with a healthcare professional."
    ],
    "cough": [
        "A cough can be caused by respiratory infections, allergies, or irritants.",
        "Stay hydrated, use a humidifier, and consider over-the-counter cough remedies.",
        "If a cough persists for more than a week or is severe, consult with a healthcare professional."
    ],
    "nausea": [
        "Nausea can be triggered by various factors, including infections, medications, or motion sickness.",
        "Sipping on ginger tea, nibbling on crackers, or avoiding strong odors may help alleviate nausea.",
        "Persistent or severe nausea should be discussed with a healthcare professional."
    ],
    "fatigue": [
        "Fatigue can result from lack of sleep, stress, or underlying health conditions.",
        "Ensure an adequate amount of sleep, manage stress, and maintain a balanced diet for improved energy levels.",
        "If fatigue persists, consider consulting a healthcare professional for evaluation."
    ],
    "shortness_of_breath": [
        "Shortness of breath can be caused by respiratory issues, heart problems, or anxiety.",
        "If experiencing sudden or severe shortness of breath, seek immediate medical attention.",
        "Chronic shortness of breath should be evaluated by a healthcare professional."
    ],
    "muscle_pain": [
        "Muscle pain can be due to overexertion, injuries, or underlying health conditions.",
        "Rest, gentle stretching, and over-the-counter pain relievers may help alleviate muscle pain.",
        "Persistent or severe muscle pain may require medical evaluation."
    ],
    "sore_throat": [
        "A sore throat can be caused by viral or bacterial infections, allergies, or irritants.",
        "Stay hydrated, gargle with salt water, and consider throat lozenges for relief.",
        "If a sore throat persists or is accompanied by other symptoms, consult with a healthcare professional."
    ],
    "abdominal_pain": [
        "Abdominal pain can have various causes, including digestive issues, infections, or inflammation.",
        "Mild abdominal pain may be relieved with rest and a bland diet.",
        "Persistent or severe abdominal pain requires evaluation by a healthcare professional."
    ],
    "joint_pain": [
        "Joint pain can be due to arthritis, injuries, or inflammatory conditions.",
        "Applying ice or heat, gentle exercises, and over-the-counter pain relievers may help manage joint pain.",
        "Chronic or worsening joint pain should be discussed with a healthcare professional."
    ],
    "dizziness": [
        "Dizziness can result from various factors, including low blood sugar, dehydration, or inner ear issues.",
        "Stay hydrated, avoid sudden movements, and rest if experiencing dizziness.",
        "Persistent or recurrent dizziness should be evaluated by a healthcare professional."
    ],
    "vomiting": [
        "Vomiting can be caused by infections, food poisoning, or underlying health conditions.",
        "Stay hydrated with small sips of clear fluids and gradually reintroduce bland foods.",
        "If vomiting persists or is severe, consult with a healthcare professional."
    ],
    "diarrhea": [
        "Diarrhea can be due to infections, certain foods, or gastrointestinal disorders.",
        "Stay hydrated with electrolyte drinks and follow a bland diet until symptoms improve.",
        "Persistent or severe diarrhea should be discussed with a healthcare professional."
    ],
    "chest_pain": [
        "Chest pain can have various causes, including heart issues, respiratory problems, or muscle strain.",
        "Seek immediate medical attention if experiencing severe or sudden chest pain.",
        "Any unexplained or persistent chest pain should be evaluated by a healthcare professional."
    ],
    "skin_rash": [
        "A skin rash can result from allergies, infections, or underlying skin conditions.",
        "Keep the affected area clean, avoid scratching, and use over-the-counter creams for relief.",
        "If the rash persists or worsens, consult with a dermatologist."
    ],
    "vision_changes": [
        "Vision changes can be a sign of eye strain, refractive errors, or underlying eye conditions.",
        "Take breaks when using screens, ensure proper lighting, and schedule regular eye exams.",
        "Sudden or severe vision changes require prompt evaluation by an eye care professional."
    ],
    "weight_loss": [
        "Unexplained weight loss can be a symptom of various health issues, including metabolic disorders or infections.",
        "Maintain a balanced diet and discuss significant weight loss with a healthcare professional.",
        "Rapid or unintentional weight loss may indicate an underlying health problem."
    ],
    "difficulty_swallowing": [
        "Difficulty swallowing can be due to throat infections, gastroesophageal reflux disease (GERD), or structural issues.",
        "Stay hydrated, avoid large bites, and try softer foods if experiencing difficulty swallowing.",
        "Persistent difficulty swallowing should be evaluated by a healthcare professional."
    ],
    "excessive_thirst": [
        "Excessive thirst can be caused by dehydration, diabetes, or certain medications.",
        "Ensure an adequate intake of water and consult with a healthcare professional if excessive thirst persists.",
        "Unexplained or persistent excessive thirst may require medical investigation."
    ],
    "hair_loss": [
        "Hair loss can result from genetics, hormonal changes, or underlying health conditions.",
        "Maintain a healthy diet, avoid excessive heat or chemical treatments, and discuss hair loss concerns with a dermatologist.",
        "Sudden or significant hair loss may require medical evaluation."
    ],
   
   
}

# Dictionary to store responses for different healthcare topics
responses = {
    "covid-19": [
        "COVID-19 is caused by the SARS-CoV-2 virus.",
        "Common COVID-19 symptoms include fever, cough, and shortness of breath.",
        "Vaccination is a key tool in controlling the spread of COVID-19.",
        "To prevent COVID-19, wear masks, practice social distancing, and maintain good hand hygiene.",
    ],
     "influenza": [
        "Influenza, or flu, is a contagious respiratory illness caused by influenza viruses.",
        "Flu symptoms include fever, muscle aches, and sore throat.",
        "Annual flu vaccination is recommended to reduce the risk of infection.",
    ],
    "diabetes": [
        "Diabetes is a chronic condition that affects how your body processes glucose (sugar).",
        "There are two main types of diabetes: Type 1 and Type 2.",
        "Managing diabetes involves monitoring blood sugar levels and lifestyle changes.",
    ],
    "cancer": [
        "Cancer is a group of diseases characterized by the uncontrolled growth of abnormal cells.",
        "Common types of cancer include breast cancer, lung cancer, and prostate cancer.",
        "Early detection and treatment are crucial for improving cancer outcomes.",
    ],
    "dengue fever": [
        "Dengue fever is a mosquito-borne viral illness.",
        "Symptoms of dengue fever include high fever, severe headache, and joint pain.",
        "Preventing mosquito bites and eliminating mosquito breeding sites can help prevent dengue fever.",
    ],
    "heart disease": [
        "Heart disease refers to a range of conditions that affect the heart's structure and function.",
        "Common types of heart disease include coronary artery disease and heart failure.",
        "Maintaining a healthy lifestyle with a balanced diet and regular exercise can reduce the risk of heart disease.",
    ],
    "stroke": [
        "A stroke occurs when there is a sudden interruption of blood flow to the brain.",
        "Common signs of a stroke include sudden numbness, confusion, and difficulty speaking.",
        "Immediate medical attention is essential to minimize stroke damage.",
    ],
    "asthma": [
        "Asthma is a chronic respiratory condition that can cause difficulty breathing and wheezing.",
        "Asthma triggers may include allergens and respiratory infections.",
        "Asthma can be managed with medications and avoiding triggers.",
    ],
    "Alzheimer's disease": [
        "Alzheimer's disease is a progressive neurodegenerative disorder that affects memory and cognitive function.",
        "Early diagnosis and treatment can help slow the progression of Alzheimer's disease.",
        "Supportive care is essential for individuals with Alzheimer's disease.",
    ],
    "hypertension": [
        "Hypertension, or high blood pressure, is a common cardiovascular condition.",
        "Untreated hypertension can lead to serious health problems, including heart disease and stroke.",
        "Lifestyle changes and medications can help manage hypertension.",
    ],
    "arthritis": [
        "Arthritis is a term for joint inflammation and stiffness.",
        "Common types of arthritis include osteoarthritis and rheumatoid arthritis.",
        "Exercise, physical therapy, and medications can help manage arthritis symptoms.",
    ],
    "pneumonia": [
        "Pneumonia is an infection that inflames the air sacs in one or both lungs.",
        "Common symptoms of pneumonia include cough, fever, and difficulty breathing.",
        "Prompt treatment with antibiotics is essential for bacterial pneumonia.",
    ],
    "osteoporosis": [
        "Osteoporosis is a condition that weakens bones and makes them more likely to break.",
        "Risk factors for osteoporosis include age, gender, and family history.",
        "Calcium, vitamin D, and lifestyle changes can help prevent and manage osteoporosis.",
    ],
    "migraine": [
        "Migraine is a type of headache characterized by severe pain, nausea, and sensitivity to light and sound.",
        "Identifying triggers, managing stress, and medications are common approaches to migraine management.",
        "If migraines are severe or frequent, consultation with a healthcare professional is recommended.",
    ],
    "chronic obstructive pulmonary disease (COPD)": [
        "COPD is a chronic lung disease that makes it difficult to breathe.",
        "Smoking is a common cause of COPD, and quitting smoking is a key part of management.",
        "Medications and pulmonary rehabilitation can help improve COPD symptoms.",
    ],
    "gastroesophageal reflux disease (GERD)": [
        "GERD is a digestive disorder that affects the lower esophageal sphincter, causing acid reflux.",
        "Lifestyle changes, such as dietary modifications and elevating the head during sleep, can alleviate GERD symptoms.",
        "If GERD symptoms persist, medical intervention may be necessary.",
    ],
    "rheumatoid arthritis": [
        "Rheumatoid arthritis is an autoimmune disorder that causes joint inflammation and pain.",
        "Early diagnosis and treatment are crucial to prevent joint damage in rheumatoid arthritis.",
        "Medications and lifestyle changes are common components of rheumatoid arthritis management.",
    ],
    "kidney disease": [
        "Kidney disease refers to a gradual loss of kidney function over time.",
        "Common causes of kidney disease include diabetes and high blood pressure.",
        "Managing underlying conditions and lifestyle changes can help slow the progression of kidney disease.",
    ],
    "anxiety disorders": [
        "Anxiety disorders are a group of mental health conditions characterized by excessive worry and fear.",
        "Treatment for anxiety disorders may include therapy, medications, and lifestyle changes.",
        "Seeking support from mental health professionals is important for managing anxiety disorders.",
    ],
    "liver disease": [
        "Liver disease encompasses a range of conditions that affect the liver's structure and function.",
        "Common liver diseases include hepatitis, cirrhosis, and fatty liver disease.",
        "Early diagnosis and lifestyle changes can play a crucial role in managing liver disease.",
    ],
    # ... (other diseases and healthcare topics)
}

# Dictionary to store responses for general health advice
health_tips_responses = {
    "stay_hydrated": [
        "Stay hydrated by drinking enough water every day.",
    ],
    "balanced_diet": [
        "A balanced diet with fruits and vegetables is essential for your health.",
    ],
    "exercise_regularly": [
        "Exercise regularly to keep your body and mind in good shape.",
    ],
    "adequate_sleep": [
        "Adequate sleep is crucial for overall well-being. Aim for 7-9 hours.",
    ],
    "wash_hands_frequently": [
        "Wash your hands frequently to prevent the spread of infections.",
    ],
    "manage_stress": [
        "Manage stress through relaxation techniques like deep breathing.",
    ],
    "limit_processed_foods": [
        "Limit processed foods and focus on whole, nutrient-rich options.",
    ],
    "protect_skin_from_sun": [
        "Protect your skin from the sun by using sunscreen and wearing hats.",
    ],
    "regular_checkups": [
        "Regular check-ups help catch potential health issues early.",
    ],
    "quit_smoking": [
        "Quit smoking for better health.",
    ],
    "limit_alcohol_intake": [
        "Limit alcohol intake for better health.",
    ],
}

def get_response(user_input):
    user_input = user_input.lower()

    # Check if the user input matches any symptom
    if user_input in symptom_responses:
        response_list = symptom_responses[user_input]
        return random.choice(response_list)
    # Check if the user input matches any disease or healthcare topic
    elif user_input in responses:
        response_list = responses[user_input]
        return random.choice(response_list)
    # Check if the user input matches any health tip
    elif user_input in health_tips_responses:
        response_list = health_tips_responses[user_input]
        return random.choice(response_list)
    else:
        return "I'm sorry, I don't have information on that topic. Please ask another question."
