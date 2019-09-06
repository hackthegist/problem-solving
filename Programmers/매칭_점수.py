'''
(2018년) KAKAO BLIND RECRUITMENT 매칭 점수

'''
import re

word = "blind"
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]

def get_bscore(word, page):
    tokens = page.split()
    body_s = tokens.index("<body>")
    body_f = tokens.index("</body>")
    score = 0
    for token in tokens[body_s+1:body_f]:
        if token.upper() == word.upper():
            score += 1
    return score

def get_lcnt(page):
    p = re.compile("<a[\w\s]+>")
    result = p.findall(page)
    return len(result)

def get_links(page, pages):
    links = []
    pages,pop(1)
    score = 0

def get_lscore(page, pages):
    pages,pop(1)
    score = 0




def solution(word, pages):
    answer = 0

    return answer

# solution(word, pages)
print(get_lcnt(pages[0]))
