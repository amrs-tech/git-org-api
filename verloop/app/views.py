from django.shortcuts import render
import requests

# Create your views here.


def repos(request, org):

    url = "https://api.github.com/orgs/"+str(org)+'/repos'

    s = requests.Session()

    data = s.get(url)

    data = data.json()

    print(len(data))

    lst = []
    for i in range(len(data)):
        lst.append([data[i]['stargazers_count'],data[i]['name']])
    newlst = sorted(lst, key=lambda x: x[0], reverse=True)
    j=0
    while j<3:
        print(newlst[j][1],' - ',newlst[j][0])
        j+=1


    return render(request,'app/repos.html', {'data': newlst[:3]})
