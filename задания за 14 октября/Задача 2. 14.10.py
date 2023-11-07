a = []
st = 'gdhfdhbygygbfebfeurheygfyebehbhcdyfgydfhdbfgfbfjdhdushdxnchdvyrgttyrhfjdhfhuhrfdudgf'
let = 'gsrrdrdr'
def first_last(st, let):
    sst = st.find(let)
    llet = st.rfind(let)
    if st.find(let) != -1: 
        a.append(sst)
        a.append(llet)
    else:
        print('None')
    print(a)
first_last(st, let)        