login = input('Enter your user name =>')
if (login == "Taz") :
    print('Wellcome', login)
    confirm = input('If you want to continue, type "yes"=>')
    if (confirm == "yes") :
        hr = input('Enter the total working hour:')
        rt = input('Enter the total rate:')
        fhr = float(hr)
        frt = float(rt)
        pay = (fhr*frt)
        if (fhr > 40) :
            extra_hr = (fhr - 40)
            extra_py = (extra_hr * 1.5)
            total_extra_py = pay + extra_py
            print('Your total Pay is', total_extra_py)
        else:
            print('Your total Pay is', pay)
    else:
        print('Thank You, Hope we see you again.')

else:
    print('Sorry, Unknnown User Detedcted')
