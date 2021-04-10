"""Solution for HackerRank challenge: Designer PDF Viewer
"""

def designer_pdf_viewer(heights, word):
    """Calculate the area of highlighted text in a pdf, given the heights of
     all letters of the alphabet, and the highlighted text.

     Assume all letters are of the same width and the highlighted area must
     encompass the largest height letter for the length of the word.

    Hint:
        char = 'a'
        chr(ord(char)) == char #True

    Args:
        heights (int[26]): height of each character.
        word (string): highlighted text to find area for.

    Returns:
        int: area of highlighted word.
    """
    diff = 0 - ord('a') #starting index of heights
    max_height = float('-inf')
    for letter in word:
        if max_height < heights[ord(letter) + diff]:
            max_height = heights[ord(letter) + diff]
    return max_height*len(word)

def main():
    """Receives input from stdin, provides output to stdout.
    """
    heights = map(int, raw_input().strip().split(' '))
    word = raw_input()
    print designer_pdf_viewer(heights, word)

if __name__ == '__main__':
    main()
