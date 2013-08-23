N = input()
titles = {}
authors = {}
keywords = {}
publishers = {}
published_years = {}
for n in xrange(N):
    id, title, author, keyword, publisher, published_year \
        = [raw_input() for i in xrange(6)]
    titles.setdefault(title, []).append(id)
    authors.setdefault(author, []).append(id)
    for key in keyword.split():
        keywords.setdefault(key, []).append(id)
    publishers.setdefault(publisher, []).append(id)
    published_years.setdefault(published_year, []).append(id)

M = input()
queries = [raw_input() for m in xrange(M)]
datas = [titles, authors, keywords, publishers, published_years]
datas = dict(zip(list('12345'), datas))
for q in queries:
    print q
    result = datas[q[0]].setdefault(q[3:], [])
    if not result:
        print 'Not Found'
    for id in sorted(result):
        print id
