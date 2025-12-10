# Apenas colheita manual
harvest()

# colheita automática, mas pouco eficiente
while True:
	harvest()

# colheita automática, mais eficiente
while True:
	if can_harvest():
		harvest()

# colheita automática,  mais eficiente mais zona de colheitas
while True:
	if can_harvest():
		harvest()
	else:
		move(North)
