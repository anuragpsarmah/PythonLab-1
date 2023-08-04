#WORD COUNT PROGRAM

para = "I am Anurag Parashar Sarmah. My reg. no. is 2347213. I am a 1st year student at Christ University pursuing MCA. My domain is Personal Health and Fitness Tracking System. I selected this domain to be able to manage fitness related data. The various attributes in my domain are User Profile, health metrics, exercise log, nutrition log, fitness goal, workout routine, acticity tracker, meal plan, health assesment, wellness dashboard. I believe personal fitness is very important."
para = para.split()

count = 0
for x in para:
    if x == "fitness": count += 1

print("Word Count for 'Fitness'= ", count)
