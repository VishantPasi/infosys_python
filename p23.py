def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    count = 0 
    li = []
    for i in patient_medical_speciality_list:
        if str(i).isdigit():
            continue
        else:
            li.append(i)
    

    for j in li:
            count = max(li,key=li.count)
    

    for key in medical_speciality:
        if count == key:
            re = medical_speciality[key]
    
    return re
       

    

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E',"E","E"]
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)