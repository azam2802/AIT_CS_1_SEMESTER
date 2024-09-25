shtrih = ['0225', '1116', '9394', '3218', '9678', '6869']
tovar = ['ruchka', 'laptop', 'chay', 'majito', 'sprite', 'rezinka']
tsena = [50, 20000, 50, 65, 55, 20]


def kassoviy_check(karzinka):
    total = 0
    result = 'KASSOVIY CHECK\n_______________\n'
    for k in karzinka.split(','):
        for sh, to, ts in zip(shtrih, tovar, tsena):
            if k == sh:
                result += to + ' -> ' + str(ts) + '\n'
                total += ts
    return result + '\n___________\nTOTAL : ' + str(total)
 


karzinka = '0225,9394,1116'
print(kassoviy_check(karzinka))