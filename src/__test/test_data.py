

text = """
  Life is a canvas painted with experiences,
  each stroke representing choices and reflections. 
  As we question our existence,
  we uncover the delicate threads connecting us to others.
  In embracing uncertainty,we find meaning,
  realizing that the journey itself holds the answers we seek.
  This[tab]line[tab]is[tab]spaced[tab]by[tab]tab[tab]characters.
""".replace("[tab]","\t")
# note 1: ",we" is intended, for word wrap test !
# note 2: The tab characters are important for testing.
unwrappedText = "Life is a canvas painted with experiences, each stroke representing choices and reflections. As we question our existence, we uncover the delicate threads connecting us to others. In embracing uncertainty, we find meaning, realizing that the journey itself holds the answers we seek."
unwrappedText += " This line is spaced by tab characters."

textA = "Science is organized knowledge. Wisdom is organized life."
textB = "Science is organized. Wisdom is organized."
