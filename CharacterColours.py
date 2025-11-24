# CharacterColours.py

def get_characters():
	"""Return the `Characters` list defined by this module.

	The function creates the character RGB-range arrays and returns a
	list of character names. Call this from other modules to obtain the
	`Characters` value.
	"""

	# Arrays for the rgb ranges of each character
	# Character1 = [37,  121, 168, 97, 181, 228]   # r_min, g_min, b_min, r_max, g_max, b_max
	Character1 = [0, 20, 70, 30, 80, 150] # finn
	Character2 = [170, 80, 45, 230, 150, 105] # jake
	Character3 = [90, 20, 30, 170, 70, 80] # lsp
	Character4 = [140, 125, 60, 180, 165, 100] # tree trunk

	Characters = [Character1, Character2, Character3, Character4]
	return Characters


# Backwards-compatible module-level variable
Characters = get_characters()


if __name__ == "__main__":
	# Example usage when run as a script
	print("Characters:", get_characters())