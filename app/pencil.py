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
		text_count = len(text)
		if self.eraser_left - text_count < 0:
			text = text[:self.eraser_left]
			text_count = len(text)
		self.eraser_left -= text_count
		last_index = self.written_text.rfind(text)
		self.written_text = self.written_text[:last_index] +self.written_text[(last_index+text_count):]
		
	def edit(self, index, text):
		characters = list(text)
		written_list = list(self.written_text)
		blank_count = text.count(' ')
		text_count = len(text)
		curr_index = index
		for character in characters:
			if written_list[curr_index] == ' ':
				written_list[curr_index] = character
			else:
				written_list[curr_index] = '@'
			curr_index += 1
			if character != ' ' and self.lead_left > 0:
				self.lead_left -= 1
		self.written_text = ''.join(written_list)