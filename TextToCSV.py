import os
import csv
import glob

SCRIPTDIR = os.path.dirname(os.path.realpath(__file__)) # holds location of python script
INDIR = os.path.join(SCRIPTDIR, 'YourPathName') # text files you want to convert
OUTDIR = os.path.join(SCRIPTDIR, 'LocationYouWantFilesIn') # location you want csv files to be dumped

txt_files = os.path.join(INDIR, '*.txt') # looks for files with a .txt extension

for txt_file in glob.glob(txt_files):
	with open(txt_file, "r") as input_file:
		in_txt = csv.reader(input_file, delimiter = ',') # delimiter is interchangeable
		filename = os.path.splitext(os.path.basename(txt_file))[0] + '.csv' # removes the .txt extension and replaces it with .csv extension
		
		with open(os.path.join(OUTDIR, filename), "w") as output_file:
			out_csv = csv.writer(output_file, lineterminator = '\n') # line terminator avoids extra rows generated in Windows-style line terminators \r\n
			out_csv.writerows(in_txt)

			print('Scan %-50s' % filename, end=' ') # shows user which files have been converted
			print("\tDone")