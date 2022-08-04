#  <img src="https://media.giphy.com/media/3o7TKz2eMXx7dn95FS/giphy.gif" width="50" height="50" /> DNA - Reversing & Complementing (FASTA format)

## Introduction

The purpose of this project is to simply reverse and complement DNA sequences in the FASTA format ! What is interesting about this program is the fact that :

- At every step of the process, some piece of information are displayed on the terminal to ensure that you know what is going on.

- The DNA sequences are displayed using a color coded scheme such that the different nucleotides are easily observable.

- The input files must simply be placed inside the *input* folder and the outputs of the program will be placed immediately in the *output* folder.

## Illustration

![](/assets/illustration.png)

## Installation

- First of all, it is **required** to install Python on your computer. If it nos already done, you can do it using the following [link](https://www.python.org/downloads/).

- Furthermore, it is needed to install the *Bio* library using the following command:

```
pip3 install Bio
```

- Finally, it is needed to allow the *shell script* to run on your computer using the command:

```
chmod 744 run.sh
```

(Do not forget to place yourself inside the root of the folder !)

## Running the program

From now on, if you want to do the reverse and complement of a DNA sequence in FASTA format, you just
have to place your .txt file inside the INPUT folder. I already placed a file named "test_small.txt" and 
"test_large.txt" such that you can see what the program is capable of ! Then you are setup ! 

In the root folder, just type the command on your terminal

```
./run.sh
```

**NOTE**: The results will be showed on your terminal as well as saved in a .txt file inside the folder OUTPUT

## License

Copyright [2022] [Mangeleer Victor]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
