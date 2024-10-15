import numpy as np;
import pandas as pd;

# 1. Define two custom numpy arrays, say A and B. Generate two new numpy
# arrays by stacking A and B vertically and horizontally.
A = np.array([0, 1, 2, 3, 4, 5]);
B = np.array([4, 5, 6, 7, 8, 9]);
vertically = np.vstack((A, B));
horizontally = np.hstack((A, B));
print(vertically);
print(horizontally);

# 2. Find common elements between A and B. [Hint : Intersection of two sets]
intersection = np.intersect1d(A, B);
print(intersection);

# 3. Extract all numbers from A which are within a specific range. eg
# between 5 and 10. [Hint: np.where() might be useful or boolean masks]
in_range = A[(5 <= A) & (A <= 10)];
print(in_range);

# 4. Filter the rows of iris_2d that has petallength (3rd column) > 1.5
# and sepallength (1st column) < 5.0
url = './iris.data.txt';
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3]);
iris_2d_filtered = iris_2d[(iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5.0)];
print(iris_2d_filtered);

# 5. From df filter the 'Manufacturer', 'Model' and 'Type' for every
# 20th row starting from 1st (row 0).
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv');
df_filtered = df.loc[::20, "Manufacturer" : "Type"];
print(df_filtered);

# 6. Replace missing values in Min.Price and Max.Price columns with
# their respective mean.
mean_minprice = df["Min.Price"].mean();
mean_maxprice = df["Max.Price"].mean();
df["Min.Price"] = df["Min.Price"].fillna(mean_minprice);
df["Max.Price"] = df["Max.Price"].fillna(mean_maxprice);
print(df[["Min.Price", "Max.Price"]]);

# 7. How to get the rows of a dataframe with row sum > 100?
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4));
df_filtered = df[df.sum(axis=1) > 100];
print(df_filtered);
