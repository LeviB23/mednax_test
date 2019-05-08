class Pencil():

	def __init__(self, lead_durability, eraser_durability):
		self.lead_durability = lead_durability
		self.eraser_durability = eraser_durability
		self.lead_left = lead_durability
		self.eraser_left = eraser_durability
		self.written_text = ''

	def write(self, text):
		characters = list(text)
		count_blank = characters.count(' ')
		count_diff = self.lead_left - (len(characters) - count_blank)
		if count_diff < 0:
			self.lead_left = 0
		else:
			self.lead_left = count_diff

		print(characters)

		if not self.written_text.endswith(' ') and self.written_text != '':
			self.written_text += ' '
		self.written_text += ''.join(characters)
