import pytest
from app.pencil import Pencil


class TestPencil:
	
	def test_write(self):
		pencil = Pencil(50, 50)
		pencil.write('Hello world')
		assert pencil.written_text == 'Hello world'
		assert pencil.lead_left == 40

	def test_write_twice(self):
		pencil = Pencil(50, 50)
		pencil.write('Hello world')
		assert pencil.written_text == 'Hello world'
		assert pencil.lead_left == 40
		pencil.write('what a great day')
		assert pencil.written_text == 'Hello world what a great day'
		assert pencil.lead_left == 27

	def test_write_extra(self):
		pencil = Pencil(5, 5)
		pencil.write('Hello world')
		assert pencil.written_text == 'Hello      '
		assert pencil.lead_left == 0

	def test_sharpen(self):
		pencil = Pencil(50, 50)
		pencil.write('Hello world')
		pencil.sharpen()
		assert pencil.lead_durability == 50

	def test_erase(self):
		pencil = Pencil(50, 50)
		pencil.write('Hello world')
		pencil.erase('worl')
		assert pencil.eraser_left == 46
		assert pencil.written_text == 'Hello d'

	def test_erase_extra(self):
		pencil = Pencil(50, 3)
		pencil.write('Hello world')
		pencil.erase('worl')
		assert pencil.eraser_left == 0
		assert pencil.written_text == 'Hello ld'

	def test_edit(self):
		pencil = Pencil(50, 50)
		pencil.write('Hello world')
		pencil.edit(6, 'Susan')
		assert pencil.written_text == 'Hello @@@@@'

	def test_edit_multiple_whitespace(self):
		pencil = Pencil(50, 50)
		pencil.write('Hello    world')
		pencil.edit(6, 'Susan')
		assert pencil.written_text == 'Hello Sus@@rld'