from django.shortcuts import render, get_object_or_404,redirect
from .models import Client, Transaction
from .forms import ClientForm,TransactionForm
from .serializers import ClientSerializer, TransactionSerializer
from rest_framework import viewsets
from .permissions import IsAdminOrReadOnly

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'clients/client_list.html', {'clients': clients})

def client_detail(request,pk):
    client = get_object_or_404(Client, pk = pk)
    return render(request,  'clients/client_detail.html', {'client': client})

def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'clients/client_form.html', {'form': form})

def client_update(request,pk):
    client = get_object_or_404(Client,pk = pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance = client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'clients/client_form.html', {'form': form})

def client_delete(request, pk):
    client = get_object_or_404(Client,pk = pk)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request,'clients/client_confirm_delete.html', {'client': client})

# Список транзакций клиента
def transaction_list(request, client_pk):
    client = get_object_or_404(Client, pk=client_pk)
    transactions = client.transactions.all()
    return render(request, 'clients/transaction_list.html', {'client': client, 'transactions': transactions})

# Создание транзакции
def transaction_create(request, client_pk):
    client = get_object_or_404(Client, pk=client_pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.client = client
            transaction.save()
            return redirect('transaction_list', client_pk=client.pk)
    else:
        form = TransactionForm()
    return render(request, 'clients/transaction_form.html', {'form': form, 'client': client})

# Редактирование транзакции
def transaction_update(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_list', client_pk=transaction.client.pk)
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'clients/transaction_form.html', {'form': form, 'client': transaction.client})

# Удаление транзакции
def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_list', client_pk=transaction.client.pk)
    return render(request, 'clients/transaction_confirm_delete.html', {'transaction': transaction})

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAdminOrReadOnly]

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAdminOrReadOnly]

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90e…I6Mn0.QmM7XjXj3lGCsteThll4QHDEZBnjhdvsCzy0ROVNQVg
