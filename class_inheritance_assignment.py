
#create parent class 'European_Tourism'
class European_Tourism:
    name = 'Atlas European Travel'
    email = 'atlas_eurotravel@gmail.com'
    password = 'letsgo!'
    account_number = 0
#create child class option 1
class Events(European_Tourism):
    Germany = 'Oktoberfest'
    France = 'Bastille Day'
    Sweden = 'Midsommar'
    #create child class option 2
class Travel(European_Tourism):
    Public_Transport = 'Rail_transport', 'Air_travel', 'Coach_transport', 'Ferry'
    Private_Transport = 'Car_rental', 'Private_jet'
