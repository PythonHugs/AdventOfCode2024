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
    print(results)
    return results

def split_by_dos(raw_text):
    raw_text_split_by_donts = raw_text.split("do()")
    print(raw_text_split_by_donts)
    return raw_text_split_by_donts

def find_valid_chunks(split_text):
    valid_chunks = []
    for chunk in split_text:
        if "don't()" in chunk:
            valid_chunks.append(chunk.split("don't()")[0])
        else:
            valid_chunks.append(chunk)
    print(valid_chunks)
    return valid_chunks

def find_matches_in_chunks(valid_chunks):
    matches = []
    for chunk in valid_chunks:
        matches.extend(find_matches(chunk))
    print(matches)
    return matches

def main():
    raw_text = open('input.txt').read()
    split_text = split_by_dos(raw_text)
    valid_chunks = find_valid_chunks(split_text)
    matches = find_matches_in_chunks(valid_chunks)
    results = do_math(matches)
    print(sum(result for _, _, result in results))  # add all the 3rd elements


if __name__ == '__main__':
    main()
