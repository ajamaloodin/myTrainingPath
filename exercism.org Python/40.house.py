def buildverses(start_verse, end_verse):

    entities = ['house that Jack built.', 'malt', 'rat', 'cat', 'dog', 'cow with the crumpled horn',
                'maiden all forlorn', 'man all tattered and torn', 'priest all shaven and shorn',
                'rooster that crowed in the morn', 'farmer sowing his corn', 'horse and the hound and the horn']
    verbs = ['', 'ate the ', 'killed the ', 'worried the ', 'tossed the ', 'milked the ', 'kissed the ',
             'married the ', 'woke the ', 'kept the ', 'belonged to the ']
    thisIs = 'This is the '
    bottomline = ' that lay in the house that Jack built.'
    verse = ''

    if start_verse == 1 and end_verse == 1:
        return thisIs + entities[0]

    verse = thisIs + entities[start_verse-1]

    index = end_verse-2
    while index >= 1:
        verse = verse + ' that ' + verbs[index] + entities[index]
        index = index - 1

    verse = verse + bottomline
    return verse


def recite(start_verse, end_verse):
    the_verse = []

    if start_verse == end_verse:
        return [buildverses(start_verse, end_verse)]

    for index in range(start_verse, end_verse+1):
        the_verse.append(buildverses(index, index))
    return the_verse
