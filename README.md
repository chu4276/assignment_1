# CDS504 Assignment 1
This is the group assignment for CDS504. We've implemented five MapReduce programs in this assignment. These implemented programs can be executed in local system or Hadoop MapReduce system.

## Required library for running MapReduce in local system or Hadoop environment
To run in local system or Hadoop, we need to install two libraries. Here is the command to install the required libraries. First library is for MapReduce framework to run Hadoop Streaming jobs and the second library is for converting our date to day such as 2020/05/07 to Thursday.

1. `pip install mrjob`
2. `pip install python-dateutil`

## Pivot
In pivot, we'll use "BreadBasket_DMS.csv" dataset to pivot and preprocess the dataset to be used with other MapReduce programs. From pivot.py, we will get three output textfiles which are support.txt, confidence.txt and lift.txt. Our pivot MapReduce program can be executed with this command.

Running in local system,
`python pivot.py BreadBasket_DMS.csv -q`

Running in Hadoop system,
`python pivot.py -r hadoop --hadoop-streaming-jar /hadoop-2.10.0/share/hadoop/tools/lib/hadoop-streaming-2.10.0.jar BreadBasket_DMS.csv`

## Support
In support, we'll use the "support.txt" dataset file as an input to our MapReduce program. For testing purposes, we've used the small dataset file which is "support_text.txt". Our support MapReduce program can be executed with this command.

Running in local system,
`python support.py support.txt -q`

Running in Hadoop system,
`python support.py -r hadoop --hadoop-streaming-jar /hadoop-2.10.0/share/hadoop/tools/lib/hadoop-streaming-2.10.0.jar support.txt`


## Confidence 
In confidence, we'll use the "confidence.txt" dataset file as an input to our MapReduce program. For testing purposes, we've used the small dataset file which is "confidence_test.txt". Our support MapReduce program can be executed with this command.

Running in local system,
`python confidence.py confidence.txt -q`

Running in Hadoop system,
`python confidence.py -r hadoop --hadoop-streaming-jar /hadoop-2.10.0/share/hadoop/tools/lib/hadoop-streaming-2.10.0.jar confidence.txt`


## Lift
In lift, we'll use the "support.txt" dataset file as an input to our MapReduce program. For testing purposes, we've used the small dataset file which is called "lift_test.txt". Our lift MapReduce program can be executed with this command.

Running in local system,
`python lift.py lift.txt -q`

Running in Hadoop system,
`python lift.py -r hadoop --hadoop-streaming-jar /hadoop-2.10.0/share/hadoop/tools/lib/hadoop-streaming-2.10.0.jar lift.csv`

## Sales Comparison
In sales comparison part, we'll use the "BreadBasket_DMS.csv" dataset file as an input to our MapReduce program. Our sales_comparison MapReduce program can be executed with this command.

Running in local system,
`python sales_comparison.py BreadBasket_DMS.csv -q`

Running in Hadoop system,
`python sales_comparison.py -r hadoop --hadoop-streaming-jar /hadoop-2.10.0/share/hadoop/tools/lib/hadoop-streaming-2.10.0.jar BreadBasket_DMS.csv`

**Notes:**
For Hadoop Streaming java file (hadoop_streaming-2.10.0.jar), file path and file name may be varied based on Hadoop system version and installation.
