#  <img src="https://media.giphy.com/media/3o7TKz2eMXx7dn95FS/giphy.gif" width="50" height="50" /> DNA - Reversing & Complementing (FASTA format - Terminal)

---------------------- 
                                    INTRODUCTION
----------------------

---------------------- 
    INSTALLATION
----------------------

1 - In order to run the program, you have to first install python3 on your macbook ! In order to do so, 
    you can simply download it on this webpage:

								https://www.python.org/downloads/


	and install it ! If does not work, you can refer to this tutorial:

								https://www.dataquest.io/blog/installing-python-on-mac/


	Once it is done, you can check it works by writing 

								python

	in your terminal ! Nice ! You can exit this mode by writing

								exit()

	in the terminal !


2 - Now, the next step is to simply install a library, to do so type
				
								pip install Bio



3 - It is almost done, now you can move inside the root folder of the project using your good old "cd" command.



4 - In order to run the program, you have to give it just once the permission to run ! Thus, you can run the
    following command in your terminal

								chmod 744 run_DNA_RC.sh


------------------------------
     RUNNING THE PROGRAM
------------------------------

All the former steps must be done only once ! That's nice isn't it ? :-)


From now on, if you want to do the reverse and complement of a DNA sequence in FASTA format, you just
have to place your .txt file inside the INPUT folder. I already placed a file named "test_small.txt" and 
"test_large.txt" such that you can see what the program is capable of ! Then you are setup ! 


NOTE: The results will be showed on your terminal as well as saved in a .txt file inside the folder OUTPUT


In the root folder, just type the command on your terminal

								./run_DNA_RC.sh

and let the magic do its work !




Kiss kiss, hope you enjoy it !


















