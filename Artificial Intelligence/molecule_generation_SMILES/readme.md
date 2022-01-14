<h2> Files</h2>
<body>
    <b>smiles </b>: Virtual Environment - Use source /smiles/bin/activate to activate the virtual env<br>
    <b>datasets/download.sh </b>: Bash script to download datasets 
		Usage : bash download.sh gdb13 OR bash download.sh gdb17 or bash download.sh gdb17
<br>
    <b>datasets/delete.sh </b>: bash script to delete files in the folder. 
		Usage : bash delete.sh gdb11_ where gdb11 is the grep string to search for.
<br>
    <b>datasets/extract.sh </b>: To extract files from a tar file and to save it in a folder

<br>
<b>datasets/gdb11.tgz </b> : Datset extracted from gdb.unibe.ch<br>
<b>datasets/data-source.txt </b> : List of all dataset and sources<br>

<b>scripts/check_molecule.py </b> : Molecule utilizing smilite to get ZINC ID of a string. If invalid, it will return error

<br>
<b>scripts/gdb11_size10.smi</b> : SMILES dataset having size 11 <br>
<b>scripts/molecule_generation_using_VAE.ipynb</b> : Notebook with Molecule generation using VAE on gdb11 script. <br>
<b>scripts/project.zip</b> : Compressed project folder with datasets, models and ipynb<br>
<b>scripts/ZINC_DB_molecule_generation_using_LSTM_VAE.ipynb</b> : Notebook with molecule generation using LSTM Autoencoder on ZINC15 dataset<br>
<b>scripts/ZINC_DB_molecule_generation_using_LSTM_VAE.pdf </b> : PDF version of above notebook..


Credits for data :https://gdb.unibe.ch/downloads/
		 :https://zinc.docking.org/substances/
		 :https://zinc.docking.org/substances/search/?q=ZINC15
		 :https://zinc.docking.org/substances/subsets/for-sale.csv?count=all with 'for_sale' filter
		 
		 
		 
Learnings : 
The latent space can be changed to generate new molecules using LSTM AutoEncoder


