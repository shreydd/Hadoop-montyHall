# Hadoop-montyHall

This mapper will do 3 trails of 10 instances

```bash 
hdfs dfs -put reducer.py /user
hdfs dfs -put mapper.py /user

hdfs dfs -chmod go+wx /user/mapper.py
hdfs dfs -chmod go+wx /user/reducer.py

hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.10.1.jar -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input /user/inputfile.txt -output /output
```

The output will be saved in /output 

```bash
hdfs dfs -cat /output/part-00000
```

references:
https://github.com/maleckicoa/Monty-Haul/blob/master/Monty%20Haul.ipynb

http://www.science.smith.edu/dftwiki/index.php/Map-Reduce_Examples
