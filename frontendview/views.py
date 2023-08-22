from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from pprint import pprint
from django import forms
from .models import Guardian, Patient, Question, Answer, Result, Category
from .forms import AccessmentQuestion
from django.urls import reverse
import json
from django.core import serializers
import base64
from .dataset import generateData
from datetime import datetime

# Create your views here.

def index(request):
    template = loader.get_template('pages/home.html')
    return HttpResponse(template.render())

def register(request):
    template = loader.get_template('pages/guardianregform.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('pages/contact.html')
    return HttpResponse(template.render())

def diagnose(request, data, guardianemail, patientoutput):
    # data_to_json = json.dumps(data)

    # jsonobj = "'{}'".format(data)
    # data_to_b64_bytes = data_to_json.encode("ascii")
    # base64_bytes = base64.b64encode(data_to_b64_bytes)
    return render(request, 'pages/diagnose.html', {
        'datas': data,
        'guardianemail': json.dumps(guardianemail),
        'patientoutput': json.dumps(patientoutput),
        })

@csrf_exempt          
def regguardian(request):
    if request.method == 'POST':
        form = request.POST
        guardian = {
                'first_name' : form.get('first_name'),
                'middle_name' : form.get('middle_name'),
                'last_name' : form.get('last_name'),
                'dob' : form.get('dob'),
                'email' : form.get('email'),
                'phone' : form.get('phone'),
                'address' : form.get('address'),
                'city' : form.get('city'),
                'state' : form.get('state'),
                'zip' : form.get('zip'),
                'country' : form.get('country'),
                'rwp' : form.get('rwp'),
            }

        patient = {
                'patient_first_name' : form.get('patient_first_name'),
                'patient_middle_name' : form.get('patient_middle_name'),
                'patient_last_name' : form.get('patient_last_name'),
                'patient_dob' : form.get('patient_dob'),
                'patient_address' : form.get('patient_address'),
                'patient_city' : form.get('patient_city'),
                'patient_state' : form.get('patient_state'),
                'patient_zip' : form.get('patient_zip'),
                'patient_country' : form.get('patient_country'),
            }

        guardianinput = Guardian(
            first_name=guardian["first_name"],
            middle_name=guardian["middle_name"],
            last_name=guardian["last_name"],
            dob=guardian["dob"],
            email=guardian["email"],
            phone=guardian["phone"],
            address=guardian["address"],
            city=guardian["city"],
            state=guardian["state"],
            zip=guardian["zip"],
            country=guardian["country"],
            rwp=guardian["rwp"] )

        patientinput = Patient(
            first_name=patient["patient_first_name"],
            middle_name=patient["patient_middle_name"],
            last_name=patient["patient_last_name"],
            dob=patient["patient_dob"],
            address=patient["patient_address"],
            city=patient["patient_city"],
            state=patient["patient_state"],
            zip=patient["patient_zip"],
            country=patient["patient_country"])

        guardianinput.save()
        patientinput.save()

        guardianemail = guardian["email"]

        if guardianinput and patientinput:
            guardianid_ = Guardian.objects.get(email = form.get('email'))
            guardianid = guardianid_.id
            Patient.objects.update(guardian_id = guardianid)

        patientoutput = {
            "first_name" : patient["patient_first_name"],
            "middle_name" : patient["patient_middle_name"],
            "last_name" : patient["patient_last_name"],
            "dob" : patient["patient_dob"],
            "address" : patient["patient_address"],
            "city" : patient["patient_city"],
            "state" : patient["patient_state"],
            "zip" : patient["patient_zip"],
            "country" : patient["patient_country"],
        }

        # print( vars(guardianemail) )

        patient_dob = patient["patient_dob"]
        
        registerguardian = AccessmentQuestion(patient_dob)
        get_assessment_question = registerguardian.getQuestion()

        kwargs=json.dumps(get_assessment_question)

        url = diagnose(request, kwargs, guardianemail, patientoutput) # redirect('/diagnoses', kwargs)
            
        return url

@csrf_exempt 
def submitAssessment (request):
    if request.method == 'POST':
        form = request.POST
        decode=json.loads(form.get("data"))

        guardianemail=json.loads(form.get("guardianemail"))

        patientdob = json.loads(form.get("patientoutput"))["dob"]

        new_category = AccessmentQuestion(patientdob)

        # return HttpResponse( new_category.getCategory() )

        get_category = new_category.getCategory()

        send_result = []

        # guardian = getGuardian(guardianemail)

        # d = {
        #     "vars": guardian['email'],
        #     }

        # return d

        # isolate fields

        # dict_decode = vars(decode.__dict__)

        answer_main = []

        anr = []

        data_push = []

        for assessment in range(len(decode)):
            # return HttpResponse( assessment['question'] )
            question = decode[assessment]['question']
            answer = decode[assessment]['answer']

            strip_string = str(answer).strip()

            anr.append(strip_string)
            
            # check if question is one of the accepted asd question for that particular patient category

            # return HttpResponse(anr[-1])

            checkquestion = checkQuestion(question)

            if checkquestion is not True:
                raise Exception("Hey! Who the hell are you???")
            else:
                guardian = getGuardian(guardianemail)
                # get_question = Question.objects.get(question = question)

                # questionid = get_question[id]

                guardianid = guardian['id']

                patient = Patient.objects.filter(guardian_id = guardianid).values()

                patientid = []
                patientname = []

                # return HttpResponse( patient )

                for i in patient:
                    # return HttpResponse( i['id'] )
                    patientid.append(i['id'])
                    patient_name = i['first_name'] + " " + i['last_name']
                    patientname.append(patient_name)

                patientid_tuple = tuple(patientid)
                patientname_tuple = tuple(patientname)

                # return HttpResponse({ guardian })

                if guardianemail != "":

                    # check the answers and make the results either 1 or 0 to depict positive or negative. guardian['answer']

                    # template = loader.get_template('pages/result.html')

                    # patientid = []
                    # patientid_tuple = tuple(patientid)

                    # guardianid = guardian['id']
                    # patient_filter = Patient.objects.filter(guardian = guardianid_tuple[-1])
                    
                    # for i in patient_filter:
                    #      patientid.append(i.id)
                    #      category_ = Category.objects.filter(category = category)
                    #      categoryid = []
                    #      for i in category_:
                    #           categoryid.append(i.id)
                    #           patientid_tuple = tuple(patientid)
                    #           categoryid_tuple = tuple(categoryid)
                    
                    # return  HttpResponse(str(anr[-1]))

                    if not str(anr[-1]) == 'agree' and not str(anr[-1]) == 'slightly agree':
                        answer_main.append(0)
                    else:
                        answer_main.append(1)

                    # answer_main_tuple = tuple(answer_main)

                    # return HttpResponse( answer_main[-1] )

                    store_answer = Answer(
                        guardian_id = guardianid,
                        patient_id = patientid_tuple[-1],
                        answer = answer_main[-1]
                    )

                    store_answer.save()

                    if store_answer:
                        create_result = createResult(guardianemail, get_category, patientdob)
                        # return HttpResponse(create_result)
                        if create_result < 1:
                            send_result.append("Negative")
                        else:
                            send_result.append("Positive")
                            
                        data = {
                            "patientname" : patientname_tuple[-1],
                             "result" : send_result[-1],
                             }
                        
                        data_push.append(data)

        # return HttpResponse( answer_main )

        createMlData(guardianemail, get_category, patientdob)

        template = loader.get_template('pages/result.html')
        return HttpResponse(template.render({"res": data_push[-1]}, request))

        # return HttpResponse(anr)
                    
    else:
        template = loader.get_template('pages/result.html')
        return HttpResponse(template.render({"system err": "something went wrong to get guidance"}, request))
    
def createResult (guardianemail, category, patient_dob):
    guardian = Guardian.objects.filter(email = guardianemail)
    
    guardianid = []
    guardianemail = []
    
    for i in guardian:
        guardianid.append(i.id)
        guardianemail.append(i.email)

    patientid = []

    guardianid_tuple = tuple(guardianid)

    patient_filter = Patient.objects.filter(guardian = guardianid_tuple[-1])

    patient_fn = []
    patient_ln = []

    for i in patient_filter:
        patient_fn.append(i.first_name)
        patient_ln.append(i.last_name)
        patientid.append(i.id)

    category_ = Category.objects.filter(category = category)

    categoryid = []

    for i in category_:
        categoryid.append(i.id)

    patientid_tuple = tuple(patientid)
    categoryid_tuple = tuple(categoryid)

    # return HttpResponse(categoryid_tuple)

    answers = Answer.objects.filter(guardian = int(guardianid_tuple[-1]), patient = int(patientid_tuple[-1])).values()

    result = []
    
    negative = []
    positive = []

    now = datetime.now()

    answer_timestamp = now

    index = 0

    arr=[]

    for answer in range(len(answers)):
        index += 1
        # arr.append(answers[answer]['answer'])
        if answers[answer]['answer'] < 1:
            negative.append(answers[answer]['answer'])
        else:
            positive.append(answers[answer]['answer'])

    # return answers

    if not len(negative) > len(positive):
        result.append(1)
    else:
        result.append(0)

    # return result

    save_result = Result(
        asd_status = result[-1],
        guardian_id = guardianid_tuple[-1],
        patient_id = patientid_tuple[-1],
        timestamp = answer_timestamp,
        category_id = categoryid_tuple[-1],
    )

    result_tuple = tuple(result)

    if save_result:
        save_result.save()
        return result_tuple[-1]
    else:
        return False
    
def createMlData(guardianemail, category, patient_dob):
    guardian = Guardian.objects.filter(email = guardianemail)
    
    guardianid = []
    guardianemail = []
    
    for i in guardian:
        guardianid.append(i.id)
        guardianemail.append(i.email)

    patientid = []

    guardianid_tuple = tuple(guardianid)

    patient_filter = Patient.objects.filter(guardian = guardianid_tuple[-1])

    patient_fn = []
    patient_ln = []

    for i in patient_filter:
        patient_fn.append(i.first_name)
        patient_ln.append(i.last_name)
        patientid.append(i.id)

    category_ = Category.objects.filter(category = category)

    categoryid = []

    for i in category_:
        categoryid.append(i.id)

    patientid_tuple = tuple(patientid)
    categoryid_tuple = tuple(categoryid)

    # return HttpResponse(categoryid_tuple)

    answers = Answer.objects.filter(guardian = int(guardianid_tuple[-1]), patient = int(patientid_tuple[-1])).values()

    result = []
    
    negative = []
    positive = []

    now = datetime.now()

    answer_timestamp = now

    index = 0

    for answer in range(len(answers)):
        index += 1
        # arr.append(answers[answer]['answer'])
        if answers[answer]['answer'] < 1:
            negative.append(answers[answer]['answer'])
        else:
            positive.append(answers[answer]['answer'])

    # return str(arr)

    if not len(negative) > len(positive):
        result.append(1)
    else:
        result.append(0)

    negative_length = len(negative)
    positive_length = len(positive)

    result_tuple = tuple(result)

    # create new dict result to pass to ml model
    ml_result = {
        "guardianid": guardianid_tuple[-1],
        "patientid": int(patientid_tuple[-1]),
        "guardianemail": guardianemail[-1],
        "patient_fname": patient_fn[-1],
        "patient_lname": patient_ln[-1],
        "category": category,
        "categoryid": categoryid[-1],
        "negative_length": negative_length,
        "positive_length": positive_length,
        "answer_timestamp": answer_timestamp,
    }
    
    generateData(ml_result)
    
def checkQuestion(question):
    # compare request question with db question field
    return True
    if question != None:
        c_question = Question.objects.get(question = question)
        if c_question.exists():
            return True
        else:
            return False
        
def getGuardian(guardianemail):
        if guardianemail != None:
            email = Guardian.objects.filter(email = guardianemail)
            # return HttpResponse(email)
            if not email:
                raise Exception("Hey! Who the hell are you???")
            else:
                for i in email:
                    guardian = {
                    "id": i.id,
                    "first_name": i.first_name,
                    "last_name": i.last_name,
                    "email": i.email,
                }
                    return guardian