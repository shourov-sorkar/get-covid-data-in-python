from covid import Covid
covid = Covid()
covid = Covid(source="john_hopkins") # get  data from john hopkins university
covid = Covid(source="worldometers") # get  data from john hopkins university
covid.get_data() # get  all data