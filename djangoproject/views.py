from django.shortcuts import render

# request take two argument one is request and other is name of file 
def homePage(request):
    return render(request,"index.html")
def loginPage(request):
    return render(request,"signin.html")
def signupPage(request):
    return render(request,"signup.html")