from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    # Gathering INput DAta
    inptext = request.POST.get('text','default')
    checkparam = ['Removed Punctuations ', 'Removed Newline Characters ','Removed Spaces ','Uppercase ']

    #Checking if checkboxs of respective purpose is on/off
    removepunc = request.POST.get('removepunc','off')
    newline = request.POST.get('newline','off')
    removespace = request.POST.get('removespace','off')
    upper = request.POST.get('upper',"off")
    params = {}
    purpose = []
    
    # If puncuations is on
    if removepunc == "on":
        purpose.append("Removed Punctuations ")
        punc = """!@#$%^&*()_+}{][:"';?><,./]"""
        analyzed = ''
        for char in inptext:
            if char not in punc:
                analyzed += char 
        print(analyzed)
        inptext = analyzed
        
    # If new line is on
    if newline == "on":
        purpose.append("Removed Newline Characters ")
        analyzed = inptext.split('\r\n')
        
        analyzed = "".join(analyzed)
        inptext = analyzed
        print(analyzed)
       
    # If spaces is on
    if removespace == "on":
        purpose.append("Removed Spaces ")
        analyzed = inptext.split()
        print(analyzed)
        analyzed = "".join(analyzed)
        inptext = analyzed
        print(analyzed)
    
    # If uppcase is on
    if upper == "on":
        purpose.append("Uppercase ")
        analyzed = inptext.upper()
        print(analyzed)

    # If none of them are on
    if removepunc != "on" and upper!="on" and newline!="on" and removespace!="on":
        return HttpResponse("<script>alert(Error)</script>")
    
    params  = {"purpose": purpose, "analyzed": analyzed,"checkparam":checkparam}
    return render(request,"analyze.html",params)
    