import sys
import os
from .models import Guardian, Patient, Question, Answer, Result, Category

from django.http import HttpRequest

currentguardian = os.getlogin()

helper = "/home/" + currentguardian + "/projects/kale/asd/asddiagnoses/helper"

sys.path.insert(1, helper)

from helper import helper

class AccessmentQuestion:
    def __init__(self, dob):
        self.dob = dob
        self.category =  {
            "infant": 1,
            "toddlers": 3,
            "preschool": 5,
            "gradeschooler": 12
        }
        self.categoryerror = {
            "error": "Ooops! You\'re not qualified for this assessment"
        }

    def infant(self):
        questions = [
            {
                'sn': 1,
                'question': 'He&#8260;she gives attentions to eye contact deliberately',
                'options': {
                    'a': 'slightly disagree',
                    'b': 'disagree',
                    'c': 'slightly agree',
                    'd': 'agree'
                },
                'answer': None
            },
             {
                'sn': 2,
                'question': 'He&#8260;she can respond to his&#8260;her name',
                'options': {
                    'a': 'slightly disagree',
                    'b': 'disagree',
                    'c': 'slightly agree',
                    'd': 'agree'
                },
                'answer': None
            },
             {
                'sn': 3,
                'question': 'He&#8260;she can copy or respond to the sound made around him',
                'options': {
                    'a': 'slightly disagree',
                    'b': 'disagree',
                    'c': 'slightly agree',
                    'd': 'agree'
                },
                'answer': None
            },
             {
                'sn': 4,
                'question': 'He&#8260;she can copy the gesture of other people',
                'options': {
                    'a': 'slightly disagree',
                    'b': 'disagree',
                    'c': 'slightly agree',
                    'd': 'agree'
                },
                'answer': None
            },
             {
                'sn': 5,
                'question': 'He&#8260;she can copy and respond to facial expression',
                'options': {
                    'a': 'slightly disagree',
                    'b': 'disagree',
                    'c': 'slightly agree',
                    'd': 'agree'
                },
                'answer': None
            },
             {
                'sn': 6,
                'question': 'He&#8260;she can watch things as they move',
                'options': {
                    'a': 'slightly disagree',
                    'b': 'disagree',
                    'c': 'slightly agree',
                    'd': 'agree'
                },
                'answer': None
            },
             {
                'sn': 7,
                'question': 'He&#8260;she can smile at others when funny things happen around them',
                'options': {
                    'a': 'slightly disagree',
                    'b': 'disagree',
                    'c': 'slightly agree',
                    'd': 'agree'
                },
                'answer': None
            },
             {
                'sn': 8,
                'question': 'He&#8260;she can bring his&#8260;her hands to his&#8260;her mouth',
                'options': {
                    'a': 'slightly disagree',
                    'b': 'disagree',
                    'c': 'slightly agree',
                    'd': 'agree'
                },
                'answer': None
            },
             {
                'sn': 9,
                'question': 'He&#8260;she can hold his&#8260;her head up when lying down on their tummy and pushing up.',
                'options': {
                    'a': 'slightly disagree',
                    'b': 'disagree',
                    'c': 'slightly agree',
                    'd': 'agree'
                },
                'answer': None
            },
             {
                'sn': 10,
                'question': 'He&#8260;she can bring objects to his&#8260;her mouth',
                'options': {
                    'a': 'slightly disagree',
                    'b': 'disagree',
                    'c': 'slightly agree',
                    'd': 'agree'
                },
                'answer': None
            },
             {
                'sn': 11,
                'question': 'He&#8260;she can move both eyes in every dimensions',
                'options': {
                    'a': 'slightly disagree',
                    'b': 'disagree',
                    'c': 'slightly agree',
                    'd': 'agree'
                },
                'answer': None
            },
             {
                'sn': 12,
                'question': 'He&#8260;she can display affection for their parents or caregivers',
                'options': {
                    'a': 'slightly disagree',
                    'b': 'disagree',
                    'c': 'slightly agree',
                    'd': 'agree'
                },
                'answer': None
            },
             {
                'sn': 13,
                'question': 'He&#8260;she can look to where a person is pointing',
                'options': {
                    'a': 'slightly disagree',
                    'b': 'disagree',
                    'c': 'slightly agree',
                    'd': 'agree'
                },
                'answer': None
            },
             {
                'sn': 14,
                'question': 'He&#8260;she can recognize people',
                'options': {
                    'a': 'slightly disagree',
                    'b': 'disagree',
                    'c': 'slightly agree',
                    'd': 'agree'
                },
                'answer': None
            }
            ]
        return questions
    
    def toddler(self):
        questions = [
             {
                'sn': 1,
                'question': 'He&#8260;she can point to show things to others',
                'options': {
                    'a': 'slightly disagree',
                    'b': 'disagree',
                    'c': 'slightly agree',
                    'd': 'agree'
                },
                'answer': None
            },
             {
                'sn': 2,
                'question': 'He&#8260;she can recognize familiar objects',
                'options': {
                    'a': 'slightly disagree',
                    'b': 'disagree',
                    'c': 'slightly agree',
                    'd': 'agree'
                },
                'answer': None
            },
             {
                'sn': 3,
                'question': 'He&#8260;she can imitate others',
                'options': {
                    'a': 'slightly disagree',
                    'b': 'disagree',
                    'c': 'slightly agree',
                    'd': 'agree'
                },
                'answer': None
            },
             {
                'sn': 4,
                'question': 'He&#8260;she can use at least 6 words',
                'options': {
                    'a': 'slightly disagree',
                    'b': 'disagree',
                    'c': 'slightly agree',
                    'd': 'agree'
                },
                'answer': None
            },
             {
                'sn': 5,
                'question': 'He&#8260;she can learn new words',
                'options': {
                    'a': 'slightly disagree',
                    'b': 'disagree',
                    'c': 'slightly agree',
                    'd': 'agree'
                },
                'answer': None
            },
             {
                'sn': 6,
                'question': 'He&#8260;she can react when a parent or caregiver leaves or comes back',
                'options': {
                    'a': 'slightly disagree',
                    'b': 'disagree',
                    'c': 'slightly agree',
                    'd': 'agree'
                },
                'answer': None
            }
        ]
        return questions
    
    def getQuestion (self):
        patient_age = helper.getCurrentAgeOfGuardian(self.dob)
        infant = self.infant()
        toddler = self.toddler()

        if patient_age <= self.category["infant"]:
            return tuple((infant))
        elif patient_age > self.category["infant"] & patient_age <= self.category["toddler"]:
            return tuple((toddler))
        else:
            return self.categoryerror
        
    def getCategory (self):
        patient_age = helper.getCurrentAgeOfGuardian(self.dob)
        categories = Category.objects.all()

        if patient_age <= self.category["infant"]:
            for i in categories:
                return i.category
        elif patient_age > self.category["infant"] & patient_age <= self.category["toddler"]:
            for i in categories:
                return i.category[1]
        else:
            return self.categoryerror
