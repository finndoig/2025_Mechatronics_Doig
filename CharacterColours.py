# CharacterColours.py

def get_characters():
	"""Return the `Characters` list defined by this module.

	The function creates the character RGB-range arrays and returns a
	list of character names. Call this from other modules to obtain the
	`Characters` value.
	"""

	# Arrays for the rgb ranges of each character
	Character1 = [57,  141, 188, 77, 161, 208]   # r_min, g_min, b_min, r_max, g_max, b_max
	Character2 = [235, 180, 61, 255, 200, 81]
	Character3 = [186, 139, 233, 206, 159, 253]
	Character4 = [221, 239, 93, 241, 255, 113]

	Characters = [Character1, Character2, Character3, Character4]
	return Characters


# Backwards-compatible module-level variable
Characters = get_characters()


if __name__ == "__main__":
	# Example usage when run as a script
	print("Characters:", get_characters())