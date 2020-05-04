MAINDIR := ~/Documents/Covid-19/tfl_cam_mobility
TMPDIR := ${MAINDIR}/tmp
OUTDIR := ${MAINDIR}/output


default: count_vehicles

count_vehicles:
	/Users/hamishgibbs/anaconda3/bin/python main.py ${TMPDIR} ${OUTDIR}/output.csv
