def generate_groups():
	sp = []
	for i in range(1, 9):
		sp.append(f"ИВБО-0{i}-20")
	sp.append("ИВБО-13-20")
	for i in range(1, 10):
		sp.append(f"ИКБО-0{i}-20")
	for i in range(10, 28):
		sp.append(f"ИКБО-{i}-20")
	sp.append("ИКБО-30-20")
	for i in range(1, 10):
		sp.append(f"ИНБО-0{i}-20")
	sp.append("ИНБО-10-20")
	sp.append("ИНБО-11-20")
	sp.append("ИНБО-13-20")
	sp.append("ИНБО-15-20")
	sp.append("ИМБО-01-20")
	sp.append("ИМБО-02-20")
