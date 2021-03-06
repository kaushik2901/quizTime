from django.http import *
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .settings import *
from django.core.exceptions import ObjectDoesNotExist
import json
import random


# home page
def Index(request):
    if 'quizTimeId' in request.COOKIES:
        return redirect("./questions")
    return render(request, 'quizMania/index.html', {})

#questions page
def Question(request):
    if 'quizTimeId' not in request.COOKIES:
        return redirect("../")
    quizTimeId = request.COOKIES['quizTimeId']

    try:
        user = Users.objects.get(id=int(quizTimeId))
    except ObjectDoesNotExist as e:
        return HttpResponse("User not found : try clearing COOKIES")
    except Exception as e:
        return HttpResponse("Unknown Exception occurred")

    try:
        userStatus = UserStatus.objects.get(user=user)
    except ObjectDoesNotExist as e:
        return HttpResponse("User Staus not found : try clearing COOKIES")
    except Exception as e:
        return HttpResponse("Unknown Exception occurred")

    if userStatus.ruleDisplay == True:
        con = {
            "user" : user,
            "userStatus" : userStatus,
            "rules" : Rules.objects.all()
        }
    else :
        con = {
            "user" : user,
            "userStatus" : userStatus,
            "ruleDisplay" : userStatus.ruleDisplay,
        }

    return render(request, 'quizMania/questions.html', con)


#do not  display rules api
def HideRules(request):
    if request.method == "POST":
        if "hideRules" in request.POST:
            hideRules = request.POST['hideRules']
            try:
                user = Users.objects.get(id=int(hideRules))
            except ObjectDoesNotExist as e:
                return HttpResponse("User not found : try clearing COOKIES")
            except Exception as e:
                return HttpResponse("Unknown Exception occurred")

            try:
                userStatus = UserStatus.objects.get(user=user)
            except ObjectDoesNotExist as e:
                return HttpResponse("User Staus not found : try clearing COOKIES")
            except Exception as e:
                return HttpResponse("Unknown Exception occurred")

            userStatus.ruleDisplay = False
            userStatus.save()

            return HttpResponse("done")

    return HttpResponse("Invalid request")


#next question api
def requestQuestion(request):
    if request.method == 'POST':
        if 'userStatus' in request.POST:
            try:
                ut = int(request.POST['userStatus'])
                userStatus = UserStatus.objects.get(id=ut)
            except ObjectDoesNotExist as e:
                return HttpResponse("User Staus not found : try clearing COOKIES")
            except Exception as e:
                return HttpResponse(e)

            allQuestions = Questions.objects.all();
            totalQuestions = len(allQuestions)

            answeredQ = userStatus.answeredQuestions
            QuestionNo = 0
            if answeredQ is None or answeredQ == '':
                nextQuestion = random.choice(allQuestions)
                userStatus.answeredQuestions = str(nextQuestion.id)
                QuestionNo = 1
            else:
                qArry = answeredQ.split(',')
                qArry = [ int(i) for i in qArry ]

                if len(qArry) == totalQuestions:
                    return HttpResponse("completed")

                nextQuestion = random.choice(allQuestions)
                while nextQuestion.id in qArry:
                    nextQuestion = random.choice(allQuestions)
                userStatus.answeredQuestions += ',' + str(nextQuestion.id)
                QuestionNo = len(qArry) + 1

            if nextQuestion.questionImage is None:
                imageURL = ''
            else :
                imageURL = "/media/" + str(nextQuestion.questionImage)

            con = {
                "totalQuestions": totalQuestions,
                "QuestionNo": QuestionNo,
                "question" : {
                    "questionString": nextQuestion.questionString,
                    "questionType": nextQuestion.questionType,
                    "questionImage": imageURL,
                    "option1": nextQuestion.option1,
                    "option2": nextQuestion.option2,
                    "option3": nextQuestion.option3,
                    "option4": nextQuestion.option4,
                    "answer": nextQuestion.answer,
                    "points": nextQuestion.points
                }
            }
            userStatus.save()
            return JsonResponse(con)
    return HttpResponse("Invalid request")

def ValidateAnswer(request):
    if request.method == "POST":
        if 'userStatus' in request.POST and 'updatePoints' in request.POST:
            try:
                ut = int(request.POST['userStatus'])
                userStatus = UserStatus.objects.get(id=ut)
            except ObjectDoesNotExist as e:
                return HttpResponse("User Staus not found : try clearing COOKIES")
            except Exception as e:
                return HttpResponse(e)

            updatePoints = int(request.POST['updatePoints'])
            userStatus.points += updatePoints
            userStatus.save()

    return HttpResponse("Invalid request")

#login api
def login(request):
    if request.method == "POST":
        if "rollNumber" in request.POST and "key" in request.POST:
            rollNumber = request.POST['rollNumber']
            key = request.POST['key']

            try:
                user = Users.objects.get(rollNumber=rollNumber, key=key)
            except ObjectDoesNotExist as e:
                return HttpResponse("Invalid roll number or key")
            except Exception as e:
                return HttpResponse("Unknown Exception occurred")

            try:
                userStatus = UserStatus.objects.get(user=user)
            except ObjectDoesNotExist:
                newUserStatus = UserStatus(user=user, answeredQuestions='', points=0)
                newUserStatus.save()
            except Exception as e:
                return HttpResponse("Unknown Exception occurred")

            response = HttpResponse("Logged in successfully..")
            response.set_cookie('quizTimeId', str(user.id), max_age=36000)
            return response
    return HttpResponse("Error : Invalid login request")
