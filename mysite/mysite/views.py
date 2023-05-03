# I have created this file - akanksha gupta
from django.http import HttpResponse
from django.core.files import File
from django.shortcuts import render

def index(request):
    return render (request,'index.html')
    #return HttpResponse('<h1>Home</h1><a href = "/removePunc">Next</a>')

def analyze(request):
    djtext = request.POST.get('text','default')
    removePunc = request.POST.get('removePunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newLine = request.POST.get('newLine','off')
    extraspaceRemover = request.POST.get('extraspaceRemover','off')
    charCount = request.POST.get('charCount','off')
    punctuations = '''.,?;!'()[]""..._/@{}<>#$&~^'''
    operations = ""
    analyze = djtext
    if removePunc == "on":
        analyzed = ""
        for char in analyze:
            if char not in punctuations:
                analyzed = analyzed + char
        analyze = analyzed
        operations = operations + "Remove Punctuations" + " "

    if fullcaps == "on":
        analyzed = ""
        for char in analyze:
            analyzed = analyzed + char.upper()
        analyze = analyzed
        operations = operations + "Capitalize Sentence" + " "

    if newLine == "on":
        analyzed = ""
        for char in analyze:
            if char != "\n" and char != "\r":
             analyzed = analyzed + char
        analyze = analyzed
        operations = operations + "Line Remover" + " "
        
    if extraspaceRemover == "on":
        analyzed = ""
        for index,char in enumerate(analyze):
            if not(analyze[index] == " " and analyze[index+1] == " "):
                analyzed = analyzed + analyze[index]    
        analyze = analyzed
        operations = operations + "Extra Space Remover" + " "
        
    if charCount == "on":
        analyzed = len(analyze) 
        if(analyze == djtext):
            analyze = "Character count is: " + str(analyzed) 
        else:
            analyze = analyze + " and Character count is: "+ str(analyzed)
        operations = operations + "Character Count" + " "

    if removePunc!="on" and fullcaps!="on" and newLine!="on" and extraspaceRemover!="on" and charCount!="on":
        return HttpResponse("<h1>No option is selected.Please select atleast a option.</h1>")
    params = {'purpose':operations,'analyzed_text':analyze,'prov':djtext}
    return render(request,'analyze.html',params)
    

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
# def capitalFirst(request):
#     return HttpResponse("Capitalize First")

# def newlineRemove(request):
#     return HttpResponse("Remove new line")

# def spaceRemove(request):
#     return HttpResponse("Remove space")

# def charCount(request):
#     return HttpResponse("Count Character")