#payroll

name = input("Enter name: ")
hours_per_week = int(input("Enter hours_per_week: "))
hourly_pay_rate = float(input("Enter hourly_pay_rate: "))
CPF_rate = float(input("Enter CPF_rate: "))

gross_pay = hourly_pay_rate * hours_per_week
contribution = gross_pay * (CPF_rate/100)
net_pay = gross_pay - contribution

print('\nPayroll statement for', name,
      '\nHours per week: ', hours_per_week,
      '\nHourly pay rate: $',"%.2f" % hourly_pay_rate,
      '\nGross pay = $',"%.2f" % gross_pay ,
      '\nCPF contribution at',CPF_rate,'% = $', "%.2f" % contribution,
      '\n',
      '\nNet pay = $', "%.2f" % net_pay)
