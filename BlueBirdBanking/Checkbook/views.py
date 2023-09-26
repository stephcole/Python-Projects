from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction


# Create your views here.
# this function will render the Home page when requested
def home(request):
    form = TransactionForm(data=request.POST or None)  # retrieve the transaction form
    # check if request method is POST
    if request.method == 'POST':
        pk = request.POST['account']  # if the form is submitted retrieve which account the user wants to view
        return balance(request, pk)  # call balance function to render that accounts balance sheet
    content = {'form': form}  # pass content to the template in a dictionary
    # adds content of form to page
    return render(request, 'checkbook/index.html', content)


# this function will render the Create New Account page when requested
def create_account(request):
    form = AccountForm(data=request.POST or None)  # retrieve the account form
    # check if request method is POST
    if request.method == 'POST':
        if form.is_valid():  # check to see f the submitted form is valid and if so saves the form
            form.save()  # saves new account
            return redirect('index')  # returns user back to the homepage
    content = {'form': form}  # saves content to the template as a directory
    # adds content of form to page
    return render(request, 'checkbook/CreateNewAccount.html', content)


# this function will render the balance page when requested
def balance(request, pk):
    account = get_object_or_404(Account, pk=pk)  # retrieve the requested account using its primary key
    transactions = Transaction.Transactions.filter(account=pk)  # retrieve all of that accounts transactions
    current_total = account.initial_deposit  # create account total variable starting with initial deposit value
    table_contents = {}  # create a dictionary into which transaction info will be placed
    for t in transactions:  # loop through transactions and determine which is a deposit and which is a withdrawl
        if t.type == 'Deposit':
            current_total += t.amount  # if deposit add amount to balance
            table_contents.update({t: current_total})  # add transaction and total to the dictionary
        else:
            current_total -= t.amount  # if withdrawal subtracts amount to balance
            table_contents.update({t: current_total})  # add transaction and total to dictionary
    # pass account, account total balance, and transaction information to the template
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)


# this function will render the transaction page when requested
def transaction(request):
    form = TransactionForm(data=request.POST or None)  # retrieve the transaction form
    # check if request method is POST
    if request.method == 'POST':
        if form.is_valid():  # check to see f the submitted form is valid and if so saves the form
            pk = request.POST['account'] # retrieve which account the transaction was for
            form.save()  # saves the transaction form
            return balance(request, pk) # renders balance of the accounts balance sheet

    # pass content to the template in a dictionary
    content = {'form': form}
    # adds content of form to page
    return render(request, 'checkbook/AddTransaction.html', content)
