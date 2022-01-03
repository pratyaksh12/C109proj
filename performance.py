from _plotly_utils import colors
import pandas as pd
import statistics as st
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go 

df=pd.read_csv('std.csv')
math_list=df['math score'].to_list()
read_list=df['reading score'].to_list()
write_list=df['writing score'].to_list()

math_mean=st.mean(math_list)
read_mean=st.mean(read_list)
write_mean=st.mean(write_list)

math_median=st.median(math_list)
read_median=st.median(read_list)
write_median=st.median(write_list)

math_mode=st.mode(math_list)
read_mode=st.mode(read_list)
write_mode=st.mode(write_list)

print("mean, median and mode of math score is {}, {} and {} respectively".format(math_mean, math_median, math_mode))
print("mean, median and mode of reading score is {}, {} and {} respectively".format(read_mean, read_median, read_mode))
print("mean, median and mode of writing score is {}, {} and {} respectively".format(write_mean, write_median, write_mode))

math_stdev=st.stdev(math_list)
read_stdev=st.stdev(read_list)
write_stdev=st.stdev(write_list)

math_first_start,math_first_end=math_mean-math_stdev,math_mean+math_stdev
math_second_start,math_second_end=math_mean-(2*math_stdev),math_mean+(2*math_stdev)
math_third_start,math_third_end=math_mean-(3*math_stdev),math_mean+(3*math_stdev)

read_first_start,read_first_end=read_mean-read_stdev,read_mean+read_stdev
read_second_start,read_second_end=read_mean-(2*read_stdev),read_mean+(2*math_stdev)
read_third_start,read_third_end=read_mean-(3*read_stdev),read_mean+(3*read_stdev)

write_first_start,write_first_end=write_mean-write_stdev,write_mean+write_stdev
write_second_start,write_second_end=write_mean-(2*write_stdev),write_mean+(2*write_stdev)
write_third_start,write_third_end=write_mean-(3*write_stdev),write_mean+(3*write_stdev)

math_list_of_data_within_1_std_deviation = [result for result in math_list if result > math_first_start and result < math_first_end]
math_list_of_data_within_2_std_deviation = [result for result in math_list  if result > math_second_start and result < math_second_end]
math_list_of_data_within_3_std_deviation = [result for result in math_list  if result > math_third_start and result < math_third_end]

read_list_of_data_within_1_std_deviation = [result for result in read_list if result > read_first_start and result < read_first_end]
read_list_of_data_within_2_std_deviation = [result for result in read_list if result > read_second_start and result < read_second_end]
read_list_of_data_within_3_std_deviation = [result for result in read_list if result > read_third_start and result < read_third_end]

write_list_of_data_within_1_std_deviation = [result for result in read_list if result > write_first_start and result < write_first_end]
write_list_of_data_within_2_std_deviation = [result for result in read_list if result > write_second_start and result < write_second_end]
write_list_of_data_within_3_std_deviation = [result for result in read_list if result > write_third_start and result < write_third_end]


print("{}% of data for math score lies within 1 standard deviation".format(len(math_list_of_data_within_1_std_deviation)*100.0/len(math_list)))
print("{}% of data for math score lies within 2 standard deviations".format(len(math_list_of_data_within_2_std_deviation)*100.0/len(math_list)))
print("{}% of data for math score lies within 3 standard deviations".format(len(math_list_of_data_within_3_std_deviation)*100.0/len(math_list)))
print("{}% of data for reading score lies within 1 standard deviation".format(len(read_list_of_data_within_1_std_deviation)*100.0/len(read_list)))
print("{}% of data for reading score lies within 2 standard deviations".format(len(read_list_of_data_within_2_std_deviation)*100.0/len(read_list)))
print("{}% of data for reading score lies within 3 standard deviations".format(len(read_list_of_data_within_3_std_deviation)*100.0/len(read_list)))
print("{}% of data for writing score lies within 1 standard deviation".format(len(write_list_of_data_within_1_std_deviation)*100.0/len(write_list)))
print("{}% of data for writing score lies within 2 standard deviations".format(len(write_list_of_data_within_2_std_deviation)*100.0/len(write_list)))
print("{}% of data for writing score lies within 3 standard deviations".format(len(write_list_of_data_within_3_std_deviation)*100.0/len(write_list)))

fig=ff.create_distplot([math_list],['math score'],show_hist=False)
fig.add_trace(go.Scatter(x=[math_mean,math_mean], y=[0,0.05],mode='lines',name='mean'))
fig.add_trace(go.Scatter(x=[math_first_start,math_first_start],y=[0,0.05],mode='lines',name='First standard devition'))
fig.add_trace(go.Scatter(x=[math_first_end,math_first_end],y=[0,0.05],mode='lines',name='First standard devition'))
fig.add_trace(go.Scatter(x=[math_second_start,math_second_start],y=[0,0.05],mode='lines',name='First standard devition'))
fig.add_trace(go.Scatter(x=[math_second_end,math_second_end],y=[0,0.05],mode='lines',name='First standard devition'))
fig.add_trace(go.Scatter(x=[math_third_start,math_third_start],y=[0,0.05],mode='lines',name='First standard devition'))
fig.add_trace(go.Scatter(x=[math_third_end,math_third_end],y=[0,0.05],mode='lines',name='First standard devition'))
fig.show()


