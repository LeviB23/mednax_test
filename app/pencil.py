class Pencil():

	def __init__(self, lead_durability, eraser_durability):
		self.lead_durability = lead_durability
		self.eraser_durability = eraser_durability
		self.lead_left = lead_durability
		self.eraser_left = eraser_durability
		self.written_text = ''

	def write(self, text):
		characters = list(text)
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

	def erase(self, text):
		last_index = self.written_text.rfind(text)
		text_count = len(text)
		blank_count = text.count(' ')
		self.written_text = self.written_text[:last_index] +self.written_text[(last_index+text_count):]
		self.eraser_left -= (text_count - blank_count)

	def edit(self, index, text):
		return False