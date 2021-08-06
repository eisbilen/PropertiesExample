import pandas as pd
import tensorflow as tf


class CSVGetInfo(object):
 """ This class displays the summary of the tabular data contained 
 in a CSV file """
 def __init__(self, path, file_name):
  self._path = path
  self._file_name = file_name

 @property
 def path(self):
  """ The docstring for the path property """
  print("Getting value of path")
  return self._path

 @path.setter
 def path(self,value):
  if '/' in value:
   self._path = value
   print("Setting value of path to {}".format(value))
  else:
   print("Error: {} is not a valid path string".format(value))
 @path.deleter
 def path(self):
  print('Deleting path attribute')
  del self._path
 @property
 def file_name(self):
  """ The docstring for the file_name property """
  print("Getting value of file_name")
  return self._file_name
 @file_name.setter
 def file_name(self,value):
  if '.' in value:
   self._file_name = value
   print("Setting value of file_name to {}".format(value))
  else:
   print("Error: {} is not a valid file name".format(value))
 @file_name.deleter
 def file_name(self):
  print('Deleting file_name attribute')
  del self._file_name
 def display_summary(self):
  data = pd.read_csv(self._path + self._file_name)
  print(self._file_name)
  print(data.info())
if __name__ == '__main__':
 data_by_genres = CSVGetInfo("/Users/erdemisbilen/Lessons/", 
 "data_by_genres.csv")
 print(data_by_genres.path)
 print(data_by_genres.file_name)
 data_by_genres.path="lessons"
 print(data_by_genres.path)
 data_by_genres.path="/Users/"
 print(data_by_genres.path)
 del data_by_genres.path
 data_by_genres.file_name="datacsv"
 print(data_by_genres.file_name)
 data_by_genres.file_name="data.csv"
 print(data_by_genres.file_name)
 del data_by_genres.file_name
