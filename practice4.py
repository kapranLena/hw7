#написати функ. яка приймає стрічку, потрібно знайти найдовшу послідовність однакових літер і вивести її довжину

# це чытерство, але воно працюэ :)
def longest():
    text = 'kdjcldjlkkkkkkk'
    import collections
    results = collections.Counter(text)
    print(results)
longest()