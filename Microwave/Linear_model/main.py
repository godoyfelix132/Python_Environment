r = "{:.2f}".format(5)
try:
    r = float(r)
except ValueError:
    try:
        r = complex(r)
    except ValueError:
        print('error')
print(type(r))
print(r)