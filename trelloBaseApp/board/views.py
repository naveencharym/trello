from django.shortcuts import render
from django.http import HttpResponse
from .models import Board,task,card
import simplejson


def index(request):
    allBoards = Board.objects.all();
    context  = {
        'all_boards':allBoards
    }

    return render(request,'board/boards.html',context)


def save_board(request):
    isBoardExists = Board.objects.filter(name=request.GET.get("name"))
    if len(isBoardExists)==0:
        board = Board(name=request.GET.get("name"));
        board.save();
        return HttpResponse(simplejson.dumps({"statusCode":200,"message":"Board created successfully"}))
    else:
        return HttpResponse(simplejson.dumps({"statusCode": 204, "message": "Board in use"}))


def save_task(request):
    isTaskExists = task.objects.filter(task_name=request.GET.get("task_name"))
    if len(isTaskExists)== 0:
        boardName = request.GET.get("board_name")
        board = Board.objects.get(name=boardName)
        taskObj = task(task_name=request.GET.get("task_name"))
        taskObj.board = board
        taskObj.save()
        return HttpResponse(simplejson.dumps({"statusCode": 200, "message": "Task created successfully"}))
    else:
        return HttpResponse(simplejson.dumps({"statusCode": 204, "message": "Task in use"}))


def save_card(request):
    isCardExists = card.objects.filter(card_name = request.GET.get("card_name"));
    print "save card"
    if len(isCardExists)==0:
        print "ifffffffffffff"
        taskName  = request.GET.get("task_name")
        selectedtask = task.objects.filter(task_name=taskName)
        cardobj   = card(card_name=request.GET.get("card_name"))
        cardobj.tasks = selectedtask[0]
        cardobj.save()
        return HttpResponse(simplejson.dumps({"statusCode": 200, "message": "Card created successfully"}))
    else:
        return HttpResponse(simplejson.dumps({"statusCode": 204, "message": "Card in use"}))


def boardDetails(request,board_info):
    selectedBoardInfo = Board.objects.filter(name=board_info);
    allLists = [];
    taskeWithCards =[]
    try:
        allLists = task.objects.filter(board=selectedBoardInfo)
    except :
        print "error occured at boardadddetils line"
    #allLists = allLists.list()

    for li in allLists:
        cardObj = {};
        cards = card.objects.filter(tasks=li)
        cardObj[li] =cards;
        taskeWithCards.append(cardObj);


    context = {
        'all_lists': taskeWithCards
    }
    return render(request,'board/list.html',{"name":board_info,"boardLists":context})


def cardsRelatedtoTask(request,task_name):
    selectedTaskName = Board.objects.filter(name=task_name);
    print selectedTaskName
    allCards = [];
    allCards = card.objects.filter(task=selectedTaskName)

    context = {
        'all_cards': allCards
    }
    return render(request,'board/list.html',{"name":selectedTaskName,"boardLists":context})


def deleteBoard(request):
    print request.GET.get("board_name")
    board_name = request.GET.get("board_name")
    instance = Board.objects.get(name=board_name)
    instance.delete();
    return  HttpResponse(simplejson.dumps({"statusCode":200,"message": "board deleted successfully"}))


def deleteTask(request):
    print request.GET.get("task_name")
    task_name = request.GET.get("task_name")
    instance = task.objects.get(task_name=task_name)
    instance.delete();
    return  HttpResponse(simplejson.dumps({"statusCode":200,"message": "task deleted successfully"}))


def deleteCard(request):
    print request.GET.get("card_name")
    card_name = request.GET.get("card_name")
    instance = card.objects.get(card_name=card_name)
    instance.delete();
    return  HttpResponse(simplejson.dumps({"statusCode":200,"message": "card deleted successfully"}))