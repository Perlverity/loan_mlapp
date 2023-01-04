from django.shortcuts import render, redirect
from .forms import InputForm, LoginForm, SignUpForm

import joblib
import numpy as np
from .models import Customer
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


# モデルの読み込み
LOADED_MODEL = joblib.load('mlapp/ml_model.pkl')


@login_required
def index(request):
    return render(request, 'mlapp/index.html')


@login_required
def input_form(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('result')
    else:
        form = InputForm()
        return render(request, 'mlapp/input_form.html', {'form': form})


@login_required
def result(request):
    # 最新の登録者のデータを取得
    data = Customer.objects.order_by('id').reverse().values_list('limit_balance', 'education', 'marriage', 'age')

    # 推論の実行
    x = np.array([data[0]])
    y = LOADED_MODEL.predict(x)
    y_proba = LOADED_MODEL.predict_proba(x)
    y_proba = y_proba * 100
    y, y_proba = y[0], y_proba[0]

    # 推論結果を保存
    customer = Customer.objects.order_by('id').reverse()[0]
    customer.proba = y_proba[y]
    customer.result = y
    customer.save()

    # 推論結果をHTMLに渡す
    return render(request, 'mlapp/result.html', {'y': y, 'y_proba': round(y_proba[y], 2)})


@login_required
def history(request):
    if request.method == 'POST':
        # POSTされた値を取得 → 顧客ID
        d_id = request.POST
        # fillterメソッドでidが一致するCustomerデータを取得
        d_customer = Customer.objects.filter(id=d_id['d_id'])
        d_customer.delete()
        customers = Customer.objects.all()
        return render(request, 'mlapp/history.html', {'customers': customers})
    else:
        customers = Customer.objects.all()
        return render(request, 'mlapp/history.html', {'customers': customers})


class Login(LoginView):
    form_class = LoginForm
    template_name = 'mlapp/login.html'


class Logout(LogoutView):
    template_name = 'mlapp/base.html'


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            new_user = authenticate(username=username, password=password)

            if new_user is not None:
                login(request, new_user)

            return redirect('index')
    else:
        form = SignUpForm()
        return render(request, 'mlapp/signup.html', {'form': form})
