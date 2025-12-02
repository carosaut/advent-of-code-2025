'''After completing the puzzle, I put the code through an LLM to see what improvements I could make. This is the result of that.
    - using 'split' rather than overly complicated get_ids() function
    - finding repeating patters using a single function rather than all the 'is_div' functions
    - use range() with a step arg rather than manually slicing the string
    - use the same func for parts one and two
    - use map() to get start and end
'''

input = '824-1475,967620-1012917,2727216511-2727316897,56345-141494,8811120-8999774,5727326-5922513,935306-961989,76751455-76787170,723458-849157,144648-162230,1597-3207,326085-472746,14-34,66-132,9453977670-9454023729,959903262-960027272,17168-26699,190-332,3351-5602,1-11,371280315-371448887,6252062-6312899,9696887156-9697040132,37-58,32770-52161,6443650762-6443689882,473092-582157,3309726-3347079,852735-912990,8294840594-8294926063,3773964-3884030,7718304-7809359,601947-677833,3434304207-3434405118,449-673,64525269-64702774,31545468-31784543,184451-308951,5771-11485'
# input = '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'


def is_repeated_pattern(num, divisor):
    """Check if num can be split into equal repeated chunks."""
    string_num = str(num)
    length = len(string_num)
    
    if length % divisor != 0:
        return False
    
    chunk_size = length // divisor
    chunk = string_num[:chunk_size]
    
    return all(string_num[i:i+chunk_size] == chunk for i in range(0, length, chunk_size))

list_id_ranges = input.split(',')

def get_invalid_ids(list_id_ranges, check_divisors):
    """Find invalid IDs based on which divisors to check."""
    invalid_ids = []
    
    for id_range in list_id_ranges:
        start, end = map(int, id_range.split('-'))
        
        for num in range(start, end + 1):
            length = len(str(num))
            
            for divisor in check_divisors:
                if length % divisor == 0 and is_repeated_pattern(num, divisor):
                    invalid_ids.append(num)
                    break  # Found a pattern, move to next number
    
    return invalid_ids

# Part 1: only check divisor 2 (split in half)
invalid_ids_1 = get_invalid_ids(list_id_ranges, [2])

# Part 2: check divisors 2, 3, 5, 7
invalid_ids_2 = get_invalid_ids(list_id_ranges, [2, 3, 5, 7])


print(f'Answer to Part 1: {sum(invalid_ids_1)}')
      
print(f'Answer to Part 2: {sum(invalid_ids_2)}')




