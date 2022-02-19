def script(check, x, y):
	if check("gold", x, y):
		return "take"
	if check("gold", x + 1, y):
		return "right"
	if check("gold", x, y - 1):
		return "up"
	if check("gold", x - 1, y):
		return "left"
	if check("gold", x, y + 1):
		return "down"
	if check("level") == 1 or check("level") == 2:
		if not check("wall", x + 1, y):
			return "right"
		if not check("wall", x, y - 1):
			return "up"
		if not check("wall", x - 1, y):
			return "left"
		if not check("wall", x, y + 1):
			return "down"
	if check("level") == 3:
		if check("wall", x, y - 1) and not check("wall", x + 1, y):
			return "right"
		if check("wall", x + 1, y - 1) and not check("wall", x + 1, y):
			return "right"
		if check("wall", x - 1, y) and not check("wall", x, y - 1):
			return "up"
		if check("wall", x - 1, y - 1) and not check("wall", x, y - 1):
			return "up"
		if check("wall", x, y + 1) and not check("wall", x - 1, y):
			return "left"
		if check("wall", x - 1, y + 1) and not check("wall", x - 1, y):
			return "left"
		if check("wall", x + 1, y) and not check("wall", x, y + 1):
			return "down"
		if check("wall", x + 1, y + 1) and not check("wall", x, y + 1):
			return "down"
	if check("level") == 4:
		if check("wall", x + 1, y) and not check("wall", x - 1, y) and check("wall", x - 2, y) and check("wall", x - 3, y - 1) and check("wall", x + 1, y - 3):
			return "left"
		if check("wall", x + 1, y) and not check("wall", x - 1, y) and check("wall", x - 2, y) and check("wall", x - 3, y - 1) and check("wall", x + 1, y + 3):
			return "left"
		if check("wall", x - 1, y + 1) and check("wall", x - 1, y + 2) and check("wall", x + 2, y) and not check("wall", x + 3, y):
			return "right"
		if check("wall", x - 1, y + 1) and check("wall", x - 1, y + 2) and check("wall", x - 2, y + 2) and check("wall", x + 2, y + 1) and not check("wall", x + 3, y + 2):
			return "right"
		if check("wall", x + 1, y - 1) and check("wall", x + 1, y - 2) and check("wall", x - 2, y) and not check("wall", x - 3, y):
			return "up"

		if check("wall", x - 1, y) and not check("wall", x, y + 1):
			return "down"
		if check("wall", x - 1, y + 1) and not check("wall", x, y + 1):
			return "down"
		if check("wall", x, y + 1) and not check("wall", x + 1, y):
			return "right"
		if check("wall", x + 1, y + 1) and not check("wall", x + 1, y):
			return "right"
		if check("wall", x + 1, y) and not check("wall", x, y - 1):
			return "up"
		if check("wall", x + 1, y - 1) and not check("wall", x, y - 1):
			return "up"
		if check("wall", x, y - 1) and not check("wall", x - 1, y):
			return "left"
		if check("wall", x - 1, y - 1) and not check("wall", x - 1, y):
			return "left"
	return "pass"
