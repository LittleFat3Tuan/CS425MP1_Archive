# CS425_MP1_LiYao

This is the git repo for CS426/ECE428 Fall 2022 MP1.

Group 61: Gan Yao(ganyao2), Linxi Li(linxili2)

We used Python3 to implement MP1.

## Repo contents

`src_new` contains our system source files and test files. \
`MP1DemoDataFA22.zip` contains log files for demo. \
`ipAdressess.txt` is a text file recording IP addressess of all our 10 VMs. \
`test_logs.zip` contains test log files used for our own unit tests. \
`MP1_report_LiYao.pdf` is our report for MP1. 

## Source files

Our source files consists of two files in `src_new` folder, which are `server.py` and `client.py`. As indicated by file name, they implemented server-client model together. \
\
To run server on VMs, simply type the following command on terminal,
```python
pthon3 server.py
```

To run grep commands to query on log files across all VMs that have server running, type the following command,
```python
pthon3 client.py
```
You will see the following prompt,
```
please enter your command:
```
You can then type the grep command and proceed.

## Tests

`unit_test.py` in `src_new` folder is our own unit test script developed before the release of demo log files.,To run it:
```python
pthon3 unit_test.py
```
`timed_tests_[freq/infreq/swfreq/regfreq].py` in `src_new` folder are timed tests used to measure our system performance. You can run it in a similar manner as above.

