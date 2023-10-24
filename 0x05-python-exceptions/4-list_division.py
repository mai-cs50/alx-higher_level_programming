#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            num1 = my_list_1[i] if i < len(my_list_1) else 0
            num2 = my_list_2[i] if i < len(my_list_2) else 0

            new_list.append(num1 / num2)
        except ZeroDivisionError:
            new_list.append(0)
            print('division by 0')
            #continue
        except IndexError:
            new_list.append(0)
            print('out of range')
            #continue
        except TypeError:
            new_list.append(0)
            print('wrong type')
            #continue
        finally:
            pass
        return new_list
