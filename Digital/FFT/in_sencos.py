from fxpmath import Fxp



# Driver Code
if __name__ == "__main__":
    n = 3628800
    data_list = []
    file = open('ttt.txt', 'w')
    for i in range(10):
        x = Fxp(n, True, 64, 32)  # signed=True, n_word=16, n_frac=8
        r = x.bin(frac_dot=False)
        r = str(r) + '\n'
        print(r)