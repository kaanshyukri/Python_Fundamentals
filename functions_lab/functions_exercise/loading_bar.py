def loading_bar(x):
    if x == 100:
        return f"100% Complete! \n" \
               f"[%%%%%%%%%%]"
    else:
        return f"{x}% [{'%'*(x//10)}{'.'*((100-x)//10)}]\n" \
               f"Still loading..."


number = int(input())
print(loading_bar(number))
