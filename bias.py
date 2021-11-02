import gensim.downloader as api
wv = api.load('word2vec-google-news-300')

def analogy(w1a, w1b, w2a):
	result = wv.most_similar(negative=[w1a], 
                                positive=[w1b, w2a])
	if result[0][0].lower() == w1b:
		return result[1]
	return result[0]

if __name__ == '__main__':
	# male_words = ["engineer", "football", "guns", "woodworking", "dishwasher", "pizza", "beer", "whiskey", "lifting", "suitcase", "work", "ejaculate", "badass", "sexy", "hot"]
	male_words = ["carpentry", "meat", "beef", "strong", "plumbing"]
	for word in male_words:
		result = analogy("he", word, "she")
		print("Man:%s :: woman:%s by %f" % (word, result[0], result[1]))

	# female_words = ["earrings", "makeup", "ballet", "tampon", "sewing", "cooking", "children", "pottery", "gardening", "cat", "archery", "menstruate", "badass", "sexy", "hot"]
	# female_words = ["tom_boy", "lesbian"]
	# for word in female_words:
	# 	result = analogy("she", word, "he")
	# 	print("She:%s :: he:%s by %f" % (word, result[0], result[1]))

	# words = ["badass", "sexy", "affectionate", "beautiful"]
	# words = ["anxious", "overbearing", "bossy", "rude", "fixated", "unhappy"]

#  assertive -> bossy -> { bitchy, catty } 

#  assertive <- forceful -> strident -> shrill -> naggy -> frumpy
# shrill <- strident <- vehement <- vociferous

	# words = ["assertive", "bossy", "forceful", "bitchy", "arrogant", "catty", "snide", "strident", "combative", "cocky"]
	# words += ["shrill", "naggy", "vehement", "frumps", "frumpy", "dowdy", "vociferous", "confrontational", "adversarial", "judgmental", "pugnacious", "feisty", "spunky", "sassy", "affable"]
	# words = ["ditzy", "cocky", "vivacious", "buffoon", "bimbo", "idiot"]
	# words = ["pretty", "abusive"]

	words = ["beast", "beastly", "beastly", "monster", "fiend", "brute", "animal", "brutish"]
	for word in words:
		female_result = analogy("he", word, "she")
		male_result = analogy("she", word, "he")
		print("He:%s :: she:%s" % (word, female_result[0]))
		print("She:%s :: he:%s" % (word, male_result[0]))