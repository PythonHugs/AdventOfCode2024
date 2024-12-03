import re


def find_matches(text):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, text)
    return matches

def do_math(matches):
    results = []
    for x, y in matches:
        x, y = int(x), int(y)
        result = x * y
        results.append((x, y, result))
    return results

def main():
    raw_text = open('input.txt').read()
    matches = find_matches(raw_text)
    results = do_math(matches)
    print(sum(result for _, _, result in results))  # add all the 3rd elements


if __name__ == '__main__':
    main()
