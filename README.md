# Hadoop-montyHall

This mapper will do 3 trails of 10 instances

```bash 
hdfs dfs -put red1.py /user
hdfs dfs -put map1.py /user

hdfs dfs -chmod go+wx /user/map1.py
hdfs dfs -chmod go+wx /user/red1.py

hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.10.1.jar -file map1.py -mapper map1.py -file red1.py -reducer red1.py -input /user/testfile.txt -output /output
```

The output will be saved in /output 

```bash
hdfs dfs -cat /output/part-00000
```

references:
https://github.com/maleckicoa/Monty-Haul/blob/master/Monty%20Haul.ipynb

http://www.science.smith.edu/dftwiki/index.php/Map-Reduce_Examples
