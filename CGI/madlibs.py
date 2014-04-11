ADJ = "ADJECTIVE"
NOUN = "NOUN"
VERB = "VERB"
ADV = "ADVERB"

class Sentence():
	"""
	>>> s = Sentence([ADJ, ADJ, NOUN], "The %s alien examined the %s %s hungrily.")
	>>> filled_blanks = ["silly", "fun", "computer"]
	>>> s.replace(filled_blanks)
	'The silly alien examined the fun computer hungrily.'
	"""
	def __init__(self, blanks, template):
		self.template = template # story 
		self.blanks = blanks # blanks is array of blanks to fill in
	def replace(self, replacements): # replacements is words fetched from form 
		return self.template % tuple(replacements)


sentences = [
	Sentence([ADJ, ADJ, NOUN], "The %s alien examined the %s %s hungrily."),
	Sentence([ADJ, ADJ, NOUN], "The %s alien examined the %s %s hungrily."),
	Sentence([ADJ, ADJ, NOUN], "The %s alien examined the %s %s hungrily."),
	Sentence([ADJ, ADJ, NOUN], "The %s alien examined the %s %s hungrily."),
]


FIELD_SENTENCE = 'sentence'
FIELD_ITEM = 'item%d'


class Controller(object):

	def __init__(self):
		import cgi, random
		form = cgi.FieldStorage() # {'item1': silly, 'item': fun}

		self.is_story = FIELD_SENTENCE in form
		if self.is_story:
			sentence_id = int(form["sentence"].value)
			sentence = sentences[sentence_id]
			num_blanks = len(sentence.blanks)
			blanks = [form[FIELD_ITEM % i].value for i in xrange(num_blanks)]
			self.sentence_id = sentence_id
			self.sentence = sentence
			self.blanks = blanks

		else:
			self.sentence_id = random.randint(0, len(sentences))


class View(object):
	def __init__(self):
		self.printed_header = False

	def print_form(self, sentence_id):
		print 'Content-Type: text/html'
		print
		print '<form action="madlibs.cgi">'
		print '<h1> Welcome to MadLibs! </h1>'
		sentence = sentences[sentence_id] # sentence.template, sentence.blanks is what needs to be filled in
		blanks = sentence.blanks
		for i in xrange(len(blanks)):
			blank = blanks[i]
			print '''<label for="{fieldname}">{label}</label><input type="text" id="{fieldname}" name="{fieldname}">
			'''.format(fieldname=FIELD_ITEM%i, label=blank)
		print '<input type=hidden value="' + str(sentence_id) + '" name="sentence" id="sentence">'
		print '<input type=submit value="Okay.">'
		print '</form>'


	def print_content(self, content):
		print 'Content-Type: text/html'
		print
		print '<h1>' + content + '</h1>'
		print '<a href="http://inst.eecs.berkeley.edu/~cs9h-am/madlibs.cgi"> Try another one. </a> '

	@staticmethod
	def sanitize_html(content):
		import pydoc
		return pydoc.html.repr(content)


def main():
	controller = Controller()
	view = View()

	if controller.is_story: # print sentence
		filled_blanks = controller.blanks
		sentence = controller.sentence
		clean_sentence = view.sanitize_html(sentence.replace(filled_blanks))
		view.print_content(clean_sentence)


	else: # prompt blanks
		view.print_form(controller.sentence_id)


if __name__ == '__main__':
	main()
