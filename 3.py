#CHARACTER COUNT

para = "I am Anurag Parashar Sarmah. My reg. no. is 2347213. I am a 1st year student at Christ University pursuing MCA. My domain is 'Personal Health and Fitness Tracking System'. I selected this domain to be able to manage fitness related data. The various attributes in my domain are User Profile, health metrics, exercise log, nutrition log, fitness goal, workout routine, activity tracker, meal plan, health assessment, wellness dashboard. I believe personal fitness is very important."

char_count = {'Integers': 0, 'Alphabets': 0, 'Special Characters': 0}

for x in para:
    if x.isalpha():
        char_count['Alphabets'] += 1
    elif x.isdigit():
        char_count['Integers'] += 1
    elif not x.isspace():
        char_count['Special Characters'] += 1

for x in char_count:
    print("Number of", x, "=", char_count[x])