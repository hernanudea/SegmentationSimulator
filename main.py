from tkinter import Tk
from Segmentation import Segmentation

if __name__ == '__main__':
    window = Tk()
    app = Segmentation(window)
    window.mainloop()


"""

add_process
    calculate_in_v_memory
	    paint_in_v_memory

	calculate_in_v_memory
	    paint_in_p_memory
		    best_fit



"""