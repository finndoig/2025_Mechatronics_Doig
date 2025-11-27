# CharacterColours.py

def get_characters():
	"""Return the `Characters` list defined by this module.

	The function creates the character RGB-range arrays and returns a
	list of character names. Call this from other modules to obtain the
	`Characters` value.
	"""

	# Arrays for the rgb ranges of each character
	# Character1 = [37,  121, 168, 97, 181, 228]   # r_min, g_min, b_min, r_max, g_max, b_max
	Character1 = [0, 20, 60, 30, 80, 140] # finn
	Character2 = [155, 70, 35, 220, 140, 100] # jake
	Character3 = [80, 18, 25, 150, 60, 70] # lsp
	Character4 = [35, 105, 80, 100, 160, 120] # tree trunk

	Characters = [Character1, Character2, Character3, Character4]
	return Characters


# Backwards-compatible module-level variable
Characters = get_characters()


if __name__ == "__main__":
	# Example usage when run as a script
	print("Characters:", get_characters())