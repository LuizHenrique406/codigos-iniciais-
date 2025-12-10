# colheita automática,  mais eficiente mais zona de colheitas
while True:
	if can_harvest():
		harvest()
	else:
		move(North)
