from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .models import TradeRecord, Trader
from django.contrib.auth.models import User
from django.http import HttpResponse


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect(reverse("user-dashboard"))
        else:
            messages.info(request, "Credentials Invalid")
            return redirect(reverse("login"))
    else:
        return render(request, "login.html")
    

def logout(request):
    auth.logout(request)
    return redirect("/")

@login_required
def user_dashboard(request):
    print(request.user)
    current_user = User.objects.get(username=request.user)
    current_trader = Trader.objects.get(user=current_user)
    user_record = TradeRecord.objects.filter(trader=current_trader)
    context = {"user_record": user_record,
               "current_trader": current_trader}
    return render(request, "index.html", context)


@login_required
def admin_dashboard(request):
    if request.user.is_superuser == True:
        all_traders = Trader.objects.all()
        print(all_traders)
        count_list = []
        for trader in all_traders:
            all_user_trades = TradeRecord.objects.filter(trader=trader).count()
            count_list.append(all_user_trades)
        print(count_list)
        context = {"all_traders": all_traders, 
                "count_list": count_list}
    else:
        return HttpResponse("You are not an admin")
    return render(request, "admin_index.html", context)


from django.shortcuts import render

def graph_view(request):
    data = [12, 19, 3, 5, 2]
    return render(request, 'graph.html', {'data': data})
