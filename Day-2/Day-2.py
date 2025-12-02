input = '824-1475,967620-1012917,2727216511-2727316897,56345-141494,8811120-8999774,5727326-5922513,935306-961989,76751455-76787170,723458-849157,144648-162230,1597-3207,326085-472746,14-34,66-132,9453977670-9454023729,959903262-960027272,17168-26699,190-332,3351-5602,1-11,371280315-371448887,6252062-6312899,9696887156-9697040132,37-58,32770-52161,6443650762-6443689882,473092-582157,3309726-3347079,852735-912990,8294840594-8294926063,3773964-3884030,7718304-7809359,601947-677833,3434304207-3434405118,449-673,64525269-64702774,31545468-31784543,184451-308951,5771-11485'
# input = '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

lst_indexes = find(input, ',')

def is_even(n):
    return n % 2 == 0

def is_div_by_3(n):
    return n % 3 == 0

def is_div_by_5(n):
    return n % 5 == 0

def is_div_by_7(n):
    return n % 7 == 0

def get_ids(lst_indexes):
    list_id_ranges = []
    for index, element in enumerate(lst_indexes):
        if index == 0:
            first_start = 0
            first_end = int(element)
            first_range = input[first_start:first_end]
            list_id_ranges.append(first_range)

        elif index == len(lst_indexes) - 1:
            start = lst_indexes[index-1] + 1
            id_range = input[start:]
            list_id_ranges.extend(id_range.split(','))

        else:
            start = lst_indexes[index-1] + 1
            end = element
            id_range = input[start:end]
            list_id_ranges.append(id_range)
    return list_id_ranges

list_id_ranges = get_ids(lst_indexes)

def get_invalid_ids_1(list_id_ranges):
    invalid_ids = []
    for id_range in list_id_ranges:
        start_end = id_range.split('-')
        start = int(start_end[0])
        end = int(start_end[1]) +1
        for num in range(start, end):
            str_num = str(num)
            lenght_num = len(str_num)
            if is_even(lenght_num):
                firstnum, secondnum = str_num[:lenght_num//2], str_num[lenght_num//2:]
                if firstnum == secondnum:
                    invalid_ids.append(num)
    return invalid_ids


def get_invalid_ids_2(list_id_ranges):
    invalid_ids = []
    for id_range in list_id_ranges:
        start_end = id_range.split('-')
        start = int(start_end[0])
        end = int(start_end[1]) +1
        for num in range(start, end):
            str_num = str(num)
            lenght_num = len(str_num)
            if is_div_by_7(lenght_num):
                firstnum, secondnum, thirdnum, fourthnum, fifthnum, sixthnum, seventhnum = str_num[0:lenght_num//7], str_num[lenght_num//7:2*lenght_num//7], str_num[2*lenght_num//7:3*lenght_num//7], str_num[3*lenght_num//7:4*lenght_num//7], str_num[4*lenght_num//7:5*lenght_num//7], str_num[5*lenght_num//7:6*lenght_num//7], str_num[6*lenght_num//7:]
                if firstnum == secondnum == thirdnum == fourthnum == fifthnum == sixthnum == seventhnum:
                    invalid_ids.append(num)
                    continue
            if is_div_by_5(lenght_num):
                firstnum, secondnum, thirdnum, fourthnum, fifthnum = str_num[0:lenght_num//5], str_num[lenght_num//5:2*lenght_num//5], str_num[2*lenght_num//5:3*lenght_num//5], str_num[3*lenght_num//5:4*lenght_num//5], str_num[4*lenght_num//5:]
                if firstnum == secondnum == thirdnum == fourthnum == fifthnum:
                    invalid_ids.append(num)
                    continue       
            if is_div_by_3(lenght_num):
                firstnum, secondnum, thirdnum = str_num[:lenght_num//3], str_num[lenght_num//3:-lenght_num//3], str_num[-lenght_num//3:]
                if firstnum == secondnum == thirdnum:
                    invalid_ids.append(num)
                    continue
            if is_even(lenght_num):
                firstnum, secondnum = str_num[:lenght_num//2], str_num[lenght_num//2:]
                if firstnum == secondnum:
                    invalid_ids.append(num)
    return invalid_ids

invalid_ids_1 = get_invalid_ids_1(list_id_ranges)
invalid_ids_2 = get_invalid_ids_2(list_id_ranges)


print(f'Answer to Part 1: {sum(invalid_ids_1)}')
      
print(f'Answer to Part 2: {sum(invalid_ids_2)}')




