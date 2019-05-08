class Pencil():

	def __init__(self, lead_durability, eraser_durability):
		self.lead_durability = lead_durability
		self.eraser_durability = eraser_durability
		self.lead_left = lead_durability
		self.eraser_left = eraser_durability
		self.written_text = ''

	def write(self, text):
		characters = list(text)
		# count_blank = characters.count(' ')
		# count_diff = self.lead_left - (len(characters) - count_blank)
		# if count_diff < 0:
		# 	self.lead_left = 0
		# 	del characters[abs(count_diff):len(characters)]
		# 	blank_list = [' ' for i in range(abs(count_diff))]
			# characters = characters + blank_list
		# else:
		# 	self.lead_left = count_diff

		# print(characters)

		# if not self.written_text.endswith(' ') and self.written_text != '':
		# 	self.written_text += ' '
		# self.written_text += ''.join(characters)
		if not self.written_text.endswith(' ') and self.written_text != '' and self.lead_left > 0:
			self.written_text += ' '

		for character in characters:
			if self.lead_left > 0:
				self.written_text += character
			else:
				self.written_text += ' '

			if character != ' ' and self.lead_left > 0:
				self.lead_left -= 1

	def sharpen(self):
		self.lead_left = self.lead_durability
