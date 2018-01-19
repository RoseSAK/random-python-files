import numpy as np


def make_cells(grid):
	"""
	Takes a n x m dimensional numpy array and creates 3x3 cells i.e. one cell for each unit in 
	the array and its surrounding units
	"""
	cell_shape = (3,3)
	view_shape = tuple(np.subtract(grid.shape, cell_shape) + 1) + cell_shape
	strides = grid.strides + grid.strides

	sub_matrices = np.lib.stride_tricks.as_strided(grid,view_shape,strides)
	#print(sub_matrices)
	return sub_matrices
	
def get_cell_status(cell):
	"""
	Takes a cell and returns the value for that cell i.e. whether it is dead (0) or alive(1)
	"""
	#if cell.shape == (3,3):
	cell_status = cell[1, 1]
	return cell_status

def update_cell(cell):
	"""
	Looks at what the cell state should be in the next iteration, given the states of its neighbouring cells
	i.e. according to the rules of the game of Life:
	A live cell with 2 or 3 neighbours will continue living
	A live cell with more than 3 neighbours or less than 2 neighbours will die - overpopulation/underpopulation
	A dead cell with exactly 3 neighbours will become live - reproduction 
	"""
	status = get_cell_status(cell)
	#print(status)
	neighbours = np.delete(cell, [1, 1])
	live_cells = np.count_nonzero(cell == 1)
	#print(live_cells)
	if live_cells == 3 or (status == 1 and live_cells == 2):
		update = 1
	else:
		update = 0
	return update 

def life_step(grid):
	"""
	Updates every cell in a grid 
	"""
	print(grid)
	cells = make_cells(grid)
	update_values = []
	for l in cells:
		for single_cell in l:
			#print(cell)
			update = update_cell(single_cell)
			update_values.append(update)
	new_grid = np.asarray(update_values).reshape(7, 7)
	print(new_grid)
	return new_grid


if __name__ == "__main__":
	grid = np.random.randint(2, size=(9, 9))
	while np.count_nonzero(grid == 1)>1:
		grid = life_step(grid)

#life_step(grid_A)



