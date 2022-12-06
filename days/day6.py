def day6_1():
    with open('res/day6_input.txt', 'r') as file:
        line = file.readlines()[0]
        i = 0
        window = []
        for c in line:
            if len(window) == 4:
                return i
            if window.__contains__(c):
                idx = window.index(c)
                window = window[idx + 1:]
                window.append(c)
                i += 1
                continue
            window.append(c)
            i += 1
        return i

def day6_2():
    with open('res/day6_input.txt', 'r') as file:
        line = file.readlines()[0]
        i = 0
        window = []
        for c in line:
            if len(window) == 14:
                return i
            if window.__contains__(c):
                idx = window.index(c)
                window = window[idx + 1:]
                window.append(c)
                i += 1
                continue
            window.append(c)
            i += 1
        return i
