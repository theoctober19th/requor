from django.shortcuts import render
from .models import QuestionModel, AnswerModel, CategoryModel, UserModel
from faker import Faker
from faker.providers import date_time, internet
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
    questions = QuestionModel.objects.all()

    context = {
        'questions': questions
    }

    return render(request, 'qna_app/index.html', context=context)

def add_question(request):
    return render(request, 'qna_app/add_question.html')

def detail(request, id):

    question = QuestionModel.objects.filter(id=id).first()

    if request.method == 'POST':
        #this means the user submitted the answer
        user = UserModel.objects.get(id=request.session['id'])
        answer = AnswerModel(description=request.POST['answer'], question=question, user=user)
        answer.save(force_insert=True)
    
    answers = AnswerModel.objects.filter(question=id)

    d = {
        'question': question,
        'answers': answers
    }

    return render(request, 'qna_app/detail.html', d)
        
    # question = QuestionModel.objects.get(id=id)

    # if request.method == 'POST':
    #     user = UserModel.objects.get(id=request.session['id'])
    #     new_answer = AnswerModel(description=request.POST['answer'], question=question, user=user)

    # answers = AnswerModel.objects.filter(question=id)

    # d = {
    #     'question': question,
    #     'answers': answers
    # }

    # return render(request, 'qna_app/detail.html', d)


def faker(request):
    fake = Faker()
    fake.add_provider(date_time)
    fake.add_provider(internet)
    category = CategoryModel(name='Django', description='Related to Django')
    category.save(force_insert=True)
    name = fake.name()
    email = fake.ascii_email()
    username='admin'
    password='admin'
    reputation=7
    user = UserModel(name=name, email=email, username=username, password=password, reputation=reputation)
    user.save(force_insert=True)
    for i in range(20):
        Faker.seed(i)
        title = fake.sentence()
        description = fake.text()
        posted = fake.date_time()
        image = fake.image_url()
        votes = fake.random_digit()
        is_answered = False
        question = QuestionModel(title=title, description=description, posted=posted, image=image, votes=votes, is_answered=is_answered, category=category, user=user)
        question.save(force_insert=True)
        for j in range(5):
            Faker.seed(j*13)
            answer = AnswerModel(description=description, posted=posted, image=image, question=question, votes=votes, is_accepted=False, user=user)
            answer.save(force_insert=True)
    return HttpResponse('<h1>Fake data created successfully</h1>')
    